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
import collections
import itertools
import math
import typing

import networkx as nx

from slambuc.alg import COST, INFEASIBLE, T_BRESULTS
from slambuc.alg.chain.path.dp import chain_partitioning, extract_barr
from slambuc.alg.app import *
from slambuc.alg.app.common import LABEL
from slambuc.alg.util import ipostorder_dfs, isubchains, ibacktrack_chain, leaf_label_nodes, recreate_subchain_blocks


class TPart(typing.NamedTuple):
    """Store subtree attributes for a given meta-subcase."""
    barr: set = set()  # Barrier/heading nodes of the given subtree partitioning
    cost: int = math.inf  # Sum cost of the partitioning

    def __repr__(self):
        return repr(tuple(self))


def meta_tree_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, N: int = math.inf, L: int = math.inf,
                           cp_end: int = None, delay: int = 1, unit: int = 100, only_barr: bool = False,
                           partition=chain_partitioning, barriers=extract_barr) -> T_BRESULTS:
    """
    Calculates minimal-cost partitioning of an app graph(tree) with respect to an upper bound **M** on the total
    memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes using
    the *partition* function to partition subchains independently.

    Cost calculation relies on the rounding *unit* and number of vCPU cores *N*, whereas platform invocation *delay*
    is used for latency calculations.

    It gives an optimal result only in case the cost function regarding the chain attributes is subadditive,
    that is k_opt = k_min is guaranteed for each case.

    Instead of full partitioning, it only returns the list of barrier nodes.

    Details in: J. Czentye, I. Pelle and B. Sonkoly, "Cost-optimal Operation of Latency Constrained Serverless
    Applications: From Theory to Practice," NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium,
    Miami, FL, USA, 2023, pp. 1-10, doi: 10.1109/NOMS56928.2023.10154412.

    :param tree:        app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:        root node of the graph
    :param M:           upper memory bound of the partition blocks (in MB)
    :param N:           upper CPU core bound of the partition blocks
    :param L:           latency limit defined on the critical path (in ms)
    :param cp_end:      tail node of the critical path in the form of subchain[root -> cp_end]
    :param delay:       invocation delay between blocks
    :param unit:        rounding unit for the cost calculation (default: 100 ms)
    :param only_barr:   return the subtree roots (barrier nodes) instead of full node partitioning
    :param partition:   function that partitions chain into blocks wrt. M and L
    :param barriers:    function that extracts barrier nodes from _partition_'s returned data structure
    :return:            tuple of barrier nodes, sum cost of the partitioning, and optimal number of cuts
    """
    tree = leaf_label_nodes(tree)
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # c_max is the number of cuts allowed by L or at most the number of edges on cpath
    c_max = math.floor(min((L - sum(tree.nodes[v][RUNTIME] for v in cpath)) / delay, len(cpath) - 1))
    # Check lower bound for latency limit
    if c_max < 0:
        return [], None, c_max
    DP = collections.defaultdict(lambda: [TPart() for _ in range(c_max + 1)])
    for pred, n in ipostorder_dfs(tree, root):
        # Only branched nodes are referred in the subcases
        if len(tree.succ[pred]) <= 1 and pred is not PLATFORM:
            continue
        # Subcases of leaves can be precalculated
        if n in tree.nodes[root][LABEL]:
            # For single nodes, a feasible solution exists by definition
            _, opt_cost, _ = partition([tree.nodes[n][RUNTIME]], [tree.nodes[n][MEMORY]], [tree[pred][n][RATE]], M, N,
                                       delay=delay, unit=unit)
            DP[n] = [TPart({n}, opt_cost)] * (c_max if n == cp_end else 1)
            continue
        for (head_part, tail_part), branches in isubchains(tree, n, cp_end):
            subchain = head_part + tail_part
            runtime, memory, rate = zip(*[(tree.nodes[v][RUNTIME], tree.nodes[v][MEMORY], tree[u][v][RATE])
                                          for u, v in itertools.pairwise([pred, *subchain])])
            sum_m_cost = sum(DP[m][0].cost for m in branches if m not in cpath)
            sum_m_barr = set().union(*(DP[m][0].barr for m in branches if m not in cpath))
            # Subchain has no intersection with cpath -> no need to track cuts
            if n not in cpath:
                # Without L, there should exist feasible solution wrt. M
                barr, opt_cost, _ = partition(runtime, memory, rate, M, N, delay=delay, unit=unit)
                if (sum_cost := opt_cost + sum_m_cost) < DP[n][0].cost:
                    DP[n][0] = TPart({subchain[b] for b in barr} | sum_m_barr, sum_cost)
            # Subchain is the tail part of cpath -> all inner edges are allowed to be merged
            elif subchain[-1] == cp_end:
                # If subchain is the cpath -> partitioning can be calculated directly applying L
                if subchain[0] == root:
                    barr, opt_cost, opt_lat = partition(runtime, memory, rate, M, N, L, delay=delay, unit=unit)
                    if not barr:
                        return barr, opt_cost, opt_lat
                    opt_barr_cost = TPart({subchain[b] for b in barr} | sum_m_barr, sum_cost := opt_cost + sum_m_cost)
                    for c in range(len(barr) - 1, c_max + 1):
                        if sum_cost < DP[n][c].cost:
                            DP[n][c] = opt_barr_cost
                else:
                    # Without L, there should exist feasible solution wrt. M
                    CDP, *_ = partition(runtime, memory, rate, M, N, delay=delay, unit=unit, ret_dp=True)
                    c_best, part_best = 0, None
                    for c in range(c_max + 1):
                        if c < len(subchain):
                            # No need to track infeasible solutions
                            if CDP[-1][c][COST] == math.inf:
                                continue
                            # If c-1 cuts give cheaper solution -> it must be involved in the at most c cuts solution
                            elif c == 0 or CDP[-1][c][COST] < CDP[-1][c_best][COST]:
                                part_best = TPart({subchain[b] for b in barriers(CDP, c)} | sum_m_barr,
                                                  CDP[-1][c][COST] + sum_m_cost)
                                c_best = c
                        if part_best.cost < DP[n][c].cost:
                            DP[n][c] = part_best
            # Subchain head is part of cpath -> a must cut edge is introduced
            else:
                m_cp = next(m for m in tree.succ[head_part[-1]] if m in cpath)
                c_cache = {}
                # Iterate over all feasible cut solutions of the subtree T_m_cp
                for k in range(0, c_max):
                    # If the subtree cannot be partitioned with k cuts -> all k-related subcases are infeasible
                    if DP[m_cp][k].cost == math.inf:
                        continue
                    # If the optimal partition cost for k equals to k+1 -> k+1 subcases will the same or more expensive
                    # For given k -> each calculated c cuts are also calculated for k-1 (k->1-c_max, k+1->2-c_max, ...)
                    if k > 0 and DP[m_cp][k - 1].cost <= DP[m_cp][k].cost:
                        continue
                    # Iterate over all possible cuts on the head_part of the subchain
                    for c_head in reversed(range(0, c_max - k)):
                        # Use previously calculated result
                        if c_head in c_cache:
                            barr, opt_cost = c_cache[c_head]
                        else:
                            L_head = sum(tree.nodes[v][RUNTIME] for v in head_part) + c_head * delay
                            barr, opt_cost, _ = partition(runtime, memory, rate, M, N, L_head, 0, len(head_part) - 1,
                                                          delay, unit)
                            # If subchain cannot be partitioned with L_head -> stricter L_head is also infeasible
                            if not barr:
                                break
                            # Precalculate stricter solutions based on the distance between optimal cut and L_head cut
                            for _c in reversed(range(len(barr) - 1, c_head + 1)):
                                c_cache[_c] = (barr, opt_cost)
                        c = k + c_head + 1
                        if (sum_cost := opt_cost + DP[m_cp][k].cost + sum_m_cost) < DP[n][c].cost:
                            DP[n][c] = TPart({subchain[b] for b in barr}.union(DP[m_cp][k].barr, sum_m_barr), sum_cost)
        # If no feasible solution exists for the subtree T_n wrt. L (c_0, c_max = inf) -> no feasible solution for T
        if min(DP[n][0], DP[n][-1]) == math.inf:
            return INFEASIBLE
    c_opt = min(range(len(DP[root])), key=lambda _c: DP[root][_c].cost)
    best_barrs, best_cost = DP[root][c_opt]
    return list(best_barrs) if only_barr else recreate_subchain_blocks(tree, best_barrs), best_cost, c_opt
