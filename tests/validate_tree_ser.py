#!/usr/bin/env python3
# Copyright 2025 Janos Czentye
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
import itertools
import math
import operator
import pathlib
import random
import time

import networkx as nx
import pandas as pd
import tabulate
from docplex.cp.utils import CpoException
from docplex.mp.utils import DOcplexException
from pulp import PulpSolverError

from slambuc.alg.app import *
from slambuc.alg.tree.serial import *
from slambuc.alg.tree.serial.ilp_cplex import tree_cplex_partitioning, tree_cpo_partitioning
from slambuc.alg.util import ibacktrack_chain, ser_subchain_latency
from slambuc.misc.random import get_random_tree

TREE_ALGS = dict(
    GREEDY=greedy_ser_tree_partitioning,
    GREEDY_ILP=all_tree_mtx_partitioning,
    ILP_GREEDY_CFG=tree_cfg_partitioning,
    ILP_HYBRID_CFG=tree_hybrid_partitioning,
    ILP_MTX=tree_mtx_partitioning,
    ILP_CPLEX=tree_cplex_partitioning,
    CPO_CFG=tree_cpo_partitioning,
    PSEUDO_B=pseudo_btree_partitioning,
    PSEUDO_B_MP=pseudo_mp_btree_partitioning,
    PSEUDO_L=pseudo_ltree_partitioning,
    PSEUDO_L_MP=pseudo_mp_ltree_partitioning,
    BIHEUR_B=biheuristic_tree_partitioning,
    BIFPTAS_L=bifptas_tree_partitioning,
    BIFPTAS_L_DUAL=bifptas_dual_tree_partitioning
)


def run_all_tree_ser_tests(params: dict) -> list:
    stats = []
    for name, tree_alg in TREE_ALGS.items():
        print(f"Executing {name}")
        t_start = time.perf_counter()
        try:
            result = tree_alg(**params)
        except (PulpSolverError, DOcplexException, CpoException) as e:
            print(f"Pulp solver failed for {name} with message: {e}")
            stats.append([name, [], None, None, None])
            continue
        alg_time = time.perf_counter() - t_start
        if name.startswith('GREEDY'):
            stats.extend([[name + f'_{i}', *res, round(alg_time, ndigits=8)] for i, res in enumerate(result)])
        else:
            stats.append([name, *result, round(alg_time, ndigits=8)])
    return stats


def compare_results(tree_path: str = None, L: int = math.inf):
    tree = nx.read_gml(
        tree_path if tree_path is not None else pathlib.Path(__file__).parent / "data/graph_test_tree_ser.gml",
        destringizer=int)
    tree.graph[NAME] += "-serial"
    params = dict(tree=tree, root=1, cp_end=10, M=6, L=L, delay=10)
    ##########################################################
    cpath = list(reversed(list(ibacktrack_chain(tree, 1, params['cp_end']))))
    print("Runtime:", [tree.nodes[v][RUNTIME] for v in tree.nodes if v is not PLATFORM])
    print("Memory:", [tree.nodes[v][MEMORY] for v in tree.nodes if v is not PLATFORM])
    print("Rate:", [tree[next(tree.predecessors(v))][v][RATE] for v in tree.nodes if v is not PLATFORM])
    print("Data:", [tree[next(tree.predecessors(v))][v][DATA] for v in tree.nodes if v is not PLATFORM])
    print(f"Tree partitioning [M={params['M']}, L={params['L']}:{(1, params['cp_end'])}] -> cpath:{cpath}")
    print("Params:", repr(params))
    print('#' * 80)
    ##########################################################
    stats = run_all_tree_ser_tests(params)
    print('#' * 80)
    print("Summary:")
    print(tabulate.tabulate(stats, ['Alg.', 'Partition', 'Cost', 'Latency', 'Time (s)'],
                            colalign=('left', 'left', 'decimal', 'decimal', 'decimal'), tablefmt='pretty'))


def test_latencies():
    tree = nx.read_gml(pathlib.Path(__file__).parent / "data/graph_test_tree_ser.gml", destringizer=int)
    tree.graph[NAME] += "-serial"
    params = dict(tree=tree, root=1, cp_end=10, M=6, L=math.inf, delay=10)
    lats = [math.inf,
            # Optimal multi-solutions
            474, 471, 443,
            # Optimal solution
            440,
            # Forces to reduce blocks
            430,
            # Stricter latency
            410,
            # Infeasible latency
            400]
    print(tree.graph.get(NAME, "tree").center(80, '#'))
    print("Runtime:", [tree.nodes[v][RUNTIME] for v in tree.nodes if v is not PLATFORM])
    print("Memory:", [tree.nodes[v][MEMORY] for v in tree.nodes if v is not PLATFORM])
    print("Rate:", [tree[next(tree.predecessors(v))][v][RATE] for v in tree.nodes if v is not PLATFORM])
    for lat in lats:
        params['L'] = lat
        print("Params:", repr(params))
        stat = run_all_tree_ser_tests(params)
        print(tabulate.tabulate(stat, ['Alg.', 'Partition', 'Cost', 'Latency', 'Time (s)'],
                                numalign='center', stralign='left', tablefmt='pretty'))
        print('#' * 80)


def test_random_validation(n: int = 10, cache_failed: bool = False, stop_failed: bool = False) -> tuple[str, list]:
    tree = get_random_tree(n)
    # noinspection PyUnresolvedReferences
    tree.graph[NAME] += "-serial"
    cp_end = n
    cpath = list(reversed(list(ibacktrack_chain(tree, 1, cp_end))))
    singleton_lat = ser_subchain_latency(tree, 1, set(range(1, n + 1)), set(cpath))
    rand_factor = 1 - 1 / random.randint(2, len(cpath))
    params = dict(tree=tree, M=6, root=1, cp_end=cp_end, delay=10, L=int(rand_factor * singleton_lat))
    # noinspection PyUnresolvedReferences
    print(tree.graph.get(NAME, "tree").center(80, '#'))
    print("Runtime:", [tree.nodes[v][RUNTIME] for v in tree.nodes if v is not PLATFORM])
    print("Memory:", [tree.nodes[v][MEMORY] for v in tree.nodes if v is not PLATFORM])
    print("Rate:", [tree[next(tree.predecessors(v))][v][RATE] for v in tree.nodes if v is not PLATFORM])
    print("Data:", [tree[next(tree.predecessors(v))][v][DATA] for v in tree.nodes if v is not PLATFORM])
    print(f"Tree partitioning [M={params['M']}, L={params['L']}:{(1, cp_end)}] -> cpath:{cpath}")
    print("Params:", repr(params))
    stat = run_all_tree_ser_tests(params)
    print(tabulate.tabulate(stat, ['Alg.', 'Partition', 'Cost', 'Latency', 'Time'],
                            stralign='decimal', tablefmt='pretty'))
    print('#' * 80)
    alg_num = len(TREE_ALGS) - 1
    p_grdy, p_algs = [p[1] for p in stat[:-alg_num]], list(map(operator.itemgetter(1), stat[-alg_num:]))
    c_grdy, c_algs = stat[0][2], list(map(operator.itemgetter(2), stat[-alg_num:]))
    l_grdy, l_algs = [p[3] for p in stat[:-alg_num]], list(map(operator.itemgetter(3), stat[-alg_num:]))
    validated = all((all(p in p_grdy for p in p_algs),
                     all(c_grdy == c for c in c_algs) if all((c_grdy, *c_algs)) else True,
                     all(l in l_grdy for l in l_algs)))
    if not validated and cache_failed:
        # noinspection PyUnresolvedReferences
        tree.graph[NAME] = f"failed_{tree.graph[NAME]}_L{params['L']}_M{params['M']}.gml"
        # noinspection PyUnresolvedReferences
        nx.write_gml(tree, tree.graph[NAME], stringizer=str)
    result = 'SUCCESS' if validated else 'FAILED'
    print(f"Validation: {result}")
    if stop_failed:
        assert result == 'SUCCESS'
    print('#' * 80)
    return result, stat


def stress_test(n: int = 10, iteration: int = 100, cache_failed: bool = True, stop_failed: bool = False):
    results = [test_random_validation(n, cache_failed=cache_failed, stop_failed=stop_failed) for _ in range(iteration)]
    valid, stats = zip(*results)
    print("Validation statistics:", collections.Counter(valid))
    df = pd.DataFrame(itertools.chain(*stats))
    pd.set_option('display.expand_frame_repr', False)
    grouped_stat = df[(df[2] < math.inf) & (df[0].isin(('GREEDY_0', *TREE_ALGS)))][[0, 4]].groupby(0)
    print("Runtime statistics:")
    print(grouped_stat.describe().reset_index().sort_values((4, 'mean'), ascending=False))


if __name__ == '__main__':
    compare_results()
    # test_latencies()
    # test_random_validation()
    # compare_results(pathlib.Path(__file__).parent / "data/graph_test_tree_ser_latency1.gml", L=520)
    # compare_results(pathlib.Path(__file__).parent / "data/graph_test_tree_ser_latency2.gml", L=255)
    # compare_results("failed_random_tree_1675283922.1326418-ser_partition_L521_M6.gml", L=521)
    # stress_test(n=15, iteration=100, stop_failed=True)
