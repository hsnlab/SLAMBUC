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
from collections.abc import Generator

import networkx as nx
import pulp as lp

from slambuc.alg import LP_LAT, INFEASIBLE, T_RESULTS
from slambuc.alg.service import *
from slambuc.alg.tree.ser.ilp import recreate_subtrees_from_xdict, extract_subtrees_from_xmatrix
from slambuc.alg.util import (ipowerset, par_subtree_memory, ipostorder_dfs, ibacktrack_chain, par_subtree_cost,
                              par_subchain_latency, induced_subtrees, par_inst_count, verify_limits, x_eval)


def ifeasible_par_greedy_subtrees(tree: nx.DiGraph, root: int, M: int, N: int = 1) -> Generator[tuple[int, set[int]]]:
    """
    Generate feasible subtrees in a combinatorial way, which meet the connectivity and memory constraint *M*.

    :param tree:    service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:    root node of the graph
    :param M:       upper memory bound of the partition blocks (in MB)
    :param N:       upper CPU core bound of the partition blocks
    :return:        generator of subtree root and regarding subtree nodes
    """
    for st in ipowerset(tuple(filter(lambda n: n is not PLATFORM, tree)), start=1):
        st = set(st)
        for v in itertools.islice(sorted(st, reverse=True), len(st) - 1):
            if next(tree.predecessors(v)) not in st:
                break
        else:
            if par_subtree_memory(tree, min(st), st, N) <= M:
                yield min(st), st


def ifeasible_par_subtrees(tree: nx.DiGraph, root: int, M: int, N: int = 1) -> Generator[tuple[int, set[int]]]:
    """
    Generate M-feasible(connected) subtrees and roots in a bottom-up way, which meet the memory constraint *M*.

    :param tree:    service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:    root node of the graph
    :param M:       upper memory bound of the partition blocks (in MB)
    :param N:       upper CPU core bound of the partition blocks
    :return:        generator of subtree root and regarding subtree nodes
    """
    subtrees = collections.defaultdict(list)
    for _, n in ipostorder_dfs(tree, root):
        for children in ipowerset(tuple(tree.successors(n))):
            for sts in itertools.product(*(subtrees[c] for c in children)):
                st = {n}.union(*sts)
                if par_subtree_memory(tree, n, st, N) <= M:
                    subtrees[n].append(st)
                    yield n, st
        for c in tree.succ[n]:
            del subtrees[c]


def build_par_tree_cfg_model(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                             N: int = 1, cpath: set[int] = frozenset(), delay: int = 1,
                             isubtrees: iter = ifeasible_par_subtrees) -> tuple[
    lp.LpProblem, dict[int, list[lp.LpVariable]]]:
    """
    Generate the configuration ILP model using parallel metric calculation.

    :return: tuple of the created model and list of decision variables
    """
    # Model
    model = lp.LpProblem(name="Tree_Partitioning", sense=lp.LpMinimize)
    # Decision variables with precalculated coefficients
    c_x, l_x, X_n = [], [], collections.defaultdict(list)
    for i, (b, nodes) in enumerate(isubtrees(tree, root, M, N)):
        # Decision variable for the subtree
        x = lp.LpVariable(f"x_{b:02d}_{i}", cat=lp.LpBinary)
        # Cache block for faster partition recreation
        x.blk = sorted(nodes)
        # Add subtree block cost
        c_x.append(par_subtree_cost(tree, b, nodes, N) * x)
        # Add subtree block latency if required
        if b in cpath:
            st_lat = par_subchain_latency(tree, b, nodes, cpath, N)
            l_x.append((st_lat + delay) * x if b != root else st_lat * x)
        # Cache node coverage of subtree block
        for n in nodes:
            X_n[n].append(x)
    # Objective
    model += lp.lpSum(c_x)
    # Feasibility constraints
    for i, x_i in X_n.items():
        model += lp.lpSum(x_i) == 1, f"Cf_{i:03d}"
    # Latency constraint
    model += lp.lpSum(l_x) <= L if L < math.inf else lp.lpSum(l_x) >= 0, LP_LAT
    return model, X_n


def tree_par_cfg_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                              N: int = 1, cp_end: int = None, delay: int = 1, solver: lp.LpSolver = None,
                              timeout: int = None, **lpargs) -> T_RESULTS:
    """
    Calculate minimal-cost partitioning of a tree based on configuration LP formulation and greedy subcase
    generation.

    Block metrics are calculated based on parallelized execution platform model.

    :param tree:    service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:    root node of the graph
    :param M:       upper memory bound of the partition blocks (in MB)
    :param L:       latency limit defined on the critical path (in ms)
    :param cp_end:  tail node of the critical path in the form of subchain[root -> c_pend]
    :param N:       available CPU core count
    :param delay:   invocation delay between blocks
    :param solver:  specific solver class (default: COIN-OR CBC)
    :param timeout: time limit in sec
    :param lpargs:  additional LP solver parameters
    :return:        tuple of list of best partitions, sum cost of the partitioning, and resulted latency
    """
    # Critical path
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(tree, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    model, X = build_par_tree_cfg_model(tree, root, M, L, N, cpath, delay, isubtrees=ifeasible_par_greedy_subtrees)
    status = model.solve(solver=solver if solver else lp.PULP_CBC_CMD(mip=True, msg=False, timeLimit=timeout, **lpargs))
    if status == lp.LpStatusOptimal:
        opt_cost, opt_lat = lp.value(model.objective), lp.value(model.constraints[LP_LAT])
        return recreate_subtrees_from_xdict(tree, X), opt_cost, L + opt_lat if L < math.inf else opt_lat
    else:
        return INFEASIBLE


def tree_par_hybrid_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                                 N: int = 1, cp_end: int = None, delay: int = 1, solver: lp.LpSolver = None,
                                 timeout: int = None, **lpargs) -> T_RESULTS:
    """
    Calculate minimal-cost partitioning of a tree based on configuration LP formulation and hybrid subcase
    generation.

    Block metrics are calculated based on parallelized execution platform model.

    :param tree:    service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:    root node of the graph
    :param M:       upper memory bound of the partition blocks (in MB)
    :param L:       latency limit defined on the critical path (in ms)
    :param cp_end:  tail node of the critical path in the form of subchain[root -> c_pend]
    :param N:       available CPU core count
    :param delay:   invocation delay between blocks
    :param solver:  specific solver class (default: COIN-OR CBC)
    :param timeout: time limit in sec
    :param lpargs:  additional LP solver parameters
    :return:        tuple of list of best partitions, sum cost of the partitioning, and resulted latency
    """
    # Critical path
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(tree, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    model, X = build_par_tree_cfg_model(tree, root, M, L, N, cpath, delay)
    status = model.solve(solver=solver if solver else lp.PULP_CBC_CMD(mip=True, msg=False, timeLimit=timeout, **lpargs))
    if status == lp.LpStatusOptimal:
        opt_cost, opt_lat = lp.value(model.objective), lp.value(model.constraints[LP_LAT])
        return recreate_subtrees_from_xdict(tree, X), opt_cost, L + opt_lat if L < math.inf else opt_lat
    else:
        return INFEASIBLE


########################################################################################################################

def build_greedy_par_tree_mtx_model(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                                    N: int = 1, cpath: set[int] = frozenset(), subchains: bool = False,
                                    delay: int = 1) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]:
    """
    Generate the matrix ILP model using greedy subcase building and parallel metric calculation.

    :return: tuple of the created model and list of decision variables
    """
    # Model
    model = lp.LpProblem(name="Tree_Partitioning", sense=lp.LpMinimize)
    # Empty decision variable matrix
    X = {j: {} for j in filter(lambda n: n is not PLATFORM, tree)}
    # Objective
    sum_cost = lp.LpAffineExpression()
    for j in X:
        cost_pre = 0
        nodes = set()
        for v in nx.dfs_preorder_nodes(tree, source=j):
            nodes |= {v}
            cost_vj = par_subtree_cost(tree, j, nodes, N)
            X[v][j] = lp.LpVariable(f"x_{v:02d}_{j:02d}", cat=lp.LpBinary) if v != root else 1
            sum_cost += (cost_vj - cost_pre) * X[v][j]
            cost_pre = cost_vj
    model += sum_cost
    # Feasibility constraints
    for i in X:
        model += lp.lpSum(X[i]) == 1, f"Cf_{i:02d}"
    # Knapsack constraints
    for j in X:
        # Cumulative memory demand of prefetched models
        model += lp.lpSum(tree.nodes[i][MEMORY] * X[i][j]
                          for i in nx.dfs_preorder_nodes(tree, source=j)) <= M, f"Ck_{j:02d}"
        r_j = tree[next(tree.predecessors(j))][j][RATE]
        # Operative memory demand of instances running in parallel
        for u, v in nx.dfs_edges(tree, source=j):
            vj_sat = min(math.ceil(tree[u][v][RATE] / r_j), N)
            # Add only non-trivial memory constraint
            if vj_sat > 1:
                model += vj_sat * tree.nodes[v][MEMORY] * X[v][j] <= M, f"Ck_{j:02d}_{v:02d}"
    # Connectivity constraints
    for j in X:
        for u, v in nx.dfs_edges(tree, source=j):
            model += X[u][j] - X[v][j] >= 0, f"Cc_{j:02d}_{u:02d}_{v:02d}"
    # Path-tree constraints
    if subchains:
        for j in X:
            for v in nx.dfs_preorder_nodes(tree, source=j):
                if tree.succ[v]:
                    model += lp.lpSum(X[i][j] for i in tree.successors(v)) <= 1, f"Cp_{j:02d}_{v:02d}"
    # Latency constraint
    sum_lat = lp.LpAffineExpression()
    for j in X:
        if j not in cpath:
            continue
        lat_pre = 0
        nodes = set()
        for v in nx.dfs_preorder_nodes(tree, source=j):
            nodes |= {v}
            # Add subtree block latency if required
            lat_vj = par_subchain_latency(tree, j, nodes, cpath, N)
            sum_lat += (lat_vj - lat_pre) * X[v][j]
            if v == j and j != root:
                sum_lat += delay * X[v][j]
            lat_pre = lat_vj
    if L < math.inf:
        model += sum_lat <= L, LP_LAT
    else:
        # Add redundant constraint to implicitly calculate the latency value
        model += sum_lat >= 0, LP_LAT
    return model, X


def build_par_tree_mtx_model(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                             N: int = 1, cpath: set[int] = frozenset(), subchains: bool = False,
                             delay: int = 1) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]:
    """
    Generate the matrix ILP model based on parallel metric calculations.

    :return: tuple of the created model and list of decision variables
    """
    # Model
    model = lp.LpProblem(name="Tree_Partitioning", sense=lp.LpMinimize)
    # Decision variable matrix with trivial variables
    X = {j: {j: lp.LpVariable(f"x_{j:02d}_{j:02d}", cat=lp.LpBinary) if j != root else 1}
         for j in tree.nodes if j is not PLATFORM}
    # Empty objective
    sum_cost = lp.LpAffineExpression()
    # Empty latency constraint
    sum_lat = lp.LpAffineExpression()
    # Generate decision variables
    for (p, j), st_edges in induced_subtrees(tree, root):
        blk_mem = tree.nodes[j][MEMORY] * X[j][j]
        # Add coefficients for single node block [j]
        r_j, d_j, t_j = tree[p][j][RATE], tree[p][j][DATA], tree.nodes[j][RUNTIME]
        sum_cost += (r_j * (d_j + t_j) + sum(par_inst_count(r_j, js[RATE], N) * js[DATA]
                                             for js in tree.succ[j].values())) * X[j][j]
        if j in cpath:
            jc = next(filter(lambda c: c in cpath, tree.successors(j)), None)
            sum_lat += (d_j + t_j + (math.ceil(tree[j][jc][RATE] / (r_j * N)) * tree[j][jc][DATA]
                                     if jc else 0)) * X[j][j]
            if j != root:
                sum_lat += delay * X[j][j]
        # Cache instance factor for nodes in cpath
        n_v = 1
        # Candidate nodes for block_j
        for u, v in st_edges:
            X[v][j] = lp.LpVariable(f"x_{v:02d}_{j:02d}", cat=lp.LpBinary)
            blk_mem += tree.nodes[v][MEMORY] * X[v][j]
            # Add coefficients for merging single node v to block [j,...]
            r_v, d_v, t_v = tree[u][v][RATE], tree[u][v][DATA], tree.nodes[v][RUNTIME]
            # sum_cost += (r_v * (t_v - d_v) + sum(vs[RATE] * vs[DATA] for vs in tree.succ[v].values())) * X[v][j]
            sum_cost += ((par_inst_count(r_j, r_v, N) * (t_v - d_v) +
                          sum(par_inst_count(r_j, vs[RATE], N) * vs[DATA] for vs in tree.succ[v].values()))) * X[v][j]
            # u -> v edge on cpath
            if v in cpath:
                n_v *= math.ceil(r_v / (tree[next(tree.predecessors(u))][u][RATE] * N))
                vc = next(filter(lambda c: c in cpath, tree.successors(v)), None)
                w_v = math.ceil(tree[v][vc][RATE] / (r_v * N)) * tree[v][vc][DATA] if vc else 0
                sum_lat += n_v * (t_v - d_v + w_v) * X[v][j]
            # Add knapsack constraint for operative memory demand
            vj_sat = min(math.ceil(tree[u][v][RATE] / r_j), N)
            # Add only non-trivial memory constraint
            if vj_sat > 1:
                model += vj_sat * tree.nodes[v][MEMORY] * X[v][j] <= M, f"Ck2_{j:02d}_{v:02d}"
            # Connectivity constraint
            model += X[u][j] - X[v][j] >= 0, f"Cc_{j:02d}_{u:02d}_{v:02d}"
        # Knapsack constraint, X[l][l] <= M for each leaf node l can be omitted
        if len(blk_mem) > 1:
            model += blk_mem <= M, f"Ck_{j:02d}"
    # Objective
    model += sum_cost
    # Feasibility constraints, X[root][root] = 1 can be omitted else it ensures that X[root][root] must be 1
    for i in filter(lambda x: x != root, X):
        model += lp.lpSum(X[i].values()) == 1, f"C_f{i:02d}"
    # Path-tree constraints
    if subchains:
        for pt in ((lp.lpSum(X[i][j] for i in tree.successors(v)) <= 1, f"Cp_{j:02d}_{v:02d}")
                   for v in X for j in X[v] if tree.succ[v]):
            model += pt
    # Latency constraint
    if L < math.inf:
        model += sum_lat <= L, LP_LAT
    else:
        # Add redundant constraint to implicitly calculate the latency value
        model += sum_lat >= 0, LP_LAT
    return model, X


def tree_par_mtx_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                              N: int = 1, cp_end: int = None, delay: int = 1, subchains: bool = False,
                              solver: lp.LpSolver = None, timeout: int = None, **lpargs) -> T_RESULTS:
    """
    Calculate minimal-cost partitioning of a tree based on matrix LP formulation.

    Block metrics are calculated based on parallelized execution platform model.

    :param tree:        service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:        root node of the graph
    :param M:           upper memory bound of the partition blocks (in MB)
    :param L:           latency limit defined on the critical path (in ms)
    :param N:           available CPU  core count
    :param cp_end:      tail node of the critical path in the form of subchain[root -> c_pend]
    :param subchains:   only subchain blocks are considered (path-tree)
    :param delay:       invocation delay between blocks
    :param solver:      specific solver class (default: COIN-OR CBC)
    :param timeout:     time limit in sec
    :param lpargs:      additional LP solver parameters
    :return:            tuple of list of best partitions, sum cost of the partitioning, and resulted latency
    """
    # Critical path
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(tree, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    model, X = build_par_tree_mtx_model(tree, root, M, L, N, cpath, subchains, delay)
    status = model.solve(solver=solver if solver else lp.PULP_CBC_CMD(mip=True, msg=False, timeLimit=timeout, **lpargs))
    if status == lp.LpStatusOptimal:
        opt_cost, opt_lat = round(lp.value(model.objective), 0), round(lp.value(model.constraints[LP_LAT]), 0)
        return extract_subtrees_from_xmatrix(X), opt_cost, L + opt_lat if L < math.inf else opt_lat
    else:
        return INFEASIBLE


########################################################################################################################


def all_par_tree_mtx_partitioning(tree: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                                  N: int = 1, cp_end: int = None, delay: int = 1, subchains: bool = False,
                                  solver: lp.LpSolver = None, timeout: int = None, **lpargs) -> list[T_RESULTS]:
    """
    Calculate all minimal-cost partitioning variations of a tree based on matrix ILP formulation.

    :param tree:        service graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:        root node of the graph
    :param M:           upper memory bound of the partition blocks (in MB)
    :param L:           latency limit defined on the critical path (in ms)
    :param N:           available CPU  core count
    :param cp_end:      tail node of the critical path in the form of subchain[root -> c_pend]
    :param subchains:   only subchain blocks are considered (path-tree)
    :param delay:       invocation delay between blocks
    :param solver:      specific solver class (default: COIN-OR CBC)
    :param timeout:     time limit in sec
    :param lpargs:      additional LP solver parameters
    :return:            tuple of list of best partitions, sum cost of the partitioning, and resulted latency
    """
    # Critical path
    cpath = set(ibacktrack_chain(tree, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(tree, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    # Get model
    model, X = build_par_tree_mtx_model(tree, root, M, L, N, cpath, subchains, delay)
    # Init for min-cost results
    results, min_cost = [], math.inf
    solver = solver if solver else lp.PULP_CBC_CMD(mip=True, msg=False, timeLimit=timeout, **lpargs)
    # Iterate over the optimal solutions
    while model.solve(solver) == lp.LpStatusOptimal:
        opt_cost, opt_lat = round(model.objective.value(), 0), round(model.constraints[LP_LAT].value(), 0)
        # If solution is not min-cost then exit else store the min-cost solution
        if min_cost < opt_cost:
            break
        else:
            min_cost = opt_cost
        results.append((extract_subtrees_from_xmatrix(X), opt_cost, L + opt_lat if L < math.inf else opt_lat))
        # Collect barrier nodes of the current optimal solution
        barr = [j for j in X if x_eval(X[j][j])]
        # Add extra constraint for excluding the current set of barrier nodes
        model += lp.lpSum(X[j][j] for j in barr) <= len(barr) - 1, f"Ca_{'_'.join(map(str, barr))}"
    # Return min-cost solutions
    return results if results else [INFEASIBLE]
