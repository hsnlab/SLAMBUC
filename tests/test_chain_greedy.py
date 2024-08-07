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
import random

from slambuc.alg.chain.path.greedy import greedy_chain_partitioning
from slambuc.misc.util import evaluate_chain_partitioning


def run_test(runtime: list, memory: list, rate: list, M: int = math.inf, N: int = math.inf, L: int = math.inf,
             start: int = 0, end: int = None, delay: int = 1, unit: int = 100):
    results = greedy_chain_partitioning(runtime, memory, rate, M, N, L, start, end, delay, unit)
    for i, (partition, opt_cost, opt_lat) in enumerate(results):
        print(f"  GREEDY[{i}]  ".center(80, '#'))
        evaluate_chain_partitioning(partition, opt_cost, opt_lat, runtime, memory, rate, M, N,
                                    L, start, end, delay, unit)
    return results


def test_chain():
    runtime = [20, 40, 50, 20, 70, 40, 50, 60, 40, 10]
    memory = [3, 3, 2, 1, 2, 1, 2, 1, 2, 3]
    rate = [1, 1, 2, 2, 1, 3, 1, 2, 1, 3]
    delay = 10
    M = 6
    N = 3
    L = 500
    start = 0
    end = len(runtime) - 1
    unit = 100
    run_test(**locals())


def test_random_chain():
    runtime = [random.randint(10, 100) for _ in range(10)]
    memory = [random.randint(1, 3) for _ in range(10)]
    rate = [random.randint(1, 3) for _ in range(10)]
    delay = 10
    M = 6
    N = 2
    L = sum(runtime) + 1 + delay * random.randint(len(runtime) // 4, len(runtime) // 2)
    start = 0
    end = len(runtime) - 1
    unit = 100
    run_test(**locals())


if __name__ == '__main__':
    test_chain()
    # test_random_chain()
