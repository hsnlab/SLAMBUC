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

docker run --rm -ti czentye/slambuc:0.5.0 chain path dp tests/data/chain_test_sequence_serial.npz --alg chain
docker run --rm -ti czentye/slambuc:0.5.0 chain path dp tests/data/chain_test_sequence_serial.npz --alg vector

docker run --rm -ti czentye/slambuc:0.5.0 chain path greedy tests/data/chain_test_sequence_serial.npz

docker run --rm -ti czentye/slambuc:0.5.0 chain path min tests/data/chain_test_sequence_serial.npz

docker run --rm -ti czentye/slambuc:0.5.0 chain path sp tests/data/chain_test_sequence_serial.npz

docker run --rm -ti czentye/slambuc:0.5.0 chain serial greedy tests/data/chain_test_sequence_serial.npy

docker run --rm -ti czentye/slambuc:0.5.0 chain serial ilp tests/data/chain_test_sequence_serial.npy --alg cfg --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 chain serial ilp tests/data/chain_test_sequence_serial.npy --alg mtx --solver glpk

docker run --rm -ti czentye/slambuc:0.5.0 dag ilp tests/data/graph_test_dag.gml --alg greedy --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 dag ilp tests/data/graph_test_dag.gml --alg dag --solver glpk

docker run --rm -ti czentye/slambuc:0.5.0 ext baseline tests/data/graph_test_tree.gml --alg singleton
docker run --rm -ti czentye/slambuc:0.5.0 ext baseline tests/data/graph_test_tree.gml --alg no

docker run --rm -ti czentye/slambuc:0.5.0 ext csp tests/data/graph_test_tree.gml --alg csp
docker run --rm -ti czentye/slambuc:0.5.0 ext csp tests/data/graph_test_tree.gml --alg gen

docker run --rm -ti czentye/slambuc:0.5.0 ext greedy tests/data/graph_test_tree.gml --alg greedy
docker run --rm -ti czentye/slambuc:0.5.0 ext greedy tests/data/graph_test_tree.gml --alg weight
docker run --rm -ti czentye/slambuc:0.5.0 ext greedy tests/data/graph_test_tree.gml --alg lat

docker run --rm -ti czentye/slambuc:0.5.0 ext mincut tests/data/graph_test_tree.gml --alg chain
docker run --rm -ti czentye/slambuc:0.5.0 ext mincut tests/data/graph_test_tree.gml --alg ksplit
docker run --rm -ti czentye/slambuc:0.5.0 ext mincut tests/data/graph_test_tree.gml --alg tree

docker run --rm -ti czentye/slambuc:0.5.0 tree layout ilp tests/data/graph_test_tree.gml --alg hybrid --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree layout ilp tests/data/graph_test_tree.gml --alg mtx --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree layout ilp tests/data/graph_test_tree.gml --alg all --solver glpk

docker run --rm -ti czentye/slambuc:0.5.0 tree parallel greedy tests/data/graph_test_tree_par.gml --alg greedy

docker run --rm -ti czentye/slambuc:0.5.0 tree parallel ilp tests/data/graph_test_tree_par.gml --alg cfg --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree parallel ilp tests/data/graph_test_tree_par.gml --alg hybrid --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree parallel ilp tests/data/graph_test_tree_par.gml --alg mtx --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree parallel ilp tests/data/graph_test_tree_par.gml --alg all --solver glpk

docker run --rm -ti czentye/slambuc:0.5.0 tree parallel pseudo tests/data/graph_test_tree_par.gml --alg btree
docker run --rm -ti czentye/slambuc:0.5.0 tree parallel pseudo tests/data/graph_test_tree_par.gml --alg ltree

docker run --rm -ti czentye/slambuc:0.5.0 tree parallel pseudo_mp tests/data/graph_test_tree_par.gml --alg ltree

docker run --rm -ti czentye/slambuc:0.5.0 tree path greedy tests/data/graph_test_tree_ser.gml --alg greedy

docker run --rm -ti czentye/slambuc:0.5.0 tree path meta tests/data/graph_test_tree_ser.gml --alg meta

docker run --rm -ti czentye/slambuc:0.5.0 tree path min tests/data/graph_test_tree_ser.gml --alg min

docker run --rm -ti czentye/slambuc:0.5.0 tree path seq tests/data/graph_test_tree_ser.gml --alg seq

docker run --rm -ti czentye/slambuc:0.5.0 tree path state tests/data/graph_test_tree_ser.gml --alg cacheless
docker run --rm -ti czentye/slambuc:0.5.0 tree path state tests/data/graph_test_tree_ser.gml --alg stateful

docker run --rm -ti czentye/slambuc:0.5.0 tree serial bicriteria tests/data/graph_test_tree_ser.gml --alg biheuristic
docker run --rm -ti czentye/slambuc:0.5.0 tree serial bicriteria tests/data/graph_test_tree_ser.gml --alg bifptas
docker run --rm -ti czentye/slambuc:0.5.0 tree serial bicriteria tests/data/graph_test_tree_ser.gml --alg dual

docker run --rm -ti czentye/slambuc:0.5.0 tree serial greedy tests/data/graph_test_tree_ser.gml --alg greedy

docker run --rm -ti czentye/slambuc:0.5.0 tree serial ilp tests/data/graph_test_tree_ser.gml --alg cfg --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree serial ilp tests/data/graph_test_tree_ser.gml --alg hybrid --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree serial ilp tests/data/graph_test_tree_ser.gml --alg mtx --solver glpk
docker run --rm -ti czentye/slambuc:0.5.0 tree serial ilp tests/data/graph_test_tree_ser.gml --alg all --solver glpk

docker run --rm -ti czentye/slambuc:0.5.0 tree serial pseudo tests/data/graph_test_tree_ser.gml --alg btree
docker run --rm -ti czentye/slambuc:0.5.0 tree serial pseudo tests/data/graph_test_tree_ser.gml --alg ltree

docker run --rm -ti czentye/slambuc:0.5.0 tree serial pseudo_mp tests/data/graph_test_tree_ser.gml --alg btree
docker run --rm -ti czentye/slambuc:0.5.0 tree serial pseudo_mp tests/data/graph_test_tree_ser.gml --alg ltree
