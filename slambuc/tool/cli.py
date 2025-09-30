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
import click


@click.group("slambuc")
def main():
    """Serverless Layout Adaptation with Memory-Bounds and User Constraints"""
    pass


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
def chain__path__dp():
    """"""
    pass


@chain__path.command("greedy")
def chain__path__greedy():
    """"""
    pass


@chain__path.command("min")
def chain__path__min():
    """"""
    pass


@chain__path.command("sp")
def chain__path__sp():
    """"""
    pass


########################################################################################################################

@chain.group("serial")
def chain__serial():
    """"""
    pass


@chain__serial.command("greedy")
def chain__serial__greedy():
    """"""
    pass


@chain__serial.command("ilp")
def chain__serial__ilp():
    """"""
    pass


########################################################################################################################

@main.group("dag")
def dag():
    """Partitioning algorithms working on DAGs"""
    pass


@dag.command("ilp")
def dag__ilp():
    """"""
    pass


########################################################################################################################

@main.group("ext")
def ext():
    """Partitioning algorithms based on external tools"""
    pass


@ext.command("baseline")
def ext__baseline():
    """"""
    pass


@ext.command("csp")
def ext__csp():
    """"""
    pass


@ext.command("greedy")
def ext__greedy():
    """"""
    pass


@ext.command("min_cut")
def ext__min_cut():
    """"""
    pass


########################################################################################################################

@main.group("tree")
def tree():
    """Tree partitioning algorithms"""
    pass


@tree.group("layout")
def tree__layout():
    pass


@tree__layout.command("ilp")
def tree__layout__ilp():
    """"""
    pass


########################################################################################################################

@tree.group("parallel")
def tree__parallel():
    pass


@tree__parallel.command("greedy")
def tree__parallel__greedy():
    """"""
    pass


@tree__parallel.command("ilp")
def tree__parallel__ilp():
    """"""
    pass


@tree__parallel.command("pseudo")
def tree__parallel__pseudo():
    """"""
    pass


@tree__parallel.command("pseudo_mp")
def tree__parallel__pseudo_mp():
    """"""
    pass


########################################################################################################################

@tree.group("path")
def tree__path():
    pass


@tree__path.command("greedy")
def tree__path__greedy():
    """"""
    pass


@tree__path.command("meta")
def tree__path__meta():
    """"""
    pass


@tree__path.command("min")
def tree__path__min():
    """"""
    pass


@tree__path.command("seq")
def tree__path__seq():
    """"""
    pass


@tree__path.command("seq_state")
def tree__path__seq_state():
    """"""
    pass


########################################################################################################################

@tree.group("serial")
def tree__serial():
    pass


@tree__serial.command("bicriteria")
def tree__serial__bicriteria():
    """"""
    pass


@tree__serial.command("greedy")
def tree__serial__greedy():
    """"""
    pass


@tree__serial.command("ilp")
def tree__serial__ilp():
    """"""
    pass


@tree__serial.command("ilp_cplex")
def tree__serial__ilp_cplex():
    """"""
    pass


@tree__serial.command("pseudo")
def tree__serial__pseudo():
    """"""
    pass


@tree__serial.command("pseudo_mp")
def tree__serial__pseudo_mp():
    """"""
    pass


########################################################################################################################

if __name__ == "__main__":
    main()
