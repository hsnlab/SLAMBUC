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
import itertools
import pathlib
import random

import networkx as nx
import numpy as np
import pandas as pd
import scipy

from slambuc.alg.service.common import *
from slambuc.gen.cluster.syn_job import random_job
from slambuc.gen.io import save_trees_to_file
from slambuc.gen.transform import faasify_dag_by_duplication

# Default sample job/task file of the installed spar package
DEF_TASK_CSV = pathlib.Path(pathlib.Path(__file__).parent / "samples/sample_tasks.csv")
DEF_BATCH_CSV = pathlib.Path(pathlib.Path(__file__).parent / "samples/batch_task.csv")
DEF_TASK_CSV_HEADER = ('job', 'task', 'duration', 'cpu', 'mem', 'num')
DEF_TASK_CSV_COLS = (1, 2, 3, 4, 5, 6)
# Default attributes for the front-end dispatcher function
DISP_NODE = 0
DISP_RUNTIME = 1
DISP_MEM = 0.1
# Default attributes of tree nodes
DEF_MEM_MAX = 100
DEF_DATA_FACTOR = 0.2

DEF_JOB_TREE_PREFIX = "job_tree"


def convert_tasks_to_dag(job_name: str, tasks: pd.DataFrame, mem_max: int = DEF_MEM_MAX,
                         data_mean: int = None) -> tuple[nx.DiGraph, int]:
    """Convert the task lines of given job *job_name* into a DAG and return it with the generated front-end root node"""
    dag = nx.DiGraph(**{NAME: job_name})
    # Build task DAG
    for _, task in tasks.iterrows():
        # Extract dependencies
        v, *pred = task.task.split('_')
        try:
            v = int(v[1:])
        except ValueError:
            return
        # Add given node and its predecessors
        dag.add_node(v, **{RUNTIME: int(task.duration), CPU: task.cpu / 100, MEMORY: int(task.mem * mem_max)})
        for p in pred:
            dag.add_edge(int(p), v, **{RATE: int(task.num)})
    # Add dispatcher node
    for v in list(filter(lambda _v: not len(dag.pred[_v]), dag)):
        dag.add_edge(DISP_NODE, v, **{RATE: 1})
    dag.nodes[DISP_NODE].update(**{RUNTIME: DISP_RUNTIME, MEMORY: DISP_MEM})
    # Connect dispatcher function to PLATFORM
    dag.add_edge(PLATFORM, DISP_NODE, **{RATE: 1})
    # Artificially fill data overheads
    data_mean = data_mean if data_mean else DEF_DATA_FACTOR * tasks["duration"].mean()
    # Draw data overhead from exponential distribution with lambda = 1 / avg(runtimes) rounded to integer (min 1)
    data_values = dict(zip(dag.edges, np.ceil(scipy.stats.expon(scale=data_mean).rvs(size=len(dag.edges))).astype(int)))
    nx.set_edge_attributes(dag, values=data_values, name=DATA)
    return dag, DISP_NODE


def igenerate_job_tree(job_df: pd.DataFrame, min_size: int = 0) -> nx.DiGraph:
    """Generate job service trees one-by-one from *min_size*"""
    jobs = job_df.groupby("job")["task"].count()
    viable_jobs = jobs[min_size <= jobs]
    for job in viable_jobs.index:
        dag, root = convert_tasks_to_dag(job, job_df[job_df["job"] == job])
        if dag is not None:
            yield faasify_dag_by_duplication(dag, root)


def igenerate_syn_tree(n: int | tuple[int, int], iteration: int = 1, job_lb: int = 10) -> nx.DiGraph:
    """Generate job service tree based on empirical distributions"""
    tree_cntr = i = 0
    while tree_cntr < iteration:
        size = random.randint(job_lb, n[1]) if isinstance(n, tuple) else n
        job_df = random_job(task_num=size)
        dag, root = convert_tasks_to_dag(f"syn_job_{i}", job_df)
        tree = faasify_dag_by_duplication(dag, root)
        if ((isinstance(n, int) and len(tree) - 1 == size) or
                (isinstance(n, tuple) and n[0] <= (len(tree) - 1) <= n[1])):
            if tree_cntr and tree_cntr % 10 == 0:
                print(f"Found {tree_cntr} tree[{n=}] out of {i:5d} generated job")
            yield tree
            tree_cntr += 1
        i += 1


########################################################################################################################


def generate_all_job_trees(data_dir: str, task_file: str = DEF_TASK_CSV, start: int = 10, end: int = None,
                           step: int = 10, tree_name: str = DEF_JOB_TREE_PREFIX):
    """Generate all job service trees with size interval between *start* and *end* and save to separate files"""
    print(f"Load data from {task_file}...")
    job_df = pd.read_csv(task_file, usecols=DEF_TASK_CSV_COLS, names=DEF_TASK_CSV_HEADER)
    trees = [tree for tree in igenerate_job_tree(job_df, min_size=start)]
    max_size = max(map(len, trees)) - 1
    end = end if end is not None else max_size
    print(f"Generated {len(trees)} job trees with {start} <= size <= {max_size}")
    for min_size, max_size in itertools.pairwise(range(start, end + step, step)):
        filtered_trees = [t for t in trees if min_size <= len(t) - 1 < max_size]
        if len(filtered_trees):
            print(f"Filtered {len(filtered_trees)} trees with {min_size} <= size <= {max_size}")
            file_name = pathlib.Path(data_dir, f"{tree_name}_n{min_size}-{max_size}.npy").resolve()
            print(f"Saving trees into {file_name}...")
            save_trees_to_file(filtered_trees, file_name=file_name, padding=max_size)
    print("Finished")


def generate_syn_job_trees(data_dir: str, iteration: int = 100, start: int = 10, end: int = 100, step: int = 10,
                           tree_name: str = DEF_JOB_TREE_PREFIX):
    """Generate synthetic job service trees with size interval between *start* and *end* and save to separate files"""
    for n in range(start, end + 1, step):
        print(f"Generating synthetic task service trees for {n=} by exhaustive iteration...")
        file_name = pathlib.Path(data_dir, f"syn_{tree_name}_n{n}.npy").resolve()
        output_trees = list(igenerate_syn_tree(n, iteration, job_lb=int(n * 0.5)))
        print(f"Saving trees into {file_name}...")
        save_trees_to_file(output_trees, file_name, padding=n)
    print("Finished")


def generate_mixed_job_trees(data_dir: str, task_file: str = DEF_TASK_CSV, iteration: int = 100, start: int = 10,
                             end: int = 100, step: int = 10, tree_name: str = DEF_JOB_TREE_PREFIX):
    """Generate job trees from sample data and extend it with synthetic trees"""
    print(f"Load data from {task_file}...")
    job_df = pd.read_csv(task_file, usecols=DEF_TASK_CSV_COLS, names=DEF_TASK_CSV_HEADER)
    trees = [tree for tree in igenerate_job_tree(job_df, min_size=start)]
    max_size = max(map(len, trees)) - 1
    end = end if end is not None else max_size
    print(f"Generated {len(trees)} job trees with {start} <= size <= {max_size}...")
    for min_size, max_size in itertools.pairwise(range(start, end + step, step)):
        filtered_trees = [t for t in trees if min_size <= len(t) - 1 < max_size]
        print(f"Filtered {len(filtered_trees)} trees with {min_size} <= size <= {max_size}")
        if len(filtered_trees) > iteration:
            # Under-sample
            print(f"Under-sampling filtered trees....")
            tree_output = random.sample(filtered_trees, iteration)
        else:
            # Extend with synthetic trees
            syn_tree_num = iteration - len(filtered_trees)
            print(f"Generate additional {syn_tree_num} synthetic job tree...")
            tree_output = list(igenerate_syn_tree((start, max_size), syn_tree_num))
            tree_output = itertools.chain(filtered_trees, tree_output)
        file_name = pathlib.Path(data_dir, f"{tree_name}_n{min_size}-{max_size}.npy").resolve()
        print(f"Saving trees into {file_name}...")
        save_trees_to_file(tree_output, file_name=file_name, padding=max_size)
    print("Finished")


if __name__ == '__main__':
    # generate_all_job_tree("../../../validation/data")
    # generate_syn_job_trees("../../../validation/data")
    generate_mixed_job_trees("../../../validation/data")
