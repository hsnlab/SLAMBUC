#!/usr/bin/env python3.11
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
import math
import pathlib
import time

import networkx as nx
import tabulate

from slambuc.alg.ext import *
from slambuc.alg.tree.par import *
from slambuc.alg.tree.par.pseudo import pseudo_par_btree_partitioning
from slambuc.alg.tree.ser import *
from slambuc.misc.util import get_cplex_path

CPLEX_PATH = get_cplex_path()

TREE_ALGS = dict(
    # Greedy
    GREEDY=greedy_ser_tree_partitioning,
    GREEDY_ILP=all_tree_mtx_partitioning,
    GREEDY_PAR=greedy_par_tree_partitioning,
    GREEDY_ILP_PAR=all_par_tree_mtx_partitioning,
    # Configuration ILP
    ILP_CFG_HYBRID=tree_hybrid_partitioning,
    ILP_CFG_GREEDY=tree_cfg_partitioning,
    ILP_CFG_HYBRID_PAR=tree_par_hybrid_partitioning,
    ILP_CFG_GREEDY_PAR=tree_par_cfg_partitioning,
    ILP_HYBRID_CPLEX_CMD=tree_hybrid_partitioning,
    # Matrix model ILP
    ILP_MTX=tree_mtx_partitioning,
    ILP_MTX_PAR=tree_par_mtx_partitioning,
    # Pseudo B-tree
    PSEUDO_B=pseudo_btree_partitioning,
    PSEUDO_B_MP=pseudo_mp_btree_partitioning,
    PSEUDO_B_PAR=pseudo_par_btree_partitioning,
    # Pseudo L-tree
    PSEUDO_L=pseudo_ltree_partitioning,
    PSEUDO_L_MP=pseudo_mp_ltree_partitioning,
    PSEUDO_L_PAR=pseudo_par_ltree_partitioning,
    PSEUDO_L_PAR_MP=pseudo_par_mp_ltree_partitioning,
    # Bi-criteria FPTAS
    BIHEUR_B=biheuristic_tree_partitioning,
    BIFPTAS_L=bifptas_tree_partitioning,
    BIFPTAS_L_DUAL=bifptas_dual_tree_partitioning,
    # Heuristics
    CHAIN_DECOMP=min_weight_chain_decomposition,
    TREE_CLUSTER=min_weight_ksplit_clustering,
    MINW_UNBOUDED=min_weight_greedy_partitioning,
    MINW_HEUR=min_weight_partition_heuristic,
    CSP=csp_tree_partitioning,
    # Baselines
    BASELINE_NO_PART=baseline_no_partitioning,
    BASELINE_SINGLE=baseline_singleton_partitioning
)


def compare_results(tree_path: str = None, L: int = math.inf):
    tree = nx.read_gml(tree_path if tree_path is not None else
                       pathlib.Path(__file__).parent / "data/graph_test_tree_ser.gml", destringizer=int)
    params = dict(tree=tree, root=1, cp_end=10, M=6, L=L, delay=10)
    ##########################################################
    print('#' * 80)
    stats = []
    for name, tree_alg in TREE_ALGS.items():
        print(f"Executing {name}")
        t_start = time.perf_counter()
        result = tree_alg(**params)
        alg_time = time.perf_counter() - t_start
        if name.startswith('GREEDY'):
            stats.extend([[name + f'_{i}', *res, round(alg_time, ndigits=8)] for i, res in enumerate(result)])
        else:
            stats.append([name, *result, round(alg_time, ndigits=8)])
    print('#' * 80)
    print("Summary:")
    print(tabulate.tabulate(stats, ['Algorithm', 'Partitioning', 'Cost', 'Latency', 'Time (s)'],
                            colalign=('left', 'left', 'center', 'center', 'decimal'), tablefmt='github'))


if __name__ == '__main__':
    compare_results()
