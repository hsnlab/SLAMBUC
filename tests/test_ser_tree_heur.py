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
import networkx as nx

from slambuc.alg.ext.greedy import (min_weight_greedy_partitioning, get_feasible_cpath_split,
                                    min_weight_partition_heuristic)
from slambuc.alg.util import ibacktrack_chain
from slambuc.misc.generator import get_random_tree
from slambuc.misc.util import evaluate_par_tree_partitioning


def test_min_weight_bounded_partitioning(root: int = 1, M: int = 11, L: int = 450, cp_end: int = 10, N: int = 1,
                                         delay: int = 10):
    tree = nx.read_gml("data/graph_test_tree.gml", destringizer=int)
    # tree = get_random_tree(10)
    partition, sum_cost, sum_lat = min_weight_greedy_partitioning(tree, root, M, N)
    evaluate_par_tree_partitioning(tree, partition, sum_cost, sum_lat, root, cp_end, M, L, N, delay=delay)


def test_min_weight_partition_heuristic(root: int = 1, M: int = 15, L: int = 475, cp_end: int = 10, N: int = 1,
                                        delay: int = 10):
    # tree = nx.read_gml("data/graph_test_tree.gml", destringizer=int)
    tree = get_random_tree(10)
    print("Cpath:", list(reversed(list(ibacktrack_chain(tree, root, cp_end)))))
    split = get_feasible_cpath_split(tree, root, cp_end, M, L, N, delay)
    print("Calculated split:", split)
    partition, sum_cost, sum_lat = min_weight_partition_heuristic(tree, root, M, L, N, cp_end, delay)
    evaluate_par_tree_partitioning(tree, partition, sum_cost, sum_lat, root, cp_end, M, L, N, delay=delay)


if __name__ == '__main__':
    test_min_weight_bounded_partitioning()
    test_min_weight_partition_heuristic()