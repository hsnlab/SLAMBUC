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

import networkx as nx

from slambuc.alg import INFEASIBLE, T_RESULTS
from slambuc.alg.tree import seq_tree_partitioning
from slambuc.alg.util import recalculate_partitioning
from slambuc.generator.transform import transform_autonomous_caching


def cacheless_path_tree_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, N: int = 1, L: int = math.inf,
                                     cp_end: int = None, delay: int = 1, valid: bool = True) -> T_RESULTS:
    """
    Calculates minimal-cost partitioning using *seq_tree_partitioning* without considering data externalization.

    :param tree:    app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:    root node of the graph
    :param M:       upper memory bound of the partition blocks (in MB)
    :param N:       upper CPU core bound of the partition blocks
    :param L:       latency limit defined on the critical path (in ms)
    :param cp_end:  tail node of the critical path in the form of subchain[root -> cp_end]
    :param delay:   invocation delay between blocks
    :param valid:   return only L-feasible solutions
    :return:        tuple of optimal partition, sum cost of the partitioning, and optimal number of cuts
    """
    partition, *_ = seq_tree_partitioning(tree, root, M, N, L, cp_end, delay, unit=1)
    if not partition:
        return INFEASIBLE
    sum_cost, sum_lat = recalculate_partitioning(tree, partition, root, N, cp_end, delay)
    return INFEASIBLE if valid and sum_lat > L else (partition, sum_cost, sum_lat)


def stateful_path_tree_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, N: int = 1, L: int = math.inf,
                                    cp_end: int = None, delay: int = 1) -> T_RESULTS:
    """
    Calculates minimal-cost partitioning using *seq_tree_partitioning* while considering data implicit state
    externalization.

    Input tree is preprocessed and function runtimes are altered to incorporate data read/write overheads.

    :param tree:    app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:    root node of the graph
    :param M:       upper memory bound of the partition blocks (in MB)
    :param N:       upper CPU core bound of the partition blocks
    :param L:       latency limit defined on the critical path (in ms)
    :param cp_end:  tail node of the critical path in the form of subchain[root -> cp_end]
    :param delay:   invocation delay between blocks
    :return:        tuple of optimal partition, sum cost of the partitioning, and optimal number of cuts
    """
    partition, *_ = seq_tree_partitioning(transform_autonomous_caching(tree, root, copy=True),
                                          root, M, N, L, cp_end, delay, unit=1)
    return (partition, *recalculate_partitioning(tree, partition, root, N, cp_end, delay)) if partition else INFEASIBLE
