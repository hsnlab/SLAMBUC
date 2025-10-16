#!/usr/bin/env bash
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

export SCRIPT_DIR=$(readlink -f "$(dirname "$0")")
export PROJECT_ROOT=$(readlink -f "${SCRIPT_DIR}/..")

VER=$(python3 -c "import slambuc;print(slambuc.__version__)")
IMG="czentye/slambuc:${VER}"

function run_slambuc() {
    docker run --rm -v "${PROJECT_ROOT}":/usr/src/slambuc -e SLAMBUC_UNFOLD=yes -ti "${IMG}" "$@"
}

run_slambuc chain path dp tests/data/chain_test_sequence_serial.npz --alg chain
run_slambuc chain path dp tests/data/chain_test_sequence_serial.npz --alg vector

run_slambuc chain path greedy tests/data/chain_test_sequence_serial.npz

run_slambuc chain path min tests/data/chain_test_sequence_serial.npz

run_slambuc chain path sp tests/data/chain_test_sequence_serial.npz

run_slambuc chain serial greedy tests/data/chain_test_sequence_serial.npy

run_slambuc chain serial ilp tests/data/chain_test_sequence_serial.npy --alg cfg #--solver glpk
run_slambuc chain serial ilp tests/data/chain_test_sequence_serial.npy --alg mtx #--solver glpk

run_slambuc dag ilp tests/data/graph_test_dag.gml --alg greedy #--solver glpk
run_slambuc dag ilp tests/data/graph_test_dag.gml --alg dag #--solver glpk

run_slambuc ext baseline tests/data/graph_test_tree.gml --alg singleton
run_slambuc ext baseline tests/data/graph_test_tree.gml --alg no

run_slambuc ext csp tests/data/graph_test_tree.gml --alg csp
run_slambuc ext csp tests/data/graph_test_tree.gml --alg gen

run_slambuc ext greedy tests/data/graph_test_tree.gml --alg greedy
run_slambuc ext greedy tests/data/graph_test_tree.gml --alg weight
run_slambuc ext greedy tests/data/graph_test_tree.gml --alg lat

run_slambuc ext mincut tests/data/graph_test_tree.gml --alg chain
run_slambuc ext mincut tests/data/graph_test_tree.gml --alg ksplit
run_slambuc ext mincut tests/data/graph_test_tree.gml --alg tree

run_slambuc tree layout ilp tests/data/graph_test_tree.gml --alg hybrid #--solver glpk
run_slambuc tree layout ilp tests/data/graph_test_tree.gml --alg mtx #--solver glpk
run_slambuc tree layout ilp tests/data/graph_test_tree.gml --alg all #--solver glpk

run_slambuc tree parallel greedy tests/data/graph_test_tree_par.gml --alg greedy

run_slambuc tree parallel ilp tests/data/graph_test_tree_par.gml --alg cfg #--solver glpk
run_slambuc tree parallel ilp tests/data/graph_test_tree_par.gml --alg hybrid #--solver glpk
run_slambuc tree parallel ilp tests/data/graph_test_tree_par.gml --alg mtx #--solver glpk
run_slambuc tree parallel ilp tests/data/graph_test_tree_par.gml --alg all #--solver glpk

run_slambuc tree parallel pseudo tests/data/graph_test_tree_par.gml --alg btree
run_slambuc tree parallel pseudo tests/data/graph_test_tree_par.gml --alg ltree

run_slambuc tree parallel pseudo_mp tests/data/graph_test_tree_par.gml --alg ltree

run_slambuc tree path greedy tests/data/graph_test_tree_ser.gml --alg greedy

run_slambuc tree path meta tests/data/graph_test_tree_ser.gml --alg meta

run_slambuc tree path min tests/data/graph_test_tree_ser.gml --alg min

run_slambuc tree path seq tests/data/graph_test_tree_ser.gml --alg seq

run_slambuc tree path state tests/data/graph_test_tree_ser.gml --alg cacheless
run_slambuc tree path state tests/data/graph_test_tree_ser.gml --alg stateful

run_slambuc tree serial bicriteria tests/data/graph_test_tree_ser.gml --alg biheuristic
run_slambuc tree serial bicriteria tests/data/graph_test_tree_ser.gml --alg bifptas
run_slambuc tree serial bicriteria tests/data/graph_test_tree_ser.gml --alg dual

run_slambuc tree serial greedy tests/data/graph_test_tree_ser.gml --alg greedy

run_slambuc tree serial ilp tests/data/graph_test_tree_ser.gml --alg cfg #--solver glpk
run_slambuc tree serial ilp tests/data/graph_test_tree_ser.gml --alg hybrid #--solver glpk
run_slambuc tree serial ilp tests/data/graph_test_tree_ser.gml --alg mtx #--solver glpk
run_slambuc tree serial ilp tests/data/graph_test_tree_ser.gml --alg all #--solver glpk

run_slambuc tree serial pseudo tests/data/graph_test_tree_ser.gml --alg btree
run_slambuc tree serial pseudo tests/data/graph_test_tree_ser.gml --alg ltree

run_slambuc tree serial pseudo_mp tests/data/graph_test_tree_ser.gml --alg btree
run_slambuc tree serial pseudo_mp tests/data/graph_test_tree_ser.gml --alg ltree
