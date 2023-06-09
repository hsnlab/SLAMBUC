# Serverless Layout Adaptation with Memory-Bounds and User Constraints (SLAMBUC)

![PyPI](https://img.shields.io/pypi/v/SLAMBUC)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/SLAMBUC)
![PyPI - License](https://img.shields.io/pypi/l/SLAMBUC)
![Algorithm tests](https://github.com/hsnlab/SLAMBUC/actions/workflows/python-alg-tests.yml/badge.svg?branch=main)


Collection of graph partitioning algorithms implemented in Python for composing cloud-native
applications from standalone serverless functions in a cost-efficient and latency-constrained manner.

## Overview

In the context of serverless computing, function fusion is a novel, high-level approach to improve
performance and at the same time reduce the operational cost of serverless applications consisting
of stateless, ephemeral functions. This is achieved by grouping, encompassing, and assembling connected
FaaS functions into separate composite components representing the deployable software artifacts that
are provisioned by the serverless frameworks in the same way as other single functions.
In addition, different user-defined Quality of Service (QoS) constraints should be also taken into
account, e.g., overall response time of the application or an end-to-end latency constraint on the critical 
path in the application's call graph.

Under the hood, this problem can be formalized as the partitioning of the application call graph (DAG)
into disjoint, connected subgraphs in a cost-efficient manner, while specific requirements imposed by
the user and the platform (flavors) itself need to be satisfied.

In this package, we designed, implemented, and collected various partitioning algorithms tailored to
tree-shape serverless applications with different runtime complexity, considering communication
parameters and requirements. Our main objective is to find the cost-optimal grouping of functions 
concerning node and edge-weighted trees and cost/memory/latency models based on public cloud frameworks,
whereas each flavor imposes an upper limit on the available operative memory.
Moreover, a user-given latency constraint has to be fulfilled on the tree's critical path, which is
defined as the subchain between the first/front-end function and a predefined leaf node.

## Installation

### Environment

Our implementations require Python3.10 or above. The following code snippet can be used to set up the 
latest Python environment on Ubuntu.

```bash
sudo add-apt-repository -y 'ppa:deadsnakes/ppa' && sudo apt update
sudo apt install python3.11-dev python3.11-dev
sudo curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.11
```

### SLAMBUC package

The easiest way to get our algorithms collected in [SLAMBUC](slambuc) is to install the package from
[PyPI repository](https://pypi.org/project/SLAMBUC/).

```bash
python3.11 -m pip install slambuc
```

However, for the latest changes, it can be installed directly from GitHub as follows.

```bash
python3.11 -m pip install --no-cache-dir git+https://github.com/hsnlab/SLAMBUC.git
```

Tree plotting relies on networkx's internal plotting feature that generates a layout based on the
[graphviz tool and its python frontend](https://pygraphviz.github.io/documentation/stable/install.html).
Thus, in that case, the related dependencies must be installed first.

```bash
sudo apt-get install graphviz graphviz-dev
python3.11 -m pip install pygraphviz
```

External solvers can also be used in LP-based algorithms that require the given solver packages to be
preinstalled and available for the [PuLP frontend](https://github.com/coin-or/pulp). Currently,
the following solvers are tested.

* CBC (default)
* GLPK (see installation [here](https://coin-or.github.io/pulp/main/installing_pulp_at_home.html#linux-installation))
* CPLEX ([installation](https://www.ibm.com/products/ilog-cplex-optimization-studio)
  and [setup](https://coin-or.github.io/pulp/guides/how_to_configure_solvers.html#cplex))

It is worth noting that CPLEX's python wrapper [docplex](https://pypi.org/project/docplex/)
(as a replacement for PuLP) is left behind the latest Python version. For using this API, requirements
are prepared separately for **Python3.10**.

```bash
python3.10 -m pip install -U -r requirements_py3.10.txt
```

For solving constrained shortest path problems (CSP), we apply solution methods from
[cspy](https://github.com/torressa/cspy).

### Test harness and performance validation

Our repository contains separate test scripts under the [tests](tests) folder for validating the 
input/output formats and call parameters. These codes also serve as examples for using the different 
implementations of our package.

For comparative analyses, we also implemented a test harness under [validation](validation)
to automatize test executions with generated test input graphs from [validation/data](validation/data)
and monitor elapsed time and memory demands of tested algorithms initiated as separate sub-processes.

To install additional dependencies, run the following commands.

```bash
python3.11 -m pip install slambuc[tests]      # For executing tests
python3.11 -m pip install slambuc[validation] # For using our test harness framework
```

## Package structure

* [slambuc](slambuc) - [Main package]
    * [alg](slambuc/alg) - [algorithms]
        * [chain](slambuc/alg/chain) - [Single Chain Partitioning]
            * [dp](slambuc/alg/chain/dp) - [dynamic programming]
            * [ser](slambuc/alg/chain/ser) - [linear programming]
        * [ext](slambuc/alg/ext) - [External algorithms and Baselines]
        * [service](slambuc/alg/service) - [Service Properties]
        * [tree](slambuc/alg/tree) - [Tree Partitioning]
            * [dp](slambuc/alg/tree/dp) - [chain-based algorithms]
            * [layout](slambuc/alg/tree/layout) - [general partitioning]
            * [par](slambuc/alg/tree/par) - [parallel executions models]
            * [ser](slambuc/alg/tree/ser) - [serialized execution models]
    * [gen](slambuc/gen) - [Input Generators]
        * [cluster](slambuc/gen/cluster) - [data-parallel job trees]
        * [microservice](slambuc/gen/microservice) - [serverless trees]
        * [random](slambuc/gen/random) - [random trees]
    * [misc](slambuc/misc) - [Miscellaneous utility codes]
* [tests](tests) - [tests]
* [validation](validation) - [Validation Framework]
    * [data](validation/data) - [generated test data]
    * [results](validation/results) - [measured result files]

## Usage

Refer to the wiki for [formats, execution parameters, and examples](https://github.com/hsnlab/SLAMBUC/wiki).

## Example

Validation results of a subset of our algorithms with a fully-serialized block execution model,
which are executed with our [validation script](tests/validate_algs.py) using different configurations 
and a [random-generated input call graph](tests/data/graph_test_tree_ser.gml) of size 10.

Used algorithmic parameters (if applicable):
  * Root node ID (root): 1
  * Memory limit (M): 6
  * Available vCPU count (N): 1
  * Critical path's end node ID (cp_end): 10 
  * Latency limit: (L): inf
  * Platform delay: (delay): 10
  * Bidirectional elimination (bidirectional): True
  * Cost approximation ratio (Epsilon): 0.0
  * Latency violation ratio (Lambda): 0.0

Exact algorithms are configured to yield all optimal solutions (if exists) with the numerating 
format `{alg}_{num}`.

Execution results:

| Algorithm            | Partitioning                                        |   Cost |   Latency |   Time (s) |
|----------------------|-----------------------------------------------------|--------|-----------|------------|
| GREEDY_0             | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.0235749  |
| GREEDY_1             | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0235749  |
| GREEDY_2             | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.0235749  |
| GREEDY_ILP_0         | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0947832  |
| GREEDY_ILP_1         | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.0947832  |
| GREEDY_ILP_2         | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.0947832  |
| GREEDY_PAR_0         | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.0405943  |
| GREEDY_PAR_1         | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0405943  |
| GREEDY_PAR_2         | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.0405943  |
| GREEDY_ILP_PAR_0     | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.101437   |
| GREEDY_ILP_PAR_1     | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.101437   |
| GREEDY_ILP_PAR_2     | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.101437   |
| ILP_CFG_HYBRID       | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0167496  |
| ILP_CFG_GREEDY       | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.017507   |
| ILP_CFG_HYBRID_PAR   | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0126527  |
| ILP_CFG_GREEDY_PAR   | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.0145207  |
| ILP_HYBRID_CPLEX_CMD | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0133516  |
| ILP_MTX              | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0197985  |
| ILP_MTX_PAR          | [[1, 3, 4, 5], [2], [6, 8, 9, 10], [7]]             |    858 |       474 | 0.0200093  |
| PSEUDO_B             | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.00047041 |
| PSEUDO_B_MP          | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.00764985 |
| PSEUDO_B_PAR         | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.00122202 |
| PSEUDO_L             | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.00083811 |
| PSEUDO_L_MP          | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.0073112  |
| PSEUDO_L_PAR         | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.00087904 |
| PSEUDO_L_PAR_MP      | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.00585536 |
| BIHEUR_B             | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.00065136 |
| BIFPTAS_L            | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.00082326 |
| BIFPTAS_L_DUAL       | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.00079769 |
| CHAIN_DECOMP         | [[1, 3, 4, 5], [2], [6, 9], [7], [8, 10]]           |    882 |       433 | 0.00010146 |
| TREE_CLUSTER         | [[1, 2, 3], [4], [5], [6, 7, 8, 9, 10]]             |    888 |       455 | 0.00152091 |
| MINW_UNBOUDED        | [[1, 3, 4, 5], [2], [6, 7, 8, 9], [10]]             |    858 |       471 | 0.00016116 |
| MINW_HEUR            | [[1, 2, 3], [4, 5, 6, 8, 9, 10], [7]]               |    858 |       443 | 0.00030477 |
| CSP                  | [[1, 3, 4, 5], [2], [6, 9], [7], [8, 10]]           |    882 |       433 | 0.0173627  |
| BASELINE_NO_PART     | [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]] |   1090 |       472 | 9.38e-05   |
| BASELINE_SINGLE      | [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]                   |    822 |       686 | 6.718e-05  |

Tests are conducted on Ubuntu 5.15.0-69-generic with AMD EPYC-Rome Processor @ 2.35GHz.

## Development and contribution

If you would like to contribute, add a feature, or just play with the implementations, the development
environment can be set up with the following commands.

```bash
git clone https://github.com/hsnlab/SLAMBUC.git
python3.11 -m pip install -U -r SLAMBUC/requirements.txt
python3.11 -m pip install --ignore-requires-python --no-deps -e SLAMBUC/
# Remove editing-mode package outside of repo root
python3.11 -m pip uninstall slambuc 
```

## Publications

If you use one of our algorithms published in this package or our test harness, please consider citing 
one of our related works.

#### [Polynomial-time algorithms based on chain-based tree partitioning:](https://doi.org/10.1109/noms56928.2023.10154412)

J. Czentye, I. Pelle and B. Sonkoly,
"Cost-optimal Operation of Latency Constrained Serverless Applications: From Theory to Practice,"
_NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium_, Miami, FL, USA, 2023, pp. 1-10,
doi: 10.1109/NOMS56928.2023.10154412.

```bibtex
@INPROCEEDINGS{Czentye2022noms,
    author = {J{\'{a}}nos Czentye and Istv{\'{a}}n Pelle and Bal{\'{a}}zs Sonkoly},
    booktitle = {{NOMS 2023-2023 IEEE/IFIP Network Operations and Management Symposium}},
    title = {{Cost-optimal Operation of Latency Constrained Serverless Applications: From Theory to Practice}},
    publisher = {{IEEE}},
    year = {2023},
    month = may,
    pages = {1--10},
    doi = {10.1109/NOMS56928.2023.10154412}
}
```

#### [Heuristic algorithm for dynamic (re)optimization control loop in edge-could environments:](https://doi.org/10.1109/jiot.2020.3042428)

I. Pelle, J. Czentye, J. Dóka, A. Kern, B. P. Gerő and B. Sonkoly,
"Operating Latency Sensitive Applications on Public Serverless Edge Cloud Platforms,"
in _IEEE Internet of Things Journal_, vol. 8, no. 10, pp. 7954-7972, 15 May, 2021,
doi: 10.1109/JIOT.2020.3042428.

```bibtex
@ARTICLE{Pelle2021jiot,
    author = {Pelle, Istv{\'{a}}n and Czentye, J{\'{a}}nos and D{\'{o}}ka, J{\'{a}}nos and Kern, Andr{\'{a}}s and Ger{\H{o}}, Bal{\'{a}}zs P. and Sonkoly, Bal{\'{a}}zs},
    journal = {{IEEE Internet of Things Journal}},
    title = {{Operating Latency Sensitive Applications on Public Serverless Edge Cloud Platforms}},
    publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
    year = {2021},
    month = may,
    volume = {8},
    number = {10},
    pages = {7954--7972},
    doi = {10.1109/JIOT.2020.3042428}
}
```

#### [Layout optimization for serverless applications over public clouds:](https://doi.org/10.1109/globecom38437.2019.9013988)

J. Czentye, I. Pelle, A. Kern, B. P. Gero, L. Toka and B. Sonkoly,
"Optimizing Latency Sensitive Applications for Amazon's Public Cloud Platform,"
_2019 IEEE Global Communications Conference (GLOBECOM)_, Waikoloa, HI, USA, 2019, pp. 1-7,
doi: 10.1109/GLOBECOM38437.2019.9013988.

```bibtex
@INPROCEEDINGS{Czentye2019globecom,
    author = {Czentye, Janos and Pelle, Istvan and Kern, Andras and Gero, Balazs Peter and Toka, Laszlo and Sonkoly, Balazs},
    booktitle = {{2019 IEEE Global Communications Conference (GLOBECOM)}},
    title = {{Optimizing Latency Sensitive Applications for Amazon's Public Cloud Platform}},
    publisher = {{IEEE}},
    year = {2019},
    month = dec,
    pages = {1--7},
    doi = {10.1109/GLOBECOM38437.2019.9013988}
}
```

## License

SLAMBUC is an open-source software licensed under [Apache 2.0](LICENSE).