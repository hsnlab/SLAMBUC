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
import setuptools

import slambuc

setuptools.setup(
    name="SLAMBUC",
    version=slambuc.__version__,
    author="Janos Czentye",
    author_email="czentye@tmit.bme.hu",
    description="Serverless Layout Adaptation with Memory-Bounds and User Constraints",
    long_description="Graph algorithms for composing cloud-native applications from standalone serverless functions"
                     "in a cost-efficient and latency-constrained manner.",
    url="https://github.com/hsnlab/SLAMBUC",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='cloud serverless ilp dp tree',
    license="Apache 2.0",
    install_requires=['numpy', 'networkx', 'PulP', 'cspy', 'matplotlib'],
    packages=['slambuc'],
    include_package_data=False,
    zip_safe=False

)
