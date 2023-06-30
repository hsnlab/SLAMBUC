# Copyright 2023 Janos Czentye
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import collections
import datetime
import itertools
import logging
import math
import os
import pathlib
import signal
import sys
import time

import networkx as nx
import pandas as pd
import tabulate

from governor import TestGovernor
from slambuc.alg import INFEASIBLE
from slambuc.alg.service import *
from slambuc.alg.util import ibacktrack_chain, ipowerset, par_subchain_latency
from slambuc.gen.io import iload_trees_from_file, get_tree_from_file

# Default params
DEF_PARAMS = dict(root=1, delay=10)
DEF_LOG_FILE = f"{__name__}.log"
RES_COLS = ('Tree', 'Alg', 'M', 'L', 'N', 'Part', 'Cost', 'Lat', 'Time')
# Test governor params
GOV_MEM_LIMIT = 0.9
GOV_TIME_LIMIT = 0
GOV_INT = 3
GOV_LOG = True
# Setup logging
log = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(logging.Formatter("%(message)s"))
fh = logging.FileHandler(DEF_LOG_FILE, 'w')
fh.setFormatter(logging.Formatter("%(message)s"))
log.handlers.extend((sh, fh))


class ExternalAbortInterrupt(BaseException):
    """Specific class for signaling aborted tests case from outer scope (observer process)"""
    pass


class InternalTimeoutInterrupt(BaseException):
    """Specific class for signaling timeout tests case from inner scope"""
    pass


def _ext_abort_handler(*args):
    """Transform and propagate caught SIGABRT signal to a dedicated exception and supress further signals"""
    supress_int_signals()
    raise ExternalAbortInterrupt(*args)


def _int_alarm_handler(*args):
    """Transform and propagate caught SIGALRM signal to a dedicated exception and supress further signals"""
    supress_int_signals()
    raise InternalTimeoutInterrupt(*args)


def set_int_signal_handlers():
    """Register signal handlers"""
    signal.signal(signal.SIGABRT, _ext_abort_handler)
    signal.signal(signal.SIGALRM, _int_alarm_handler)


def supress_int_signals():
    """Suppress signals from interrupting execution"""
    signal.signal(signal.SIGABRT, signal.SIG_IGN)
    signal.signal(signal.SIGALRM, signal.SIG_IGN)


def reset_int_signal_handlers():
    """Reset default signal handlers"""
    signal.signal(signal.SIGABRT, signal.SIG_DFL)
    signal.signal(signal.SIGALRM, signal.SIG_DFL)


def calc_min_max_latency(tree: nx.DiGraph, cpath: list[int], delay: int, N: int = 1) -> tuple[int, int]:
    """Calculate the min/max latency values for the given *cpath* with exhaustive search"""
    cp_len, cp_set, min_lats, max_lats = len(cpath), set(cpath), math.inf, 0
    for cut in ipowerset(range(1, cp_len)):
        blk_lats = [par_subchain_latency(tree, cpath[i], set(cpath[i:j]), cp_set, N)
                    for i, j in itertools.pairwise([0, *cut, cp_len])]
        sum_lats = sum(blk_lats) + (len(blk_lats) - 1) * delay
        min_lats, max_lats = min(min_lats, sum_lats), max(max_lats, sum_lats)
    return min_lats, max_lats


def est_min_max_latency(tree: nx.DiGraph, cpath: list[int], delay: int, N: int = 1) -> list[int, int]:
    """Estimate the min/max latency values for the given *cpath* by considering all cuts and singleton group cases"""
    cp_set = set(cpath)
    singleton_lat = sum(par_subchain_latency(tree, v, {v}, cp_set, N) for v in cpath) + (len(cpath) - 1) * delay
    monolith_lats = par_subchain_latency(tree, cpath[0], cp_set, cp_set, N)
    return sorted((singleton_lat, monolith_lats))


def decode_partitioning(part: list[list[int]], sep: str = '|') -> str:
    """Decode partitioning  to a compressed format of barrier nodes"""
    return f"[{sep.join(map(str, (f'{p[0][0]}@{p[-1]}' if isinstance(p, tuple) else p[0] for p in part)))}]"


def test_cleanup(tmp: str = "/tmp"):
    """Do cleanup after alg tests"""
    for tmp_ext in ('*.lp', '*.sol'):
        for tf in pathlib.Path(tmp).glob(tmp_ext):
            os.remove(tf)


########################################################################################################################


def run_all_algs(algs: dict[str, collections.abc.Callable], params: dict[str, int | float | nx.DiGraph],
                 timeout: int = 0, sdelay: int = 0) -> list[int | str]:
    """Perform test case of all given algorithms with given parameters and return execution statistics"""
    stats = []
    for alg_name, tree_alg in algs.items():
        log.debug(f"Executing {alg_name}")
        result, t_delta = INFEASIBLE, None
        t_start = time.perf_counter()
        try:
            set_int_signal_handlers()
            # Set up timer
            signal.alarm(timeout)
            t_start = time.perf_counter()
            result = tree_alg(**params)
            t_delta = time.perf_counter() - t_start
            # Disable timer
            signal.alarm(0)
            # Delay alg executions for a possible delayed interruption and ensure the measured delta > timeout
            time.sleep(sdelay)
        except ExternalAbortInterrupt:
            log.warning(f">>> Execution ABORTED due to exceeded memory limit")
        except InternalTimeoutInterrupt:
            log.warning(f">>> Execution ABORTED due to exceeded time limit")
        except Exception as e:
            log.critical(f"Got exception during execution of algorithm: {alg_name}")
            log.error(e, exc_info=False)
        finally:
            if t_delta is None:
                t_delta = time.perf_counter() - t_start
            stats.append([params['tree'].graph[NAME], alg_name, params['M'], params['L'], params.get('N'),
                          decode_partitioning(result[0]), *result[1:], t_delta])
    return stats


def validate(algs: dict[str, collections.abc.Callable], tree: nx.DiGraph, mem_coeff: int | float = 0.5,
             lat_coeff: int | float = 0.5, N: int = 1, timeout: int = 0, sdelay: int = 0,
             **alg_params: dict) -> list[list[str, int]]:
    """Validate execution of given algorithms based on the given test parameters"""
    if isinstance(mem_coeff, float):
        m_min = max(tree.nodes[v].get(MEMORY, 0) for v in tree)
        m_max = sum(tree.nodes[v].get(MEMORY, 0) for v in tree)
        M = round(mem_coeff * m_max + (1 - mem_coeff) * m_min)
        log.debug(f"Calculated memory limit: {M=} ({m_min} - {m_max}) with {mem_coeff=}")
    else:
        M = mem_coeff
    cp_end = max(v for v in tree if v is not PLATFORM)
    cpath = list(reversed(list(ibacktrack_chain(tree, 1, cp_end))))
    log.debug(f"Critical path: {cpath}")
    if isinstance(lat_coeff, float):
        l_min, l_max = est_min_max_latency(tree, cpath, delay=DEF_PARAMS['delay'])
        L = round(lat_coeff * l_max + (1 - lat_coeff) * l_min)
        log.debug(f"Estimated latency limit: {L=} ({l_min} - {l_max}) with {lat_coeff=}")
    else:
        L = lat_coeff
    alg_params.update(tree=tree, cp_end=cp_end, M=M, L=L, **DEF_PARAMS)
    if N > 1:
        alg_params.update(N=N)
    log.debug(f"Tree partitioning params: [{alg_params}]")
    log.debug(f"Start test execution at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info('#' * 80)
    stats = run_all_algs(algs, alg_params, timeout=timeout, sdelay=sdelay)
    log.info('#' * 80)
    log.info(tabulate.tabulate(stats, RES_COLS, stralign='decimal', tablefmt='pretty'))
    log.debug("Cleanup...")
    test_cleanup()
    return stats


def execute_tests(algs: dict[str, collections.abc.Callable], test_file: str, mem_coeff: int | float,
                  lat_coeff: int | float, N: int, output_dir: str = "results", output_file: str = None,
                  tree_num: int = None, timeout: int = 0, **alg_params: dict):
    """
    Execute tests based on the given parameters.

    :param algs:        dict of algorithms
    :param test_file:   generated input trees
    :param mem_coeff:   coefficient [0 - 1.0] for generating memory limit M
    :param lat_coeff:   coefficient [0 - 1.0] for generating latency limit M
    :param N:           number of assumed vCPU core
    :param output_dir:  output directory for result statistics
    :param output_file: file name of the results
    :param tree_num:    run test only with the given tree
    :param timeout:     set timeout for algs (no timeout: 0)
    :param alg_params:  additional algorithm parameters
    """
    test_file = pathlib.Path(test_file).resolve()
    if not test_file.exists():
        log.error(f"Missing test file: {test_file}")
        return
    log.info(f"Load trees from file: {test_file}")
    output_file = test_file if output_file is None else pathlib.Path(output_file)
    output_file = pathlib.Path(output_dir, output_file.name).resolve().with_suffix('.csv')
    if tree_num:
        output_file = output_file.with_stem(output_file.stem + f"_t{tree_num}")
    if output_file.exists():
        log.debug(f"Remove existing results file: {output_file}")
        os.remove(output_file)
    log.info(f"Dumping results to {output_file}")
    log.info(f"Applied timeout for algorithm execution: {timeout} s")
    log.debug(f"Perform tests in main process: {os.getpid()}")
    supress_int_signals()
    gov = TestGovernor(mem_limit=GOV_MEM_LIMIT, time_limit=GOV_TIME_LIMIT, interval=GOV_INT)
    gov.start()
    log.debug(f"Subprocess initiated: {gov}")
    if tree_num:
        log.info(f"Execute test for single input tree: {tree_num}")
        tree = get_tree_from_file(test_file, tree_num)
        tree_name = test_file.stem.rsplit('_', 1)[0] + f"_{tree_num}"
        tree.graph[NAME] = tree_name
        log.info(f" {test_file.name} -> {tree_name} ".center(80, '#'))
        res = validate(algs, tree, mem_coeff, lat_coeff, N, timeout=timeout, **alg_params)
        pd.DataFrame(res, columns=RES_COLS).to_csv(output_file, mode='w', header=False, index=False)
    else:
        pd.DataFrame([], columns=RES_COLS).to_csv(output_file, mode='w', header=True, index=False)
        for i, tree in enumerate(iload_trees_from_file(test_file), start=1):
            tree_name = test_file.stem.rsplit('_', 1)[0] + f"_{i}"
            tree.graph[NAME] = tree_name
            log.info(f" {test_file.name} -> {tree_name} ".center(80, '#'))
            res = validate(algs, tree, mem_coeff, lat_coeff, N, timeout=timeout, sdelay=gov.interval, **alg_params)
            pd.DataFrame(res, columns=RES_COLS).to_csv(output_file, mode='a', header=False, index=False)
    gov.shutdown()
    reset_int_signal_handlers()


########################################################################################################################


def compare_latency_limit_estimation(test_file: str, lat_coeff: float = 0.5):
    """Compare calculated and estimated values for minimal and maximal latency limits"""
    test_file = pathlib.Path(test_file).resolve()
    print("Load trees from file:", test_file)
    diffs = []
    for i, tree in enumerate(iload_trees_from_file(test_file)):
        cp_end = max(v for v in tree if v is not PLATFORM)
        cpath = list(reversed(list(ibacktrack_chain(tree, 1, cp_end))))
        lc_min, lc_max = calc_min_max_latency(tree, cpath, delay=DEF_PARAMS['delay'])
        Lc = round(lat_coeff * lc_max + (1 - lat_coeff) * lc_min)
        print(f"Calculated latency limit: {Lc=} ({lc_min} - {lc_max})")
        le_min, le_max = est_min_max_latency(tree, cpath, delay=DEF_PARAMS['delay'])
        Le = round(lat_coeff * le_max + (1 - lat_coeff) * le_min)
        print(f"Estimated latency limit: {Le=} ({le_min} - {le_max})")
        diff = (Le - Lc) / Lc * 100
        print(f"Difference: {diff:.2f} % "
              f"({(le_min - lc_min) / lc_min * 100:.2f} % -- {(le_max - lc_max) / lc_max * 100:.2f} %)")
        print('#' * 80)
        diffs.append(diff)
    print(f">>> Avg. diff: {sum(diffs) / len(diffs):.2f} %")


if __name__ == '__main__':
    compare_latency_limit_estimation(test_file="data/rand_tree_n10.npy")
