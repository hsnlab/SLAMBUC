#!/usr/bin/env python3.14
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
import json
import pathlib
import re

import pytest
from click import Group
from click.testing import CliRunner

from slambuc.misc.util import get_cplex_path
from slambuc.tool import cli

ANSI_ESC = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')  # Remove bash color sequences

SLAMBUC_ALG_MODULES = {'chain', 'dag', 'ext', 'tree'}


def _get_input_data_filename(cli_args: list[str]) -> pathlib.Path | None:
    match cli_args:
        case 'chain', 'path', *_:
            filename = "chain_test_sequence_serial.npz"
        case 'chain', 'serial', *_:
            filename = "chain_test_sequence_serial.npy"
        case 'dag', *_:
            filename = "graph_test_dag.gml"
        case 'ext', *_:
            filename = "graph_test_tree.gml"
        case 'tree', 'layout', *_:
            filename = "graph_test_tree.gml"
        case 'tree', 'parallel', *_:
            filename = "graph_test_tree_par.gml"
        case 'tree', 'path', *_:
            filename = "graph_test_tree_ser.gml"
        case 'tree', 'serial', *_:
            filename = "graph_test_tree_ser.gml"
        case _:
            return None
    return pathlib.Path(__file__).resolve().parent / "data" / filename


def _generate_test_ids(param):
    match param:
        case list():
            return '/'.join(param)
        case str():
            return f"({param.rsplit('/', maxsplit=1)[-1]})"
        case tuple():
            return param[0].rsplit('=')[-1]
        case _:
            return str(param)


def generate_slambuc_cli_commands():
    cmds = list(cmd for cmd in dir(cli) if cmd.split('__')[0] in SLAMBUC_ALG_MODULES and
                not isinstance(getattr(cli, cmd), Group))
    for cmd in cmds:
        cli_attr = cmd.split('__')
        alg_opt = [p for p in getattr(cli, cmd).params if p.name == 'alg'].pop()
        for alg in (o.name for o in alg_opt.type.choices):
            yield [cli_attr, (f"--alg={alg}",), str(_get_input_data_filename(cli_attr))]


########################################################################################################################

@pytest.mark.parametrize(['cmds', 'params', 'filename'], list(generate_slambuc_cli_commands()), ids=_generate_test_ids)
def test_cli_command(cmds: list[str], params: tuple[str], filename: str):
    runner = CliRunner()
    # noinspection PyTypeChecker
    ret = runner.invoke(cli.main, args=['--json', *cmds, filename, *params], color=True)
    print(ret.output)
    assert ret.exit_code == 0
    result = json.loads(ANSI_ESC.sub('', ret.stdout.strip()))
    feasible = bool(result[0]) if isinstance(result, (tuple, list)) else all(map(bool, (r[0] for r in result)))
    assert feasible is True


def execute_cli_tests():
    for cmds, params, filename in generate_slambuc_cli_commands():
        if not isinstance(params[0], str) or params[0].rsplit('=', maxsplit=1)[-1] in ('cpo', 'cplex'):
            print("Skip test:", cmds)
            continue
        print("Executing test:", '-'.join(map(_generate_test_ids, (cmds, params, filename))))
        test_cli_command(cmds, params, filename)


if __name__ == '__main__':
    execute_cli_tests()
