# SLAMBUC
## Serverless Layout Adaptation with Memory-Bounds and User Constraints

Graph algorithms for composing cloud-native applications from standalone serverless functions
in a cost-efficient and latency-constrained manner.

### Installation

To install all requirements the following commands can be used:

```bash
sudo add-apt-repository -y 'ppa:deadsnakes/ppa' && sudo apt update
sudo apt install build-essential graphviz libgraphviz-dev pkg-config glpk-utils python3.11-dev
sudo curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.11
python3.11 -m pip install -U pip
python3.11 -m pip install -U -r requirements.txt
```

Tests can be executed from the **[tests](tests)** folder but algorithms can be installed as a standalone package.
Install the ``SLAMBUC`` package with the following command:

```bash
python3.11 -m pip install ./
```

or

```bash
python3.11 setup.py
```

For development mode you can use the following commands:

```bash
python3.11 -m pip install -e ./
```

or

```bash
python3.11 setup.py develop
```

``docplex`` package only support Python3.10 (2023. jan.). To install for Python3.10 use the above command with the
*3.10* version and __[requirements_py3.10.txt](requirements_py3.10.txt)__ dependencies.

```bash
sudo apt install python3.10-dev
sudo curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.10
python3.10 -m pip install -U pip
python3.10 -m pip install -U -r requirements_py3.10.txt
```