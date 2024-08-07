# Copyright 2024 Janos Czentye
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

import networkx as nx
import pulp as lp

from slambuc.alg import LP_LAT, INFEASIBLE, T_RESULTS
from slambuc.alg.app import *
from slambuc.alg.tree.serial.ilp import extract_subtrees_from_xmatrix
from slambuc.alg.util import (par_inst_count, ibacktrack_chain, verify_limits, par_subchain_latency,
                              iclosed_subgraph, par_subgraph_cost)


def build_greedy_dag_mtx_model(dag: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                               N: int = 1, cpath: set[int] = frozenset(), delay: int = 1,
                               path_tree: bool = False) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]:
    """
    Generate the matrix ILP model using greedy subcase building and parallel metric calculation.

    :return: tuple of the created model and list of decision variables
    """
    # Model
    model = lp.LpProblem(name="DAG_Partitioning", sense=lp.LpMinimize)
    # Empty decision variable matrix
    X = {j: {} for j in filter(lambda n: n is not PLATFORM, dag)}
    # Objective
    sum_cost = lp.LpAffineExpression()
    for j in X:
        cost_pre = 0
        nodes = set()
        for v in iclosed_subgraph(dag, source=j):
            nodes |= {v}
            cost_vj = par_subgraph_cost(dag, j, nodes, N)
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
        model += lp.lpSum(dag.nodes[i][MEMORY] * X[i][j] for i in X if j in X[i]) <= M, f"Ck_{j:02d}"
        R_j = sum(dag[p][j][RATE] for p in dag.predecessors(j))
        # Operative memory demand of instances running in parallel
        for v in iclosed_subgraph(dag, source=j):
            vj_sat = min(math.ceil(sum(dag[p][v][RATE] for p in dag.predecessors(v)) / R_j), N)
            # Add only non-trivial memory constraint
            if vj_sat > 1:
                model += vj_sat * dag.nodes[v][MEMORY] * X[v][j] <= M, f"Ck_{j:02d}_{v:02d}"
    # Connectivity constraints
    for j in X:
        for v in iclosed_subgraph(dag, source=j, inclusive=False):
            for u in dag.predecessors(v):
                model += X[u][j] - X[v][j] >= 0, f"Cc_{j:02d}_{u:02d}_{v:02d}"
    # Path-tree constraints
    if path_tree:
        for j in X:
            for v in iclosed_subgraph(dag, source=j):
                model += lp.lpSum(X[s][j] for s in dag.successors(v) if j in X[s]) <= 1, f"Cpp_{j:02d}_{v:02d}"
    # Latency constraint
    sum_lat = lp.LpAffineExpression()
    for j in X:
        if j not in cpath:
            continue
        lat_pre = 0
        nodes = set()
        for v in iclosed_subgraph(dag, source=j):
            nodes |= {v}
            # Add subtree block latency if required
            lat_vj = par_subchain_latency(dag, j, nodes, cpath, N)
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


def greedy_dag_partitioning(dag: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                            N: int = 1, cp_end: int = None, delay: int = 1, path_tree: bool = False,
                            solver: lp.LpSolver = None, timeout: int = None, **lpargs) -> T_RESULTS:
    """
    Calculate minimal-cost partitioning of a tree based on matrix LP formulation.

    Block metrics are calculated based on a parallelized execution platform model.

    :param dag:         app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:        root node of the graph
    :param M:           upper memory bound of the partition blocks (in MB)
    :param L:           latency limit defined on the critical path (in ms)
    :param N:           available CPU  core count
    :param cp_end:      tail node of the critical path in the form of subchain[root -> c_pend]
    :param delay:       invocation delay between blocks
    :param path_tree:   only subchain blocks are considered (path-tree)
    :param solver:      specific solver class (default: COIN-OR CBC)
    :param timeout:     time limit in sec
    :param lpargs:      additional LP solver parameters
    :return:            tuple of list of best partitions, sum cost of the partitioning, and resulted latency
    """
    # Critical path
    cpath = set(ibacktrack_chain(dag, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(dag, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    model, X = build_greedy_dag_mtx_model(dag, root, M, L, N, cpath, delay, path_tree)
    status = model.solve(solver=solver if solver else lp.PULP_CBC_CMD(mip=True, msg=False, timeLimit=timeout, **lpargs))
    if status == lp.LpStatusOptimal:
        opt_cost, opt_lat = round(lp.value(model.objective), 0), round(lp.value(model.constraints[LP_LAT]), 0)
        return extract_subtrees_from_xmatrix(X), opt_cost, L + opt_lat if L < math.inf else opt_lat
    else:
        return INFEASIBLE


########################################################################################################################

def build_dag_mtx_model(dag: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                        N: int = 1, cpath: set[int] = frozenset(), delay: int = 1,
                        path_tree: bool = False) -> tuple[lp.LpProblem, dict[int, dict[int, lp.LpVariable]]]:
    """
    Generate the matrix ILP model based on parallel metric calculations.

    :return: tuple of the created model and list of decision variables
    """
    # Model
    model = lp.LpProblem(name="DAG_Partitioning", sense=lp.LpMinimize)
    # Decision variable matrix with trivial variables
    X = {j: {j: lp.LpVariable(f"x_{j:02d}_{j:02d}", cat=lp.LpBinary) if j != root else 1}
         for j in dag.nodes if j is not PLATFORM}
    # Empty objective
    sum_cost = lp.LpAffineExpression()
    # Empty latency constraint
    sum_lat = lp.LpAffineExpression()
    # Generate decision variables
    for j in X:
        blk_mem = dag.nodes[j][MEMORY] * X[j][j]
        # Add coefficients for single node block [j]
        R_j = sum(dag[p][j][RATE] for p in dag.predecessors(j))
        D_j = sum(dag[p][j][RATE] * dag[p][j][DATA] for p in dag.predecessors(j))
        t_j = dag.nodes[j][RUNTIME]
        sum_cost += (D_j + R_j * t_j
                     + sum(par_inst_count(R_j, dag[j][js][RATE], N) * dag[j][js][DATA]
                           for js in dag.successors(j))) * X[j][j]
        if j in cpath:
            jp = next(filter(lambda _p: _p in cpath or _p is PLATFORM, dag.predecessors(j)), None)
            jc = next(filter(lambda _c: _c in cpath, dag.successors(j)), None)
            sum_lat += (dag[jp][j][DATA] + t_j
                        + (math.ceil(dag[j][jc][RATE] / (dag[jp][j][RATE] * N)) * dag[j][jc][DATA]
                           if jc else 0)) * X[j][j]
            if j != root:
                sum_lat += delay * X[j][j]
        # Cache instance factor for nodes in cpath
        n_v = 1
        # Candidate nodes for block_j
        for v in iclosed_subgraph(dag, source=j, inclusive=False):
            X[v][j] = lp.LpVariable(f"x_{v:02d}_{j:02d}", cat=lp.LpBinary)
            blk_mem += dag.nodes[v][MEMORY] * X[v][j]
            # Add coefficients for merging single node v to block [j,...]
            t_v = dag.nodes[v][RUNTIME]
            R_v = sum(dag[p][v][RATE] for p in dag.predecessors(v))
            # sum_cost += (r_v * (t_v - d_v) + sum(vs[RATE] * vs[DATA] for vs in tree.succ[v].values())) * X[v][j]
            sum_cost += ((par_inst_count(R_j, R_v, N) * t_v
                          - sum(par_inst_count(R_j, dag[vp][v][RATE], N) * dag[vp][v][DATA]
                                for vp in dag.predecessors(v))
                          + sum(par_inst_count(R_j, dag[v][vs][RATE], N) * dag[v][vs][DATA]
                                for vs in dag.successors(v)))) * X[v][j]
            # u -> v edge on cpath
            if v in cpath:
                vp = next(filter(lambda _p: _p in cpath, dag.predecessors(v)), None)
                vpp = next(filter(lambda _p: _p in cpath or _p is PLATFORM, dag.predecessors(vp)), None)
                n_v *= math.ceil(dag[vp][v][RATE] / (dag[vpp][vp][RATE] * N))
                vc = next(filter(lambda _c: _c in cpath, dag.successors(v)), None)
                w_v = math.ceil(dag[v][vc][RATE] / (dag[vp][v][RATE] * N)) * dag[v][vc][DATA] if vc else 0
                sum_lat += n_v * (t_v - dag[vp][v][DATA] + w_v) * X[v][j]
            # Add knapsack constraint for operative memory demand
            vj_sat = min(math.ceil(R_v / R_j), N)
            # Add only non-trivial memory constraint
            if vj_sat > 1:
                model += vj_sat * dag.nodes[v][MEMORY] * X[v][j] <= M, f"Ck2_{j:02d}_{v:02d}"
            # Connectivity constraint
            for u in dag.predecessors(v):
                if j in X[u]:
                    model += X[u][j] - X[v][j] >= 0, f"Cc_{j:02d}_{u:02d}_{v:02d}"
        # Knapsack constraint, X[l][l] <= M for each leaf node l can be omitted
        if len(blk_mem) > 1:
            model += blk_mem <= M, f"Ck_{j:02d}"
    # Path-tree constraints
    if path_tree:
        for j in X:
            for v in iclosed_subgraph(dag, source=j):
                model += lp.lpSum(X[s][j] for s in dag.successors(v) if j in X[s]) <= 1, f"Cpp_{j:02d}_{v:02d}"
    # Objective
    model += sum_cost
    # Feasibility constraints, X[root][root] = 1 can be omitted else it ensures that X[root][root] must be 1
    for i in filter(lambda x: x != root, X):
        model += lp.lpSum(X[i].values()) == 1, f"Cf_{i:02d}"
    # Latency constraint
    if L < math.inf:
        model += sum_lat <= L, LP_LAT
    else:
        # Add redundant constraint to implicitly calculate the latency value
        model += sum_lat >= 0, LP_LAT
    return model, X


def dag_partitioning(dag: nx.DiGraph, root: int = 1, M: int = math.inf, L: int = math.inf,
                     N: int = 1, cp_end: int = None, delay: int = 1, path_tree: bool = False,
                     solver: lp.LpSolver = None, timeout: int = None, **lpargs) -> T_RESULTS:
    """
    Calculate minimal-cost partitioning of a tree based on matrix LP formulation.

    Block metrics are calculated based on a parallelized execution platform model.

    :param dag:        app graph annotated with node runtime(ms), memory(MB) and edge rates and data overheads(ms)
    :param root:        root node of the graph
    :param M:           upper memory bound of the partition blocks (in MB)
    :param L:           latency limit defined on the critical path (in ms)
    :param N:           available CPU  core count
    :param cp_end:      tail node of the critical path in the form of subchain[root -> c_pend]
    :param delay:       invocation delay between blocks
    :param path_tree:   only subchain blocks are considered (path-tree)
    :param solver:      specific solver class (default: COIN-OR CBC)
    :param timeout:     time limit in sec
    :param lpargs:      additional LP solver parameters
    :return:            tuple of list of best partitions, sum cost of the partitioning, and resulted latency
    """
    # Critical path
    cpath = set(ibacktrack_chain(dag, root, cp_end))
    # Verify the min values of limits for a feasible solution
    if not all(verify_limits(dag, cpath, M, L)):
        # No feasible solution due to too strict limits
        return INFEASIBLE
    model, X = build_dag_mtx_model(dag, root, M, L, N, cpath, delay, path_tree)
    status = model.solve(solver=solver if solver else lp.PULP_CBC_CMD(mip=True, msg=False, timeLimit=timeout, **lpargs))
    if status == lp.LpStatusOptimal:
        opt_cost, opt_lat = round(lp.value(model.objective), 0), round(lp.value(model.constraints[LP_LAT]), 0)
        return extract_subtrees_from_xmatrix(X), opt_cost, L + opt_lat if L < math.inf else opt_lat
    else:
        return INFEASIBLE
