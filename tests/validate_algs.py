#!/usr/bin/env python3
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
import math
import pathlib
import time
from collections.abc import Callable

import networkx as nx
import tabulate

from slambuc.alg.app import RUNTIME, MEMORY, RATE, DATA, Flavor
from slambuc.alg.chain import *
from slambuc.alg.dag import *
from slambuc.alg.dag.ilp import greedy_dag_partitioning
from slambuc.alg.ext import *
from slambuc.alg.tree import *
from slambuc.alg.tree.parallel.pseudo import pseudo_par_btree_partitioning
from slambuc.alg.tree.path.seq_state import cacheless_path_tree_partitioning, stateful_path_tree_partitioning
from slambuc.alg.util import ibacktrack_chain, split_chain
from slambuc.misc.util import get_cplex_path

CPLEX_PATH = get_cplex_path()


def on_critical_path(alg: Callable, with_cpu: bool = True, with_data: bool = True, extract: bool = True):
    @functools.wraps(alg)
    def input_wrapper(tree: nx.DiGraph, root: int = 1, cp_end: int = None, **kwargs):
        chain = list(reversed(list(ibacktrack_chain(tree, start=root, leaf=cp_end))))
        runtime, memory, rate, data = zip(*((tree.nodes[n][RUNTIME], tree.nodes[n][MEMORY],
                                             tree[next(tree.predecessors(n))][n][RATE],
                                             tree[next(tree.predecessors(n))][n][DATA]) for n in chain))
        params = dict(runtime=runtime, memory=memory, rate=rate, M=kwargs.get('M', math.inf),
                      L=kwargs.get('L', math.inf), start=0, end=len(runtime) - 1, delay=kwargs.get('delay', 1))
        if with_data:
            params.update(data=data)
        if with_cpu:
            params.update(N=kwargs.get('N', math.inf))
        res = alg(**params)
        return (split_chain(res[0], len(chain)), *res[1:]) if extract else res

    return input_wrapper


def with_single_flavor(alg: Callable):
    @functools.wraps(alg)
    def input_wrapper(M: int = math.inf, N: int = 1, **kwargs):
        return alg(flavors=[Flavor(mem=M, ncore=N)], **kwargs)

    return input_wrapper


def with_tree(alg: Callable):
    @functools.wraps(alg)
    def input_wrapper(tree: nx.DiGraph, **kwargs):
        return alg(dag=tree, **kwargs)

    return input_wrapper


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
    # Chain-based partitioning
    GREEDY_CHAIN_PART=greedy_tree_partitioning,
    CHAIN_META_PART=meta_tree_partitioning,
    CHAIN_MIN_PART=min_tree_partitioning,
    CHAIN_SEQ_PART=seq_tree_partitioning,
    CHAIN_PART=cacheless_path_tree_partitioning,
    CHAIN_PART_SER=stateful_path_tree_partitioning,
    # General partitioning with flavors
    GREEDY_GEN_ILP=with_single_flavor(all_gen_tree_mtx_partitioning),
    GEN_ILP_CFG=with_single_flavor(tree_gen_hybrid_partitioning),
    GEN_ILP_MTX=with_single_flavor(tree_gen_mtx_partitioning),
    # Baselines
    BASELINE_NO_PART=baseline_no_partitioning,
    BASELINE_SINGLE=baseline_singleton_partitioning,
    # Critical path chain
    GREEDY_CPATH_CHAIN=on_critical_path(greedy_chain_partitioning, with_data=False, extract=False),
    CPATH_CHAIN_MIN=on_critical_path(min_chain_partitioning, with_data=False),
    CPATH_CHAIN=on_critical_path(chain_partitioning, with_data=False),
    CPATH_CHAIN_VEC=on_critical_path(vec_chain_partitioning, with_data=False),
    CPATH_SP_CHAIN=on_critical_path(sp_chain_partitioning, with_cpu=False),
    GREEDY_CPATH_SER_CHAIN=on_critical_path(greedy_ser_chain_partitioning, with_cpu=False, extract=False),
    CPATH_SER_CFG_ILP=on_critical_path(chain_cfg_partitioning, with_cpu=False, extract=False),
    CPATH_SER_MTX_ILP=on_critical_path(chain_mtx_partitioning, with_cpu=False, extract=False),
    # DAG partitioning
    DAG_ILP_MTX=with_tree(dag_partitioning),
    DAG_GREEDY_ILP_MTX=with_tree(greedy_dag_partitioning)
)


def compare_results(tree_path: str = None, L: int = math.inf):
    tree = nx.read_gml(tree_path if tree_path is not None else
                       pathlib.Path(__file__).parent / pathlib.Path(__file__).parent / "data/graph_test_tree_ser.gml",
                       destringizer=int)
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
    exit(0)
