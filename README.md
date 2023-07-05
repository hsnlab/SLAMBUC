# Serverless Layout Adaptation with Memory-Bounds and User Constraints (SLAMBUC)

Collection of graph partitioning algorithms implemented in Python for composing cloud-native applications
from standalone serverless functions in a cost-efficient and latency-constrained manner.

## Overview

In the context of serverless computing, function fusion is a novel, high-level approach to improve
performance and at the same time reduce the operational cost of serverless applications consisting
of stateless, ephemeral functions. This is achieved by grouping, encompassing, and assembling connected
FaaS functions into separate composite components representing the deployable software artifacts that
are provisioned by the serverless frameworks in the same way as other single functions.
In addition, different user-defined Quality of Service (QoS) constraints should be also taken into
account, e.g. overall response time of the application or an end-to-end latency constraint on the
critical path in the application's call graph.

Under the hood, this problem can be formalized as the partitioning of the application call graph (DAG)
into disjoint, connected subgraphs in a cost-efficient manner, while specific requirements imposed by
the user and the platform (flavors) itself need to be satisfied.

In the package, we collected various partitioning algorithms tailored to tree-shape serverless
applications with different runtime complexity, considering communication parameters and requirements.
Our main objective is to find the cost-optimal grouping of functions concerning node and edge-weighted
trees and cost/memory/latency models based on public cloud frameworks, whereas each flavor imposes an
upper limit on the available operative memory.
Moreover, a user-given latency constraint has to be fulfilled on the tree's critical path which is
defined as the subchain between the first/front-end function and a predefined leaf node.

## Installation

### Environment

Our implementations require Python3.10 or above. To set up the latest Python environment on Ubuntu,
the following code snippet can be used:

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

However, for the latest changes, it can be installed directly from GitHub with

```bash
python3.11 -m pip install --no-cache-dir git+https://github.com/hsnlab/SLAMBUC.git
```

Tree plotting relies on networkx's internal plotting feature that generates a layout based on the external
[graphviz tool and its python frontend](https://pygraphviz.github.io/documentation/stable/install.html).
Thus, in that case, the related packages must be installed:

```bash
sudo apt-get install graphviz graphviz-dev
python3.11 -m pip install pygraphviz
```

External solvers can be used in LP-based algorithms that require the given solver packages to be
preinstalled and available for the [PuLP frontend](https://github.com/coin-or/pulp). Currently,
the following solvers are tested:

* CBC (default)
* GLPK (see installation [here](https://coin-or.github.io/pulp/main/installing_pulp_at_home.html#linux-installation))
* CPLEX ([installation](https://www.ibm.com/products/ilog-cplex-optimization-studio)
  and [setup](https://coin-or.github.io/pulp/guides/how_to_configure_solvers.html#cplex))

It is worth noting that CPLEX's python wrapper [docplex](https://pypi.org/project/docplex/)
(as a replacement for PuLP) is left behind the latest Python version. For using this API, separate
requirements are prepared for Python version _3.10_.

```bash
python3.10 -m pip install -U -r requirements_py3.10.txt
```

For solving constrained shortest path problems, we apply heuristics from the [cspy](https://github.com/torressa/cspy)
package.

### Test harness and performance validation

Our repository contains separate test scripts under the [tests](tests) folder for validating the input/output
formats and call parameters. These codes also serve as example codes for using our package.

For comparative analyses, we also implemented a test harness under [validation](validation)
to automatize test executions with generated test input graphs from [validation/data](validation/data).

To install additional dependencies, run the following command:

```bash
python3.11 -m pip install slambuc[tests]      # For executing tests
python3.11 -m pip install slambuc[validation] # For using test harness
```

## Development and contribution

If you would like to contribute, add a feature, or just play with the implementations, the development
environment can be set up with the following commands.

```bash
git clone https://github.com/hsnlab/SLAMBUC.git
python3.11 -m pip install -U -r SLAMBUC/requirements.txt
python3.11 -m pip install -e SLAMBUC
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

## Publications

If you use one of our algorithms published in this package or our test harness, please consider
citing one of our related works:

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