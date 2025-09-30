#!/usr/bin/env python3
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
import collections
import itertools
import json
import math
import operator
import pprint
import time

import pandas as pd
import tabulate

from slambuc.alg.chain.serial import *
from slambuc.misc.random import get_random_chain_data
from slambuc.misc.util import print_ser_chain_summary

CHAIN_ALGS = dict(
    GREEDY=greedy_ser_chain_partitioning,
    ILP_CFG=chain_cfg_partitioning,
    ILP_MTX=chain_mtx_partitioning
)


def run_all_chain_ser_tests(params: dict) -> list:
    stats = []
    for name, ser_chain_alg in CHAIN_ALGS.items():
        print(f"Executing {name}")
        t_start = time.perf_counter()
        result = ser_chain_alg(**params)
        alg_time = time.perf_counter() - t_start
        if name.startswith('GREEDY'):
            stats.extend([[name + f'_{i}', *res, round(alg_time, ndigits=8)] for i, res in enumerate(result)])
        else:
            stats.append([name, *result, round(alg_time, ndigits=8)])
    return stats


def compare_results():
    params = dict(runtime=[20, 40, 50, 20, 70, 40, 50, 60, 40, 10],
                  memory=[3, 3, 2, 1, 2, 1, 2, 1, 2, 3],
                  rate=[1, 1, 2, 2, 1, 3, 1, 2, 1, 3],
                  data=[5, 3, 5, 2, 1, 3, 2, 3, 5, 1],
                  delay=10,
                  M=6,
                  L=1050,
                  # L=math.inf,
                  start=0,
                  end=9)
    ##########################################################
    stats = run_all_chain_ser_tests(params)
    print('#' * 80)
    print("Summary:")
    print(tabulate.tabulate(stats, ['Alg.', 'Partition', 'Cost', 'Latency', 'Time (s)'],
                            colalign=('left', 'left', 'decimal', 'decimal', 'decimal'), tablefmt='pretty'))


def test_random_validation(n: int = 10, cache_failed: bool = True, stop_failed: bool = False):
    runtime, memory, rate, data = get_random_chain_data(n, (10, 100), (1, 3), (1, 3), (1, 5))
    params = dict(runtime=runtime,
                  memory=memory,
                  rate=rate,
                  data=data,
                  delay=10,
                  M=6,
                  L=700,
                  start=0,
                  end=n - 1)
    print_ser_chain_summary(runtime, memory, rate, data)
    stat = run_all_chain_ser_tests(params)
    print("  Statistics  ".center(80, '#'))
    print("Params:", pprint.pformat(params))
    print(tabulate.tabulate(stat, ['Alg.', 'Partition', 'Cost', 'Latency', 'Time (s)'],
                            numalign='center', stralign='left', tablefmt='pretty'))
    alg_num = len(CHAIN_ALGS) - 1
    p_grdy, p_algs = [p[1] for p in stat[:-alg_num]], list(map(operator.itemgetter(1), stat[-alg_num:]))
    c_grdy, c_algs = stat[0][2], list(map(operator.itemgetter(2), stat[-alg_num:]))
    l_grdy, l_algs = [p[3] for p in stat[:-alg_num]], list(map(operator.itemgetter(3), stat[-alg_num:]))
    validated = all((all(p in p_grdy for p in p_algs),
                     all(c_grdy == c for c in c_algs) if all((c_grdy, *c_algs)) else True,
                     all(l in l_grdy for l in l_algs)))
    if not validated and cache_failed:
        with open(f"failed_chain_{time.time()}.json", 'w') as f:
            json.dump(params, f, indent=4)
    result = 'SUCCESS' if validated else 'FAILED'
    print(f"Validation: {result}")
    if stop_failed:
        assert result == 'SUCCESS'
    print('#' * 80)
    return result, stat


def stress_test(n: int = 10, iteration: int = 100, cache_failed: bool = True, stop_failed: bool = False):
    results = [test_random_validation(n, cache_failed=cache_failed, stop_failed=stop_failed) for _ in range(iteration)]
    valid, stats = zip(*results)
    print("Validation statistics:", collections.Counter(valid))
    df = pd.DataFrame(itertools.chain(*stats))
    pd.set_option('display.expand_frame_repr', False)
    grouped_stat = df[(df[2] < math.inf) & (df[0].isin(('GREEDY_0', *CHAIN_ALGS)))][[0, 4]].groupby(0)
    print("Runtime statistics:")
    print(grouped_stat.describe().reset_index().sort_values((4, 'mean'), ascending=False))


if __name__ == '__main__':
    compare_results()
    # test_random_validation()
    # stress_test(10, iteration=100)
