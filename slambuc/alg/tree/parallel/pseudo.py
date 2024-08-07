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
import operator
import typing
import warnings

import networkx as nx

from slambuc.alg import INFEASIBLE, T_RESULTS
from slambuc.alg.app import *
from slambuc.alg.tree.serial.pseudo import SubLTreePart, OPT
from slambuc.alg.util import (ipostorder_dfs, ileft_right_dfs, ibacktrack_chain, recreate_subtree_blocks,
                              par_inst_count, verify_limits)


class SubParBTreePart(typing.NamedTuple):
    """Store subtree partitioning attributes for a given subcase."""
    cost: int = math.inf  # Optimal sum cost of the subtree partitioning (OPT)
    top_cost: int = math.inf  # Cost of the topmost subtree block
    top_blk: set[int] = set()  # Nodes of the topmost block
    barr: set[int] = set()  # Barrier/heading nodes of the given subtree partitioning

    def __repr__(self):
        return repr(tuple(self))


def pseudo_par_btree_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf, N: int = 1,
                                  cp_end: int = None, delay: int = 1, bidirectional: bool = True) -> T_RESULTS:
    """
    Calculates minimal-cost partitioning of a app graph(tree) with respect to an upper bound **M** on the total
    memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
    applying bottom-up tree traversal approach.

    Block metrics are calculated based on parallelized execution platform model.

    Provide suboptimal partitioning due to the inaccurate latency calculation that directly comes from the bottom-up
    tree traversal approach.

    :param tree:            app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:            root node of the graph
    :param M:               upper memory bound of the partition blocks in MB
    :param L:               latency limit defined on the critical path in ms
    :param N:               available CPU core count
    :param cp_end:          tail node of the critical path in the form of subchain[root -> cp_end]
    :param delay:           invocation delay between blocks
    :param bidirectional:   use bidirectional subcase elimination (may introduce quadratic increase in the worst case)
    :return:                tuple of optimal partitioning, reached sum cost and latency on the critical path
    """
    if N > 1:
        warnings.warn(f"Suboptimal for {N=} due to violated monotonicity of cost function in upward merging!")
    # Set of critical path's nodes
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(tree, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    # Init empty data structure for optimal results of subtrees T_v
    DP = {n: collections.defaultdict(dict) for n in tree if n is not PLATFORM}
    # Iterate nodes in a bottom-up traversal order
    for p, v in ipostorder_dfs(tree, root):
        r_v, d_v, t_v, m_v = tree[p][v][RATE], tree[p][v][DATA], tree.nodes[v][RUNTIME], tree.nodes[v][MEMORY]
        # SINGLETON: calculate the default subcase of singleton partition of node v
        cost = r_v * (d_v + t_v) + sum(par_inst_count(r_v, vs[RATE], N) * vs[DATA] for vs in tree.succ[v].values())
        # Only add fetching overhead for root node and omit caching to ensure lat monotonicity of merging
        lat = d_v + t_v if v == root else t_v if v in cpath else 0
        DP[v][lat, lat][m_v, m_v] = SubParBTreePart(cost, cost, {v}, {v})
        # Bottom-up propagation for considering v's descendant subcases in sequential order (v is not leaf)
        # -->   p   ---->   v   ----[i.]---->   b
        for b in tree.successors(v):
            # Init empty data structure of subcase T[v,b]
            _cache = collections.defaultdict(dict)
            r_b, d_b, t_b = tree[v][b][RATE], tree[v][b][DATA], tree.nodes[b][RUNTIME]
            # Calculate possible latency/memory combinations
            for lats_v, lats_b in itertools.product(DP[v], DP[b]):
                for mem_v, mem_b in itertools.product(DP[v][lats_v], DP[b][lats_b]):
                    sub_v, sub_b = DP[v][lats_v][mem_v], DP[b][lats_b][mem_b]
                    lat_v, blk_lat_v = lats_v
                    lat_b, blk_lat_b = lats_b
                    # Latency calculation in case v -> b edge is in cpath
                    if b in cpath:
                        # CUT: v -> b edge is marked as a cut (opt subcases of b have the dedicated memory value 0)
                        if mem_b == (OPT, OPT):
                            # Add caching overhead of inter-block call
                            top_blk_lat = blk_lat_v + math.ceil(r_b / (r_v * N)) * d_b
                            # Add invocation delay and fetch overhead of inter-block call
                            if (lat := top_blk_lat + delay + d_b + lat_b) > L:
                                # Infeasible subcase due to exceeded latency constraint
                                continue
                        # MERGE: v -> b edge is marked as a merge
                        else:
                            # Top block's latency comes for only the single cp node v, hence n_v = 1
                            top_blk_lat = blk_lat_v + math.ceil(r_b / (r_v * N)) * blk_lat_b
                            # Calculate new latency based on the recalculated top block's latency
                            if (lat := lat_b - blk_lat_b + top_blk_lat) > L:
                                # Infeasible subcase due to exceeded latency constraint
                                continue
                    else:
                        # Top block's attributes remain the same, either v in cpath or not
                        top_blk_lat, lat = blk_lat_v, lat_v
                    # CUT: v -> b edge is marked as a cut
                    if mem_b == (OPT, OPT):
                        # Top block's attributes remain the same
                        mem, top_blk = mem_v, sub_v.top_blk
                        # Sub-partitions are just concatenated
                        barr, cost, top_blk_cost = sub_v.barr | sub_b.barr, sub_v.cost + sub_b.cost, sub_v.top_cost
                    # MERGE: v -> b edge is marked as a merge
                    elif (mem_ld := mem_v[0] + mem_b[0]) > M:
                        # Infeasible subcase due to exceeded memory constraint
                        continue
                    else:
                        mem_op, top_blk_cost = mem_v[1], sub_v.top_cost - par_inst_count(r_v, r_b, N) * d_b
                        for f in sub_b.top_blk:
                            r_f = tree[next(tree.predecessors(f))][f][RATE]
                            if (mem_op := max(mem_op, min(math.ceil(r_f / r_v), N) * tree.nodes[f][MEMORY])) > M:
                                # Infeasible subcase due to exceeded memory constraint
                                continue
                            top_blk_cost += (par_inst_count(r_v, r_f, N) * tree.nodes[f][RUNTIME] +
                                             sum(par_inst_count(r_v, fs[RATE], N) * fs[DATA]
                                                 for s, fs in tree.succ[f].items() if s not in sub_b.top_blk))
                        # Top blocks of the two sub-partitions are merged together with root node v
                        mem = mem_ld, mem_op
                        barr, top_blk = sub_v.barr | sub_b.barr - {b}, sub_v.top_blk | sub_b.top_blk
                        cost = sub_v.cost - sub_v.top_cost + sub_b.cost - sub_b.top_cost + top_blk_cost
                    # Store the min cost subcase
                    sub_lats = lat, top_blk_lat
                    if mem not in _cache[sub_lats] or cost < _cache[sub_lats][mem].cost:
                        _cache[sub_lats][mem] = SubParBTreePart(cost, top_blk_cost, top_blk, barr)
                    # Check whether the current subcase is a better sub-solution for state (v, sub_lats, mem)
                    if mem not in _cache[sub_lats] or cost < _cache[sub_lats][mem].cost:
                        if bidirectional:
                            # Eliminate prior subcases that are dominated by the new subcase
                            for l, m in tuple((_l, _m) for _l in _cache if _l[0] >= lat and _l[1] >= top_blk_lat
                                              for _m in _cache[_l] if (_m[0] >= mem[0] and _m[1] >= mem[1]
                                                                       and _cache[_l][_m].cost >= cost)):
                                if len(_cache[l]) > 1:
                                    del _cache[l][m]
                                else:
                                    del _cache[l]
                        # Add superior subcase
                        _cache[sub_lats][mem] = SubParBTreePart(cost, top_blk_cost, top_blk, barr)
            # Store min subcases as C(v,i-1) for the next iteration of the propagation process
            DP[v] = _cache
            # Drop unnecessary subcases
            del DP[b]
        # Store the cost-opt subcases wrt. latency for node v encoded with memory value 0,0
        for lats in DP[v]:
            DP[v][lats][OPT, OPT] = min(DP[v][lats].values(), key=operator.itemgetter(OPT))
    # Subcases under the root node contain the feasible partitioning
    if opt_lats := min(DP[root], key=lambda _l: DP[root][_l][OPT, OPT].cost, default=None):
        opt = DP[root][opt_lats][OPT, OPT]
        return recreate_subtree_blocks(tree, opt.barr), opt.cost, opt_lats[OPT]
    else:
        # No feasible solution
        return INFEASIBLE


########################################################################################################################


def pseudo_par_ltree_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf, N: int = 1,
                                  cp_end: int = None, delay: int = 1, bidirectional: bool = True) -> T_RESULTS:
    """
    Calculates minimal-cost partitioning of a app graph(tree) with respect to an upper bound **M** on the total
    memory of blocks and a latency constraint **L** defined on the subchain between *root* and *cp_end* nodes, while
    applying left-right tree traversal approach.

    Block metrics are calculated based on parallelized execution platform model.

    :param tree:            app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:            root node of the graph
    :param M:               upper memory bound of the partition blocks in MB
    :param L:               latency limit defined on the critical path in ms
    :param N:               available CPU core count
    :param cp_end:          tail node of the critical path in the form of subchain[root -> cp_end]
    :param delay:           invocation delay between blocks
    :param bidirectional:   use bidirectional subcase elimination (may introduce quadratic increase in the worst case)
    :return:                tuple of optimal partitioning, reached sum cost and latency on the critical path
    """
    # Set of critical path's nodes
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(tree, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    # Init empty data structure for optimal results of subtrees
    TDP = {n: {} for n in tree if n is not PLATFORM}
    # Process subtrees of T in a bottom-up traversal order
    for p, n in ipostorder_dfs(tree, root):
        # Init empty data structure for optimal subcases T_n[v,b]
        DP = collections.defaultdict(lambda: collections.defaultdict(dict))
        r_n, d_n, t_n, m_n = tree[p][n][RATE], tree[p][n][DATA], tree.nodes[n][RUNTIME], tree.nodes[n][MEMORY]
        # Traverse subtree T_n in a left-right traversal
        #       |--(j-1.)--> [v_p]   |--(i-1.)--> [b_p]                                 | left side
        # -->  [u]  ----(j.)---->  [v]  ----(i.)---->  [b]  ----(max_k.)----> [b_k]     | right side
        for e_uvp, b_p, e_vb in ileft_right_dfs(tree, n):
            v, b = e_vb
            # Merge edge u -> v as consider node v and all its first 0 child (b=0)
            if b == 0:
                # SINGLETON: C[n,0] - calculate the default subcase of singleton partition of root node n
                if v == n:
                    cost = r_n * (d_n + t_n) + sum(par_inst_count(r_n, ns[RATE], N) * ns[DATA]
                                                   for ns in tree.succ[n].values())
                    if n in cpath:
                        nc = next(filter(lambda c: c in cpath, tree.successors(n)), None)
                        # n_v = 1 for root node n; add caching overhead on critical path here
                        lat = d_n + t_n + (math.ceil(tree[n][nc][RATE] / (r_n * N)) * tree[n][nc][DATA] if nc else 0)
                    else:
                        lat = 0
                    DP[e_vb][lat][m_n, m_n] = SubLTreePart(cost, 1, {n})
                # MERGE: C[v,0] - subcase of merging single node v into the n-rooted block containing node u
                else:
                    u, v_p = e_uvp
                    r_v, d_v = tree[u][v][RATE], tree[u][v][DATA]
                    t_v, m_v = tree.nodes[v][RUNTIME], tree.nodes[v][MEMORY]
                    # v_p = 0 => no prior sibling node, C[v,0] = C[u,j-1] + delta(u,v)
                    for lat_u in DP[e_uvp]:
                        for mem_u in DP[e_uvp][lat_u]:
                            sub_u = DP[e_uvp][lat_u][mem_u]
                            # Calculate memory prefetch and operative memory demands separately
                            mem = mem_u[0] + m_v, max(mem_u[1], min(math.ceil(r_v / r_n), N) * m_v)
                            if max(mem) > M:
                                # Infeasible subcase due to exceeded memory constraint
                                continue
                            # v in cpath => u in cpath
                            if v in cpath:
                                rel_r_v = math.ceil(r_v / (tree[next(tree.predecessors(u))][u][RATE] * N))
                                n_v = rel_r_v * sub_u.mul
                                vc = next(filter(lambda c: c in cpath, tree.successors(v)), None)
                                w_v = math.ceil(tree[v][vc][RATE] / (r_v * N)) * tree[v][vc][DATA] if vc else 0
                                # Recalculate caching overhead (remove prior block's write out from E2E latency)
                                if (lat := lat_u + n_v * (t_v - d_v + w_v)) > L:
                                    # Infeasible subcase due to exceeded latency constraint
                                    continue
                            else:
                                lat, n_v = lat_u, sub_u.mul
                            # Calculate sum cost by adding merged node runtime and caching
                            cost = (sub_u.cost + par_inst_count(r_n, r_v, N) * (t_v - d_v) +
                                    sum(par_inst_count(r_n, vs[RATE], N) * vs[DATA] for vs in tree.succ[v].values()))
                            # Check whether the current subcase is a better sub-solution for state (e_vb, lat, mem)
                            if lat not in DP[e_vb] or mem not in DP[e_vb][lat] or cost < DP[e_vb][lat][mem].cost:
                                # Add superior subcase
                                DP[e_vb][lat][mem] = SubLTreePart(cost, n_v, sub_u.barr)
            # CUT: C[v,b]
            else:
                # b_k <- C[v_i, d(v_i)]
                b_k = collections.deque(tree.successors(b), 1).pop() if len(tree.succ[b]) else 0
                # Previously merged edge: v -> b  =>  [root ... -> u -> v -> b ...]   |   [b]  --(max_k.)--> [b_w]
                DP[e_vb] = DP[b, b_k]
                # Cut edge: v -> b  |  [root ... -> u -> v] - [b ...]   |   v --(i-1.)--> b_p
                for lat_v in DP[v, b_p]:
                    for mem_v in DP[v, b_p][lat_v]:
                        for lat_b, opt_b in TDP[b].items():
                            # b in cpath => v in cpath
                            if (lat := lat_v + delay + lat_b if b in cpath else lat_v) > L:
                                # Infeasible subcase due to exceeded latency constraint
                                continue
                            sub_v = DP[v, b_p][lat_v][mem_v]
                            # Only concatenate blocks
                            cost, barr = sub_v.cost + opt_b.cost, sub_v.barr | opt_b.barr
                            # Check whether the current subcase is a better sub-solution for state (e_vb, lat, mem)
                            if lat not in DP[e_vb] or mem_v not in DP[e_vb][lat] or cost < DP[e_vb][lat][mem_v].cost:
                                if bidirectional:
                                    # Eliminate prior subcases that are dominated by the new subcase
                                    for l, m in tuple((_l, _m) for _l in DP[e_vb] if _l >= lat
                                                      for _m in DP[e_vb][_l] if (_m[0] >= mem_v[0] and _m[0] >= mem_v[0]
                                                                                 and DP[e_vb][_l][_m].cost >= cost)):
                                        if len(DP[e_vb][l]) > 1:
                                            del DP[e_vb][l][m]
                                        else:
                                            del DP[e_vb][l]
                                # Add superior subcase
                                DP[e_vb][lat][mem_v] = SubLTreePart(cost, sub_v.mul, barr)
        # Cache the best subcase for subtree T_n
        n_w = collections.deque(tree.successors(n), 1).pop() if len(tree.succ[n]) else 0
        # Store the best subcases of subtree T_n
        for lat_n, dp in DP[n, n_w].items():
            TDP[n][lat_n] = min(dp.values(), key=operator.itemgetter(OPT))
    # Subcases under the root node contain the feasible partitioning
    if opt_lat := min(TDP[root], key=lambda _l: TDP[root][_l].cost, default=None):
        opt = TDP[root][opt_lat]
        return recreate_subtree_blocks(tree, opt.barr), opt.cost, opt_lat
    else:
        # No feasible solution
        return INFEASIBLE
