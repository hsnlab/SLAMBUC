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
import os
import pathlib

from slambuc.generator.cluster.job_tree import generate_mixed_job_trees
from slambuc.generator.microservice.faas_tree import generate_all_faas_trees
from slambuc.generator.random.random_tree import generate_all_random_trees, generate_random_trees

DATA_DIR = "data"
MAX_INST = 100
MAX_TREE_SIZE = 100
PERF_TREE_SIZE_RANGE = (10, MAX_TREE_SIZE + 1, 10)  # [10, 20, ..., 140, 150]
PERF_TEST_DATA_PARAMS = dict(data_dir=DATA_DIR, iteration=MAX_INST, file_prefix="rand_tree")
COST_TEST_DATA_PARAMS = dict(data_dir=DATA_DIR, iteration=MAX_INST, start=10, end=MAX_TREE_SIZE, step=10)


def main():
    data_dir = pathlib.Path(DATA_DIR).resolve()
    print("Clear data dir:", data_dir)
    for f in data_dir.glob("*.npy"):
        os.remove(f)
    print("Generate test data ...")
    for n in range(*PERF_TREE_SIZE_RANGE):
        generate_random_trees(n, **PERF_TEST_DATA_PARAMS)
    generate_all_random_trees(**COST_TEST_DATA_PARAMS)
    generate_mixed_job_trees(**COST_TEST_DATA_PARAMS)
    generate_all_faas_trees(**COST_TEST_DATA_PARAMS)
    print("Finished")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
