#!/usr/bin/env python3.11
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
import enum

import click

from tests import *
from validation.generate_test_data import MAX_INST, MAX_TREE_SIZE


class PERF(enum.StrEnum):
    """Options for performance tests"""
    SER = "ser"
    PAR = "par"


class SENS(enum.StrEnum):
    """Options for sensitivity tests"""
    MEM = "mem"
    LAT = "lat"
    CPU = "cpu"
    EPS = "eps"
    LAMBDA = "lambda"
    BICRIT = "bicrit"


class COST(enum.StrEnum):
    """Options for cost tests"""
    SER = "ser"
    PAR = "par"


class TREE(enum.StrEnum):
    """Options for tree types"""
    RAND = "rand"
    RANDOM = "random"
    JOB = "job"
    FAAS = "faas"


@click.group("Tests")
def main():
    pass


@main.command(help="Execute performance tests")
@click.option("-a", "--alg", type=click.Choice(PERF.__members__.values()), required=True, help="Alg type")
@click.option("-n", "--size", "n", type=click.IntRange(10, MAX_TREE_SIZE), required=True, help="Tree size")
@click.option("-d", "--data", "data_dir", type=str, default=DATA_DIR, help="Data directory")
@click.option("-i", "--instance", type=click.IntRange(1, MAX_INST), default=None, help="Tree instance num.")
@click.option("-t", "--timeout", type=click.IntRange(min=0), default=DEF_TIMEOUT, help="Timeout")
def perf(alg: str, n: int, data_dir: str, instance: int, timeout: int):
    match PERF(alg):
        case PERF.SER:
            perform_tree_size_ser_tests(n=n, data_dir=data_dir, tree_num=instance, timeout=timeout)
        case PERF.PAR:
            perform_tree_size_par_tests(n=n, data_dir=data_dir, tree_num=instance, timeout=timeout)
        case _:
            print("Invalid alg. type:", alg)


class TestValuesParamType(click.ParamType):
    name = "Comma-sep values"

    def convert(self, value, param, ctx):
        if value is not None:
            try:
                value = tuple(float(v) for v in value.split(','))
            except ValueError:
                self.fail(f"{value:r} is not valid list of parameters separated with comma(,) !", param, ctx)
        return value


@main.command(help="Execute sensitivity tests")
@click.option("-a", "--attr", type=click.Choice(SENS.__members__.values()), required=True, help="Attr type")
@click.option("-n", "--size", "n", type=click.IntRange(10, MAX_TREE_SIZE), required=True, help="Tree size")
@click.option("-d", "--data", "data_dir", type=str, default=DATA_DIR, help="Data directory")
@click.option("-i", "--instance", type=click.IntRange(1, MAX_INST), default=None, help="Tree instance num.")
@click.option("-v", "--value", type=TestValuesParamType(), default=None, help="Comma-separated attr values")
@click.option("-t", "--timeout", type=click.IntRange(min=0), default=DEF_TIMEOUT, help="Timeout")
def sens(attr: str, n: int, data_dir: str, instance: int, timeout: int, value: str):
    match SENS(attr):
        case SENS.MEM:
            perform_mem_sens_tests(n=n, data_dir=data_dir, tree_num=instance, value=value, timeout=timeout)
        case SENS.LAT:
            perform_lat_sens_tests(n=n, data_dir=data_dir, tree_num=instance, value=value, timeout=timeout)
        case SENS.CPU:
            perform_cpu_sens_tests(n=n, data_dir=data_dir, tree_num=instance, value=value, timeout=timeout)
        case SENS.EPS:
            perform_epsilon_sens_tests(n=n, data_dir=data_dir, tree_num=instance, value=value, timeout=timeout)
        case SENS.LAMBDA:
            perform_lambda_sens_tests(n=n, data_dir=data_dir, tree_num=instance, value=value, timeout=timeout)
        case SENS.BICRIT:
            perform_bicriteria_sens_tests(n=n, data_dir=data_dir, tree_num=instance, value=value, timeout=timeout)
        case _:
            print("Invalid attr. type", attr)


@main.command(help="Execute cost tests")
@click.option("-n", "--size", "n", type=int, required=True, help="Tree size pattern")
@click.option("-a", "--tree", "tree", type=click.Choice(TREE.__members__.values()), default=None, help="Tree type")
@click.option("-d", "--data", "data_dir", type=str, default=DATA_DIR, help="Data directory")
@click.option("-i", "--instance", type=click.IntRange(1, MAX_INST), default=None, help="Tree instance num.")
@click.option("-t", "--timeout", type=click.IntRange(min=0), default=DEF_TIMEOUT, help="Timeout")
def cost(n: int, tree: str, data_dir: str, instance: int, timeout: int):
    perform_cost_tests(size_pattern=n, tree_type=tree, data_dir=data_dir, tree_num=instance, timeout=timeout)


if __name__ == '__main__':
    main()
