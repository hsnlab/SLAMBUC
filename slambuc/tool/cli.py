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

CTX_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_default=True
)


@click.group('slambuc', context_settings=CTX_SETTINGS,
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

    def convert(self, value: str | float, param: click.Option, ctx: click.Context) -> int | float:
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

    def convert(self, value: str | float, param: click.Option, ctx: click.Context) -> path_type:
        if (ext := value.rsplit('.', maxsplit=1)[-1]) not in ('gml', 'npy'):
            self.fail(f"Call graph format: {ext} is not in the supported format: {self.supported}!", param, ctx)
        return self.path_type(super().convert(value, param, ctx))


CallGraphFile = CallGraphPathType()


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

root = click.option("--root", metavar='<NODE>', type=click.INT, required=False, default=1,
                    help="Root node ID of the call graph")
M = click.option("--M", type=HalfOpenRange, required=False, default=math.inf,
                 help="Upper memory bound for blocks")
L = click.option("--L", type=HalfOpenRange, required=False, default=math.inf,
                 help="Latency limit for critical path")
cp_end = click.option("--cp_end", metavar='<NODE>', type=click.INT, required=False, show_default='ignore',
                      help="Tail node ID of the critical path")
delay = click.option("--delay", type=HalfOpenRange, required=False, default=1,
                     help="Invocation delay between blocks")
bidirectional = click.option("--bidirectional", metavar='BOOL', type=click.BOOL, required=False,
                             show_default=True, default=True, help="Use bidirectional subcase elimination")


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
    pass


@dag.command("ilp")
def dag__ilp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@main.group("ext")
def ext():
    """External partitioning algorithms and heuristics"""
    pass


@ext.command("baseline")
def ext__baseline(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@ext.command("csp")
def ext__csp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@ext.command("greedy")
def ext__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@ext.command("min_cut")
def ext__min_cut(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@main.group("tree")
@click.pass_context
def tree(ctx: click.Context):
    """Tree partitioning algorithms"""
    ctx.ensure_object(dict)
    ctx.obj['INPUT_ARG_REF'] = 'tree'


@tree.group("layout")
def tree__layout():
    pass


@tree__layout.command("ilp")
def tree__layout__ilp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@tree.group("parallel")
def tree__parallel():
    pass


@tree__parallel.command("greedy")
def tree__parallel__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__parallel.command("ilp")
def tree__parallel__ilp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__parallel.command("pseudo")
def tree__parallel__pseudo(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__parallel.command("pseudo_mp")
def tree__parallel__pseudo_mp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@tree.group("path")
def tree__path():
    pass


@tree__path.command("greedy")
def tree__path__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__path.command("meta")
def tree__path__meta(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__path.command("min")
def tree__path__min(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__path.command("seq")
def tree__path__seq(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__path.command("seq_state")
def tree__path__seq_state(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


########################################################################################################################

@tree.group("serial")
def tree__serial():
    pass


@tree__serial.command("bicriteria")
def tree__serial__bicriteria(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__serial.command("greedy")
def tree__serial__greedy(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__serial.command("ilp")
def tree__serial__ilp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
    """"""
    invoke_algorithm(filename=filename, alg=alg.value, parameters=parameters)


@tree__serial.command("ilp_cplex")
def tree__serial__ilp_cplex(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
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


@tree__serial.command("pseudo_mp")
def tree__serial__pseudo_mp(filename: pathlib.Path, alg, **parameters: dict[str, ...]):
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
    log_info(f"Importing algorithm: {alg} from module: {module_name}")
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
        feasible = all(map(bool, results))
        log_info(f"Received {'FEASIBLE' if feasible else 'INFEASIBLE'} solution:")
        dumper = functools.partial(json.dumps, indent=None, default=str) if ctx.obj.get('FORMAT_JSON') else repr
        for res in (results if ctx.obj.get('FORMAT_SPLIT') else (results,)):
            click.secho(dumper(res), fg='green' if feasible else 'yellow', bold=True)
    except Exception as e:
        log_err(f"  -> Got unexpected error during execution: {e}")
    except KeyboardInterrupt:
        log_info("Execution interrupted. Exiting...")
        sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
