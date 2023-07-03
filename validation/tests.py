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
import functools
import itertools
import logging
import pathlib

import cspy
import numpy as np
import pulp

from generate_test_data import PERF_TEST_DATA_PARAMS, PERF_TREE_SIZE_RANGE, DATA_DIR
from harness import execute_tests, log
from slambuc.alg.ext import *
from slambuc.alg.tree import *
from slambuc.alg.tree.dp.seq_state import cacheless_chain_partitioning, stateful_chain_partitioning
from slambuc.gen import DEF_FAAS_TREE_PREFIX, DEF_RAND_TREE_PREFIX, DEF_JOB_TREE_PREFIX
from slambuc.misc.util import get_cplex_path

# Common parameters for tests
CPLEX_PATH = get_cplex_path()
# cpu
DEF_CPU_NUM = 1
MAX_CPU_NUM = 4
DEF_PAR_CPU_NUM = 2
# tree
TREE_TYPES = (DEF_JOB_TREE_PREFIX, DEF_RAND_TREE_PREFIX, DEF_FAAS_TREE_PREFIX)
DEF_TREE_SIZE = 40
# algs
DEF_MEM_COEFF = 0.2
DEF_LAT_COEFF = 0.2
COEFF_RANGE = np.linspace(0.0, 1.0, 11)  # [0.0, 0.1, ..., 0.9, 1.0]
DEF_EPS = 0.5
DEF_LAMBDA = 0.5
DEF_TIMEOUT = 1000  # ~ 17 min
# Setup logging
DEF_LOG_LEVEL = logging.DEBUG
logging.getLogger().setLevel(DEF_LOG_LEVEL)

########################################################################################################################


# Algorithms under test with serialized execution
TREE_SER_ALGS = dict(
    ILP_HYBRID=functools.partial(tree_hybrid_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    ILP_MTX=functools.partial(tree_mtx_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    PSEUDO_B=functools.partial(pseudo_btree_partitioning, bidirectional=False),
    PSEUDO_B_BI=pseudo_btree_partitioning,
    PSEUDO_B_MP=functools.partial(pseudo_mp_btree_partitioning, bidirectional=False),
    PSEUDO_L=functools.partial(pseudo_ltree_partitioning, bidirectional=False),
    PSEUDO_L_BI=pseudo_ltree_partitioning,
    PSEUDO_L_MP=functools.partial(pseudo_mp_ltree_partitioning, bidirectional=False),
    BIFPTAS_L=functools.partial(bifptas_tree_partitioning, Epsilon=DEF_EPS, Lambda=DEF_LAMBDA),
    GREEDY=min_weight_partition_heuristic
)

# Algorithms under test with parallelized execution
TREE_PAR_ALGS = dict(
    ILP_HYBRID_PAR=functools.partial(tree_par_hybrid_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    ILP_MTX_PAR=functools.partial(tree_par_mtx_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    PSEUDO_L_PAR=functools.partial(pseudo_par_ltree_partitioning, bidirectional=False),
    PSEUDO_L_PAR_BI=pseudo_par_ltree_partitioning,
    PSEUDO_L_PAR_MP=functools.partial(pseudo_par_mp_ltree_partitioning, bidirectional=False),
    GREEDY=min_weight_partition_heuristic
)


def perform_tree_size_ser_tests(n: int = None, data_dir: str = DATA_DIR, output_prefix: str = "test_tree_size_ser",
                                tree_num: int = None, timeout: int = DEF_TIMEOUT):
    print(" Tree size ser. tests ".center(80, '#'))
    size_range = range(*PERF_TREE_SIZE_RANGE) if n is None else range(n, n + 1)
    for n in size_range:
        log.info(f"Test tree size: {n}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}.csv"
        execute_tests(TREE_SER_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                      N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


def perform_tree_size_par_tests(n: int = None, data_dir: str = DATA_DIR, output_prefix: str = "test_tree_size_par",
                                n_cpu: int = DEF_PAR_CPU_NUM, tree_num: int = None, timeout: int = DEF_TIMEOUT):
    log.info(" Tree size par. tests ".center(80, '#'))
    size_range = range(*PERF_TREE_SIZE_RANGE) if n is None else range(n, n + 1)
    for n in size_range:
        log.info(f"Test tree size: {n}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}.csv"
        execute_tests(TREE_PAR_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF, N=n_cpu,
                      output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


########################################################################################################################


# Algorithms under test with parameters M and L
TREE_SENS_ALGS = dict(
    ILP_HYBRID=functools.partial(tree_hybrid_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    ILP_MTX=functools.partial(tree_mtx_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    PSEUDO_B=pseudo_btree_partitioning,
    PSEUDO_L=pseudo_ltree_partitioning,
    GREEDY=min_weight_partition_heuristic,
    BIFPTAS=functools.partial(bifptas_tree_partitioning, Epsilon=DEF_EPS, Lambda=DEF_LAMBDA),
)

# Algorithms under test with parallelized execution
TREE_SENSE_PAR_ALGS = dict(
    ILP_HYBRID_PAR=functools.partial(tree_par_hybrid_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    ILP_MTX_PAR=functools.partial(tree_par_mtx_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False)),
    PSEUDO_L_PAR=pseudo_par_ltree_partitioning,
    GREEDY=min_weight_partition_heuristic,
    BIFPTAS=functools.partial(bifptas_tree_partitioning, Epsilon=DEF_EPS, Lambda=DEF_LAMBDA),
)

# Algorithms under test with parameters Epsilon and Lambda
APPROX_SENS_ALGS = dict(
    BIFPTAS=bifptas_tree_partitioning
)


def perform_mem_sens_tests(n: int = DEF_TREE_SIZE, data_dir: str = DATA_DIR, output_prefix: str = "test_alg_sens",
                           tree_num: int = None, value: str = None, timeout: int = DEF_TIMEOUT):
    log.info(" M-sensitivity tests ".center(80, '#'))
    if value:
        v, *_ = value
        log.info(f"Test algs with memory coeff: {v}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}_m{round(v, 1):.1f}.csv"
        execute_tests(TREE_SENS_ALGS, test_file=test_file, mem_coeff=v, lat_coeff=DEF_LAT_COEFF, N=DEF_CPU_NUM,
                      output_file=output_file, tree_num=tree_num, timeout=timeout)
    else:
        for m in COEFF_RANGE:
            log.info(f"Test algs with memory coeff: {m}")
            test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
            output_file = output_prefix + f"_n{n}_m{round(m, 1):.1f}.csv"
            execute_tests(TREE_SENS_ALGS, test_file=test_file, mem_coeff=m, lat_coeff=DEF_LAT_COEFF, N=DEF_CPU_NUM,
                          output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


def perform_lat_sens_tests(n: int = DEF_TREE_SIZE, data_dir: str = DATA_DIR, output_prefix: str = "test_alg_sens",
                           tree_num: int = None, value: str = None, timeout: int = DEF_TIMEOUT):
    log.info(" L-sensitivity tests ".center(80, '#'))
    if value:
        v, *_ = value
        log.info(f"Test algs with latency coeff: {v}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}_l{round(v, 1):.1f}.csv"
        execute_tests(TREE_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=v, N=DEF_CPU_NUM,
                      output_file=output_file, tree_num=tree_num, timeout=timeout)
    else:
        for l in COEFF_RANGE:
            log.info(f"Test algs with latency coeff: {l}")
            test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
            output_file = output_prefix + f"_n{n}_l{round(l, 1):.1f}.csv"
            execute_tests(TREE_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=l, N=DEF_CPU_NUM,
                          output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


def perform_cpu_sens_tests(n: int = DEF_TREE_SIZE, data_dir: str = DATA_DIR, output_prefix: str = "test_alg_sens",
                           tree_num: int = None, value: str = None, timeout: int = DEF_TIMEOUT):
    log.info(" CPU-sensitivity tests ".center(80, '#'))
    if value:
        v, *_ = value
        log.info(f"Test algs with CPU core num: {v}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}_cpu{round(v, 1):.1f}.csv"
        execute_tests(TREE_SENSE_PAR_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                      N=v, output_file=output_file, tree_num=tree_num, timeout=timeout)
    else:
        for cpu in range(DEF_CPU_NUM, MAX_CPU_NUM + 1):
            log.info(f"Test algs with CPU core num: {cpu}")
            test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
            output_file = output_prefix + f"_n{n}_cpu{round(cpu, 1):.1f}.csv"
            execute_tests(TREE_SENSE_PAR_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                          N=cpu, output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


def perform_epsilon_sens_tests(n: int = DEF_TREE_SIZE, data_dir: str = DATA_DIR, output_prefix: str = "test_alg_sens",
                               tree_num: int = None, value: str = None, timeout: int = DEF_TIMEOUT):
    log.info(" Epsilon-sensitivity tests ".center(80, '#'))
    if value:
        v, *_ = value
        log.info(f"Test algs with epsilon coeff: {v}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}_eps{round(v, 1):.1f}.csv"
        execute_tests(APPROX_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                      N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout, Epsilon=v)
    else:
        for e in COEFF_RANGE:
            log.info(f"Test algs with epsilon coeff: {e}")
            test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
            output_file = output_prefix + f"_n{n}_eps{round(e, 1):.1f}.csv"
            execute_tests(APPROX_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                          N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout, Epsilon=e)
    log.info("Finished")


def perform_lambda_sens_tests(n: int = DEF_TREE_SIZE, data_dir: str = DATA_DIR, output_prefix: str = "test_alg_sens",
                              tree_num: int = None, value: str = None, timeout: int = DEF_TIMEOUT):
    log.info(" Lambda-sensitivity tests ".center(80, '#'))
    if value:
        v, *_ = value
        log.info(f"Test algs with lambda coeff: {v}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}_lam{round(v, 1):.1f}.csv"
        execute_tests(APPROX_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                      N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout, Lambda=v)
    else:
        for l in COEFF_RANGE:
            log.info(f"Test algs with lambda coeff: {l}")
            test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
            output_file = output_prefix + f"_n{n}_lam{round(l, 1):.1f}.csv"
            execute_tests(APPROX_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                          N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout, Lambda=l)
    log.info("Finished")


def perform_bicriteria_sens_tests(n: int = DEF_TREE_SIZE, data_dir: str = DATA_DIR,
                                  output_prefix: str = "test_alg_sens", tree_num: int = None,
                                  value: str = None, timeout: int = DEF_TIMEOUT):
    log.info(" (Epsilon, Lambda)-sensitivity tests ".center(80, '#'))
    if value:
        v_e, v_l = value
        log.info(f"Test algs with E-L coeffs: {value}")
        test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
        output_file = output_prefix + f"_n{n}_bicrit_{round(v_e, 1):.1f}-{round(v_l, 1):.1f}.csv"
        execute_tests(APPROX_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                      N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout, Epsilon=v_e,
                      Lambda=v_l)
    else:
        for e, l in itertools.product(COEFF_RANGE, COEFF_RANGE):
            log.info(f"Test algs with E-L coeffs: {(e, l)}")
            test_file = pathlib.Path(data_dir, PERF_TEST_DATA_PARAMS['file_prefix'] + f"_n{n}.npy").resolve()
            output_file = output_prefix + f"_n{n}_bicrit_{round(e, 1):.1f}-{round(l, 1):.1f}.csv"
            execute_tests(APPROX_SENS_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                          N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout, Epsilon=e,
                          Lambda=l)
    log.info("Finished")


########################################################################################################################


# Algorithms under test with serialized execution
TREE_COST_SER_ALGS = dict(
    # Baselines - infeasible
    BASELINE_NO_PART=baseline_no_partitioning,
    BASELINE_SINGLE=baseline_singleton_partitioning,
    # Baseline1 - chains, poly, maybe infeasible
    MINW_CHAIN=min_weight_chain_decomposition,
    # Baseline - subtrees, poly, k-block, maybe infeasible
    K_SPLIT=min_weight_ksplit_clustering,
    # Baseline - subtrees, poly, all k-block, maybe infeasible
    K_SPLIT_EXH=min_weight_tree_clustering,
    # SOTA - chains, poly, no data caching
    CHAIN_PART=cacheless_chain_partitioning,
    # SOTA - chains, poly, integrated data caching
    CHAIN_PART_SER=stateful_chain_partitioning,
    # SOTA - chains, heuristic(poly), with data caching
    COSTLESS=functools.partial(csp_tree_partitioning, solver=cspy.BiDirectional),
    # OUR - subtrees, poly-heur, feasible/no solution
    GREEDY=min_weight_partition_heuristic,
    # OUR - subtrees, approx. (poly)
    BIFPTAS=functools.partial(bifptas_tree_partitioning, Epsilon=DEF_EPS, Lambda=DEF_LAMBDA),
    # Optimal - subtree, optimal
    OPT=functools.partial(tree_mtx_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False))
)

# Algorithms under test with parallelized execution
TREE_COST_PAR_ALGS = dict(
    # Baselines - infeasible
    BASELINE_NO_PART_PAR=baseline_no_partitioning,
    BASELINE_SINGLE_PAR=baseline_singleton_partitioning,
    # Baseline1 - chains, poly, maybe infeasible
    MINW_CHAIN_PAR=min_weight_chain_decomposition,
    # Baseline - subtrees, poly, k-block, maybe infeasible
    K_SPLIT_PAR=min_weight_ksplit_clustering,
    # Baseline - subtrees, poly, all k-block, maybe infeasible
    K_SPLIT_EXH_PAR=min_weight_tree_clustering,
    # SOTA - chains, poly, no data caching
    CHAIN_PART_PAR=cacheless_chain_partitioning,
    # SOTA - chains, poly, integrated data caching
    CHAIN_FULL_PAR=stateful_chain_partitioning,
    # SOTA - chains, heuristic(poly), with data caching
    COSTLESS_PAR=functools.partial(csp_tree_partitioning, solver=cspy.BiDirectional),
    # OUR - subtrees, poly-heur, feasible/no solution
    GREEDY_PAR=min_weight_partition_heuristic,
    # OUR - subtree, optimal, parallel
    PSEUDO_L_PAR=pseudo_par_ltree_partitioning,
    # Optimal - subtree, optimal
    OPT_PAR=functools.partial(tree_par_mtx_partitioning, solver=pulp.CPLEX_CMD(path=CPLEX_PATH, msg=False))
)


def perform_cost_ser_tests(tree_type: str = None, size_pattern: str | int = DEF_TREE_SIZE, data_dir: str = DATA_DIR,
                           output_prefix: str = "test_alg_cost", tree_num: int = None, timeout: int = DEF_TIMEOUT):
    log.info(" Cost calculation ser tests ".center(80, '#'))
    for trees in (TREE_TYPES if tree_type is None else (f"{tree_type}_tree",)):
        log.info(f"Test algs with tree type: {trees}")
        for test_file in sorted(pathlib.Path(data_dir).resolve().glob(trees + f"_n{size_pattern}-*.npy")):
            sizes = test_file.name.rsplit('_', 1)[1]
            output_file = pathlib.Path(data_dir, '_'.join((output_prefix,
                                                           trees,
                                                           sizes))).resolve().with_suffix('.csv')
            execute_tests(TREE_COST_SER_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                          N=DEF_CPU_NUM, output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


def perform_cost_par_tests(tree_type: str = None, size_pattern: str | int = DEF_TREE_SIZE, n_cpu: int = DEF_PAR_CPU_NUM,
                           data_dir: str = DATA_DIR, output_prefix: str = "test_alg_cost", tree_num: int = None,
                           timeout: int = DEF_TIMEOUT):
    log.info(" Cost calculation par tests ".center(80, '#'))
    for trees in (TREE_TYPES if tree_type is None else (f"{tree_type}_tree",)):
        log.info(f"Test algs with tree type: {trees}")
        for test_file in sorted(pathlib.Path(data_dir).resolve().glob(trees + f"_n{size_pattern}-*.npy")):
            sizes = test_file.name.rsplit('_', 1)[1]
            output_file = pathlib.Path(data_dir, '_'.join((output_prefix,
                                                           trees,
                                                           sizes))).resolve().with_suffix('.csv')
            execute_tests(TREE_COST_PAR_ALGS, test_file=test_file, mem_coeff=DEF_MEM_COEFF, lat_coeff=DEF_LAT_COEFF,
                          N=n_cpu, output_file=output_file, tree_num=tree_num, timeout=timeout)
    log.info("Finished")


if __name__ == '__main__':
    # perform_tree_size_ser_tests(n=20, tree_num=13, timeout=10)
    # perform_tree_size_par_tests(n=20, tree_num=13, timeout=10)
    #
    # perform_mem_sens_tests(n=20, tree_num=13, value=(0.5,), timeout=10)
    # perform_lat_sens_tests(n=20, tree_num=13, value=(0.5,), timeout=10)
    # perform_cpu_sens_tests(n=20, tree_num=13, value=(0.5,), timeout=10)
    # perform_epsilon_sens_tests(n=20, tree_num=13, value=(0.5,), timeout=10)
    # perform_lambda_sens_tests(n=20, tree_num=13, value=(0.5,), timeout=10)
    # perform_bicriteria_sens_tests(n=20, tree_num=13, value=(0.5, 0.5), timeout=10)
    #
    # perform_cost_ser_tests(size_pattern=20, tree_type="faas", output_prefix="test", tree_num=13, timeout=100)
    perform_cost_par_tests(size_pattern=20, tree_type="faas", output_prefix="test", tree_num=13, timeout=10)
