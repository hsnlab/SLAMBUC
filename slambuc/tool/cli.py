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
import enum
import functools
import importlib
import inspect
import itertools
import json
import math
import os
import pathlib
import sys
import time
import typing

import click
import networkx as nx
import numpy as np

import slambuc
from slambuc.alg import Flavor

GLOBAL_CTX_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_default=True,
    max_content_width=120
)


@click.group('slambuc', context_settings=GLOBAL_CTX_SETTINGS,
             epilog="See https://github.com/hsnlab/SLAMBUC for more details.")
@click.option('-j', '--json', 'format_json', is_flag=True, default=False, help="Output as valid JSON")
@click.option('-s', '--split', 'format_split', is_flag=True, default=False, help="Split results into separate lines")
@click.option('-q', '--quiet', 'output_quiet', is_flag=True, default=False, help="Suppress logging messages")
@click.version_option(slambuc.__version__, "-v", "--version", package_name="slambuc")
@click.pass_context
def main(ctx: click.Context, format_json: bool, format_split: bool, output_quiet: bool):
    """Serverless Layout Adaptation with Memory-Bounds and User Constraints"""
    ctx.ensure_object(dict)
    ctx.obj['FORMAT_JSON'] = format_json
    ctx.obj['FORMAT_SPLIT'] = format_split
    ctx.obj['OUTPUT_QUIET'] = output_quiet


########################################################################################################################


class HalfOpenIntRangeType(click.IntRange):
    """Custom Integer range type that supports positive half-open intervals to infinity"""
    name = "INT"

    def __init__(self):
        super().__init__(min=0, min_open=True, clamp=False)

    def convert(self, value: typing.Any, param: click.Parameter, ctx: click.Context) -> int | float:
        if ((isinstance(value, float) and math.isinf(value)) or
                (isinstance(value, str) and value.lower() == 'inf')):
            return math.inf
        else:
            try:
                return super().convert(value, param, ctx)
            except ValueError:
                self.fail(f"'{value}' is not a valid integer or {math.inf}", param, ctx)


HalfOpenRange = HalfOpenIntRangeType()


class CallGraphPathType(click.Path):
    """Custom Integer range type that supports positive half-open intervals to infinity"""
    name: str = "CALL_GRAPH_FILE"
    supported: tuple[str] = ('gml', 'npy')
    path_type = pathlib.Path

    def __init__(self):
        super().__init__(exists=True, file_okay=True, dir_okay=False, readable=True,
                         resolve_path=True, path_type=self.path_type)

    def convert(self, value: typing.Any, param: click.Parameter, ctx: click.Context) -> path_type:
        if (file_ext := value.rsplit('.', maxsplit=1)[-1]) not in ('gml', 'npy'):
            self.fail(f"Call graph format: {file_ext} is not in the supported format: {self.supported}!", param, ctx)
        return self.path_type(super().convert(value, param, ctx))


CallGraphFile = CallGraphPathType()


class SlambucFlavorType(click.ParamType):
    """Flavor type"""
    name: str = 'Flavor'
    _format = 'mem[int>0],ncore[int>0],cfactor[float>0.0]'

    def convert(self, value: typing.Any, param: click.Parameter, ctx: click.Context) -> Flavor:
        """Parse and convert flavors from CLI inf format <mem[int]>,<ncore[int]>,<cfactor[float]>"""
        print(value, param, ctx)
        if isinstance(value, Flavor):
            return value
        try:
            mem, ncore, cfactor = value.split(',', maxsplit=2)
            _flavor = Flavor(math.inf if mem == 'inf' else int(mem), int(ncore), float(cfactor))
            if not all(metric > 0 for metric in _flavor):
                self.fail(f"Flavor {_flavor} is out of range! Correct format: {self._format}", param, ctx)
            return _flavor
        except ValueError as e:
            self.fail(f"{e}! Correct format: {self._format}", param, ctx)

    def __repr__(self) -> str:
        return self._format


FlavorType = SlambucFlavorType()


def algorithm(enum_type: enum.EnumType, *options) -> typing.Callable:
    """Decorator for common Click arguments and options for algorithm invocation"""

    def wrapped(func):
        func = click.argument('filename', required=True, nargs=1, type=CallGraphFile)(func)
        # parameters = lambda *options: functools.reduce(lambda f, g: lambda x: f(g(x)), reversed(options))
        for param in reversed(options):
            func = param(func)
        func = click.option('--alg', required=False, help="Specific algorithm to be run",
                            type=click.Choice(enum_type, case_sensitive=False),
                            default=enum_type['DEF'])(func)
        return func

    return wrapped


########################################################################################################################

root = click.option('--root', metavar='<NODE_ID>', type=click.INT, required=False, default=1,
                    help="Root node ID of the call graph")
M = click.option('--M', type=HalfOpenRange, required=False, default=math.inf,
                 help="Upper memory bound for blocks")
L = click.option('--L', type=HalfOpenRange, required=False, default=math.inf,
                 help="Latency limit for critical path")
N = click.option('--N', type=HalfOpenRange, required=False, default=1,
                 help="Available vCPU cores for blocks")
cp_end = click.option('--cp_end', metavar='<NODE_ID>', type=click.INT, required=False, show_default='ignore',
                      help="Tail node ID of the critical path")
delay = click.option('--delay', type=HalfOpenRange, required=False, default=1,
                     help="Invocation delay between blocks")
bidirectional = click.option('--bidirectional', metavar='BOOL', type=click.BOOL, required=False,
                             show_default=True, default=True, help="Use bidirectional subcase elimination")
timeout = click.option('--timeout', type=HalfOpenRange, required=False, show_default='ignore',
                       help="ILP solver timeout in seconds")
subchains = click.option('--subchains', metavar='BOOL', type=click.BOOL, required=False,
                         show_default=True, default=False, help="Calculate only subchain blocks (path-tree)")
Epsilon = click.option('--Epsilon', type=click.FloatRange(min=0.0, max=1.0, min_open=True, max_open=False),
                       metavar='FLOAT', required=False, show_default='ignore', help="Weight factor for trimming")
Lambda = click.option('--Lambda', type=click.FloatRange(min=0.0, min_open=False),
                      metavar='FLOAT', required=False, default=0.0, help="Latency factor for trimming")
flavor = click.option('--flavor', 'flavors', type=FlavorType, multiple=True, required=False,
                      default=(Flavor(),), metavar='<mem,ncore,cfactor>', show_default=True,
                      help=f"Resource flavor as a comma-separated tuple")
unit = click.option('--unit', type=HalfOpenRange, required=False, default=1, show_default=True,
                    help="Rounding unit for cost calculation")
only_cuts = click.option('--only_cuts', metavar='BOOL', type=click.BOOL, required=False,
                         show_default=True, default=False, help="Return cuts size instead of latency")
only_barr = click.option('--only_barr', metavar='BOOL', type=click.BOOL, required=False,
                         show_default=True, default=False, help="Return barrier nodes instead of blocks")
full = click.option('--full', metavar='BOOL', type=click.BOOL, required=False,
                    show_default=True, default=True, help="Return full blocks instead of tail nodes")
valid = click.option('--valid', metavar='BOOL', type=click.BOOL, required=False,
                     show_default=True, default=True, help="Return only latency-feasible solution")
exhaustive = click.option('--exhaustive', metavar='BOOL', type=click.BOOL, required=False,
                          show_default=True, default=True, help="Iterate over all topological orderings")
metrics = click.option('--metrics', metavar='BOOL', type=click.BOOL, required=False,
                       show_default=True, default=True, help="Calculate cost/latency metrics explicitly")
k = click.option('--k', type=HalfOpenRange, required=False, default=None, show_default='auto',
                 help="Predefined number of clusters")


########################################################################################################################

@main.group("chain")
def chain():
    """Sequence partitioning algorithms"""
    pass


@chain.group("path")
def chain__path():
    """"""
    pass


@chain__path.command("dp")
def chain__path__dp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@chain__path.command("greedy")
def chain__path__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@chain__path.command("min")
def chain__path__min(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@chain__path.command("sp")
def chain__path__sp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@chain.group("serial")
def chain__serial():
    """"""
    pass


@chain__serial.command("greedy")
def chain__serial__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@chain__serial.command("ilp")
def chain__serial__ilp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@main.group("dag")
def dag():
    """DAG partitioning algorithms"""
    click.get_current_context().obj['INPUT_ARG_REF'] = 'dag'


class DagILPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.dag.ilp`."""
    greedy = "greedy_dag_partitioning"
    dag = "dag_partitioning"
    DEF = dag


@dag.command("ilp")
@algorithm(DagILPType, root, M, L, N, cp_end, delay, subchains, timeout)
def dag__ilp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@main.group("ext")
def ext():
    """External partitioning algorithms and heuristics"""
    click.get_current_context().obj['INPUT_ARG_REF'] = 'tree'


class ExtBaselineType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.ext.baseline`."""
    singleton = "baseline_singleton_partitioning"
    no = "baseline_no_partitioning"
    DEF = singleton


@ext.command("baseline")
@algorithm(ExtBaselineType, root, N, cp_end, delay)
def ext__baseline(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class ExtCSPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.ext.csp`."""
    csp = "csp_tree_partitioning"
    gen = "csp_gen_tree_partitioning"
    DEF = csp


@ext.command("csp")
@algorithm(ExtCSPType, root, flavor, M, L, N, cp_end, delay, exhaustive, timeout)
def ext__csp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class ExtGreedyType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.ext.greedy`."""
    greedy = "min_weight_greedy_partitioning"
    min_weight = "min_weight_partition_heuristic"
    min_lat = "min_lat_partition_heuristic"
    DEF = greedy


@ext.command("greedy")
@algorithm(ExtGreedyType, root, M, L, N, cp_end, delay, metrics)
def ext__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class ExtMinCutType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.ext.min_cut`."""
    chain = "min_weight_chain_decomposition"
    ksplit = "min_weight_ksplit_clustering"
    tree = "min_weight_tree_clustering"
    DEF = tree


@ext.command("min_cut")
@algorithm(ExtMinCutType, root, k, L, N, cp_end, delay, metrics)
def ext__min_cut(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@main.group("tree")
def tree():
    """Tree partitioning algorithms"""
    click.get_current_context().obj['INPUT_ARG_REF'] = 'tree'


@tree.group("layout")
def tree__layout():
    pass


class TreeLayoutILPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.layout.ilp`."""
    hybrid = "tree_gen_hybrid_partitioning"
    mtx = "tree_gen_mtx_partitioning"
    all = "all_gen_tree_mtx_partitioning"
    DEF = mtx


@tree__layout.command("ilp")
@algorithm(TreeLayoutILPType, root, flavor, L, cp_end, subchains, delay, timeout)
def tree__layout__ilp(filename: pathlib.Path, alg: TreeLayoutILPType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@tree.group("parallel")
def tree__parallel():
    pass


class TreeParallelGreedyType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.parallel.greedy`."""
    greedy = "greedy_par_tree_partitioning"
    DEF = greedy


@tree__parallel.command("greedy")
@algorithm(TreeParallelGreedyType, root, M, L, N, cp_end, delay)
def tree__parallel__greedy(filename: pathlib.Path, alg: TreeParallelGreedyType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeParallelILPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.parallel.ilp`."""
    cfg = "tree_par_cfg_partitioning"
    hybrid = "tree_par_hybrid_partitioning"
    mtx = "tree_par_mtx_partitioning"
    all = "all_par_tree_mtx_partitioning"
    DEF = mtx


@tree__parallel.command("ilp")
@algorithm(TreeParallelILPType, root, M, L, N, cp_end, delay, timeout, subchains)
def tree__parallel__ilp(filename: pathlib.Path, alg: TreeParallelILPType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeParallelPseudoType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.parallel.pseudo`."""
    btree = "pseudo_par_btree_partitioning"
    ltree = "pseudo_par_ltree_partitioning"
    DEF = ltree


@tree__parallel.command("pseudo")
@algorithm(TreeParallelPseudoType, root, M, L, N, cp_end, delay, bidirectional)
def tree__parallel__pseudo(filename: pathlib.Path, alg: TreeParallelPseudoType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeParallelPseudoMPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.parallel.pseudo_mp`."""
    ltree = "pseudo_par_mp_ltree_partitioning"
    DEF = ltree


@tree__parallel.command("pseudo_mp")
@algorithm(TreeParallelPseudoMPType, root, M, L, N, cp_end, delay, bidirectional)
def tree__parallel__pseudo_mp(filename: pathlib.Path, alg: TreeParallelPseudoMPType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@tree.group("path")
def tree__path():
    pass


class TreePathGreedyType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.path.greedy`."""
    greedy = "greedy_tree_partitioning"
    DEF = greedy


@tree__path.command("greedy")
@algorithm(TreePathGreedyType, root, M, N, L, cp_end, delay, unit, only_cuts)
def tree__path__greedy(filename: pathlib.Path, alg: TreePathGreedyType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreePathMetaType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.path.greedy`."""
    meta = "meta_tree_partitioning"
    DEF = meta


@tree__path.command("meta")
@algorithm(TreePathMetaType, root, M, N, L, cp_end, delay, unit, only_barr)
def tree__path__meta(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreePathMinType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.path.greedy`."""
    min = "min_tree_partitioning"
    DEF = min


@tree__path.command("min")
@algorithm(TreePathMinType, root, M, N, L, cp_end, delay, unit, full)
def tree__path__min(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreePathSeqType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.path.greedy`."""
    seq = "seq_tree_partitioning"
    DEF = seq


@tree__path.command("seq")
@algorithm(TreePathSeqType, root, M, N, L, cp_end, delay, unit, full)
def tree__path__seq(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreePathSeqStateType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.path.greedy`."""
    cacheless = "cacheless_path_tree_partitioning"
    stateful = "stateful_path_tree_partitioning"
    DEF = stateful


@tree__path.command("seq_state")
@algorithm(TreePathSeqStateType, root, M, N, L, cp_end, delay, valid)
def tree__path__seq_state(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@tree.group("serial")
def tree__serial():
    pass


class TreeSerialBicriteriaType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.serial.bicriteria`."""
    biheuristic = "biheuristic_tree_partitioning"
    bifptas = "bifptas_tree_partitioning"
    dual = "bifptas_dual_tree_partitioning"
    DEF = bifptas


@tree__serial.command("bicriteria")
@algorithm(TreeSerialBicriteriaType, root, M, L, cp_end, delay, Epsilon, Lambda, bidirectional)
def tree__serial__bicriteria(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeSerialGreedyType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.serial.greedy`."""
    greedy = "greedy_ser_tree_partitioning"
    DEF = greedy


@tree__serial.command("greedy")
@algorithm(TreeSerialGreedyType, root, M, L, cp_end, delay)
def tree__serial__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeSerialILPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.serial.ilp`."""
    cfg = "tree_cfg_partitioning"
    hybrid = "tree_hybrid_partitioning"
    mtx = "tree_mtx_partitioning"
    all = "all_tree_mtx_partitioning"
    DEF = mtx


@tree__serial.command("ilp")
@algorithm(TreeSerialILPType, root, M, L, cp_end, delay, subchains, timeout)
def tree__serial__ilp(filename: pathlib.Path, alg: TreeSerialILPType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeSerialILPCplexType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.serial.ilp_cplex`."""
    cpo = "tree_cpo_partitioning"
    cplex = "tree_cplex_partitioning"
    DEF = cplex


@tree__serial.command("ilp_cplex")
@algorithm(TreeSerialILPCplexType, root, M, L, cp_end, delay, timeout)
def tree__serial__ilp_cplex(filename: pathlib.Path, alg: TreeSerialILPCplexType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeSerialPseudoType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.serial.pseudo`."""
    btree = "pseudo_btree_partitioning"
    ltree = "pseudo_ltree_partitioning"
    DEF = ltree


@tree__serial.command("pseudo")
@algorithm(TreeSerialPseudoType, root, M, L, cp_end, delay, bidirectional)
def tree__serial__pseudo(filename: pathlib.Path, alg: TreeSerialPseudoType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


class TreeSerialPseudoMPType(enum.Enum):
    """Partitioning algorithms in `slambuc.alg.tree.serial.pseudo_mp`."""
    btree = "pseudo_mp_btree_partitioning"
    ltree = "pseudo_mp_ltree_partitioning"
    DEF = ltree


@tree__serial.command("pseudo_mp")
@algorithm(TreeSerialPseudoMPType, root, M, L, cp_end, delay, bidirectional)
def tree__serial__pseudo_mp(filename: pathlib.Path, alg: TreeSerialPseudoMPType, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

def log_info(msg: str):
    """Pretty print log message."""
    if not click.get_current_context().obj.get('OUTPUT_QUIET'):
        click.secho(msg, err=True)


def log_err(msg: str):
    """Pretty print error message."""
    if not click.get_current_context().obj.get('OUTPUT_QUIET'):
        click.secho(msg, err=True, fg='red')


def read_input_file(filename: pathlib.Path, arg_name: str):
    """Read input data structure(s) from file."""
    data = None
    match filename.suffix:
        case '.gml':
            data = nx.read_gml(filename, destringizer=int)
        case '.npy':
            data = np.load(filename)
        case _:
            raise click.BadParameter("Unsupported extension! Parameter <filename> must end with .gml or .npy")
    return dict(zip(arg_name, data)) if isinstance(arg_name, (list, tuple)) else {arg_name: data}


def invoke_algorithm(filename: pathlib.Path, alg: str, parameters: dict[str, ...]):
    """Load input data and dynamically invoke partitioning algorithm."""
    ctx = click.get_current_context()
    ##################################
    module_name = f"slambuc.alg.{inspect.currentframe().f_back.f_code.co_name.replace('__', '.')}"
    log_info(f"Importing algorithm: <{alg}> from module: <{module_name}>")
    try:
        module = importlib.import_module(module_name)
        alg_method = getattr(module, alg)
    except AttributeError as e:
        log_err(f"Got unexpected error: {e}")
        raise click.ClickException from e
    ##################################
    log_info(f"Loading input data from file: {filename}")
    data = read_input_file(filename=filename, arg_name=ctx.obj['INPUT_ARG_REF'])
    if not data:
        raise click.ClickException(f"Missing input data!")
    log_info(f"Parsed input:")
    for name, obj in data.items():
        log_info(f"  - {name}: {obj}")
    ##################################
    spec = inspect.getfullargspec(alg_method)
    parameters = {arg: parameters[aa] for arg in spec.args
                  if (aa := arg.lower()) in set(s.lower() for s in parameters) and parameters[aa] is not None}
    log_info(f"Collected explicit algorithm parameters: {parameters}")
    parameters.update(data)
    ##################################
    try:
        log_info(f"Executing partitioning algorithm...")
        _start = time.perf_counter()
        results = alg_method(**parameters)
        _elapsed = (time.perf_counter() - _start) * 1e3
        log_info(f"  -> Algorithm finished successfully in {_elapsed:.6f} ms!")
        metr = list(map(bool, results) if isinstance(results, tuple)
                    else itertools.chain(map(bool, r) for r in results))
        feasible = all(metr if parameters.get('cp_end') else metr[:-1]) if parameters.get('metrics', True) else metr[0]
        log_info(f"Received {'FEASIBLE' if feasible else 'INFEASIBLE'} solution:")
        dumper = functools.partial(json.dumps, indent=None, default=str) if ctx.obj.get('FORMAT_JSON') else repr
        for res in (results if ctx.obj.get('FORMAT_SPLIT') else (results,)):
            click.secho(dumper(res), fg='green' if feasible else 'yellow', bold=True)
    except Exception as e:
        log_err(f"Got unexpected error during execution: {e}")
        raise
    except KeyboardInterrupt:
        log_info("Execution interrupted. Exiting...")
        sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
