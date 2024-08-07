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

import networkx as nx

from slambuc.alg.app import NAME
from slambuc.alg.tree.path.seq import seq_tree_partitioning
from slambuc.misc.random import get_random_tree
from slambuc.misc.util import evaluate_tree_partitioning


def run_test(tree: nx.DiGraph, M: int, N: int, L: int, root: int = 1, cp_end: int = None, delay: int = 10,
             unit: int = 100):
    partition, opt_cost, opt_cut = seq_tree_partitioning(tree, root, M, N, L, cp_end, delay, unit)
    evaluate_tree_partitioning(tree, partition, opt_cost, root, cp_end, M, N, L, delay, unit)
    return partition, opt_cost, opt_cut


def test_tree_partitioning():
    tree = nx.read_gml(pathlib.Path(__file__).parent / pathlib.Path(__file__).parent / "data/graph_test_tree.gml",
                       destringizer=int)
    tree.graph[NAME] += "-seq"
    params = dict(tree=tree,
                  root=1,
                  cp_end=10,
                  M=15,
                  N=2,
                  L=math.inf,
                  delay=10)
    run_test(**params)


def test_random_tree_partitioning(n: int = 10):
    tree = get_random_tree(n)
    tree.graph[NAME] += "-seq"
    params = dict(tree=tree,
                  root=1,
                  cp_end=n,
                  M=6,
                  N=2,
                  L=math.inf,
                  # L = 200,
                  delay=10)
    run_test(**params)


if __name__ == '__main__':
    test_tree_partitioning()
    test_random_tree_partitioning()
