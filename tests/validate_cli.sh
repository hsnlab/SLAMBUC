#!/usr/bin/env sh
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
set -ex

slambuc chain path dp ./data/chain_test_sequence_serial.npz --alg chain
slambuc chain path dp ./data/chain_test_sequence_serial.npz --alg vector

slambuc chain path greedy ./data/chain_test_sequence_serial.npz

slambuc chain path min ./data/chain_test_sequence_serial.npz

slambuc chain path sp ./data/chain_test_sequence_serial.npz

slambuc chain serial greedy ./data/chain_test_sequence_serial.npy

slambuc chain serial ilp ./data/chain_test_sequence_serial.npy --alg cfg
slambuc chain serial ilp ./data/chain_test_sequence_serial.npy --alg mtx

slambuc dag ilp ./data/graph_test_dag.gml --alg greedy
slambuc dag ilp ./data/graph_test_dag.gml --alg dag

slambuc ext baseline ./data/graph_test_tree.gml --alg singleton
slambuc ext baseline ./data/graph_test_tree.gml --alg no

slambuc ext csp ./data/graph_test_tree.gml --alg csp
slambuc ext csp ./data/graph_test_tree.gml --alg gen

slambuc ext greedy ./data/graph_test_tree.gml --alg greedy
slambuc ext greedy ./data/graph_test_tree.gml --alg weight
slambuc ext greedy ./data/graph_test_tree.gml --alg lat

slambuc ext mincut ./data/graph_test_tree.gml --alg chain
slambuc ext mincut ./data/graph_test_tree.gml --alg ksplit
slambuc ext mincut ./data/graph_test_tree.gml --alg tree

slambuc tree layout ilp ./data/graph_test_tree.gml --alg hybrid
slambuc tree layout ilp ./data/graph_test_tree.gml --alg mtx
slambuc tree layout ilp ./data/graph_test_tree.gml --alg all

slambuc tree parallel greedy ./data/graph_test_tree_par.gml --alg greedy

slambuc tree parallel ilp ./data/graph_test_tree_par.gml --alg cfg
slambuc tree parallel ilp ./data/graph_test_tree_par.gml --alg hybrid
slambuc tree parallel ilp ./data/graph_test_tree_par.gml --alg mtx
slambuc tree parallel ilp ./data/graph_test_tree_par.gml --alg all

slambuc tree parallel pseudo ./data/graph_test_tree_par.gml --alg btree
slambuc tree parallel pseudo ./data/graph_test_tree_par.gml --alg ltree

slambuc tree parallel pseudo_mp ./data/graph_test_tree_par.gml --alg ltree

slambuc tree path greedy ./data/graph_test_tree_ser.gml --alg greedy

slambuc tree path meta ./data/graph_test_tree_ser.gml --alg meta

slambuc tree path min ./data/graph_test_tree_ser.gml --alg min

slambuc tree path seq ./data/graph_test_tree_ser.gml --alg seq

slambuc tree path state ./data/graph_test_tree_ser.gml --alg cacheless
slambuc tree path state ./data/graph_test_tree_ser.gml --alg stateful

slambuc tree serial bicriteria ./data/graph_test_tree_ser.gml --alg biheuristic
slambuc tree serial bicriteria ./data/graph_test_tree_ser.gml --alg bifptas
slambuc tree serial bicriteria ./data/graph_test_tree_ser.gml --alg dual

slambuc tree serial greedy ./data/graph_test_tree_ser.gml --alg greedy

slambuc tree serial ilp ./data/graph_test_tree_ser.gml --alg cfg
slambuc tree serial ilp ./data/graph_test_tree_ser.gml --alg hybrid
slambuc tree serial ilp ./data/graph_test_tree_ser.gml --alg mtx
slambuc tree serial ilp ./data/graph_test_tree_ser.gml --alg all

slambuc tree serial pseudo ./data/graph_test_tree_ser.gml --alg btree
slambuc tree serial pseudo ./data/graph_test_tree_ser.gml --alg ltree

slambuc tree serial pseudo_mp ./data/graph_test_tree_ser.gml --alg btree
slambuc tree serial pseudo_mp ./data/graph_test_tree_ser.gml --alg ltree
