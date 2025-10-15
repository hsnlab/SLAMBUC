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

$(eval VER = `python3.14 -c "import slambuc;print(slambuc.__version__)"`)

clean:
	rm -rf *.egg-info
	rm -rf ./build ./dist
	rm -rf .pytest_cache
	sudo py3clean -v .
	docker rmi -f czentye/slambuc:${VER} || true

build: clean
	@#python3.14 setup.py sdist bdist_wheel
	python3.14 -m build --sdist --wheel --outdir dist/ .

docker-image: clean
	docker build -t czentye/slambuc:${VER} -t czentye/slambuc:latest .

check:
	twine check dist/*

release: build docker-image check
	git tag -a `python3.14 -c "import slambuc;print(slambuc.__version__)"` -m  "New version release"
	git pull origin main
	git pull github main
	git push origin main
	git push github main
	git push --tags origin
	git push --tags github
	docker push czentye/slambuc:${VER}
	docker push czentye/slambuc:latest

publish: build check
	@#cat token.txt | xargs -I {} twine upload --repository pypi -u __token__ -p {} dist/*
	twine upload --verbose --repository SLAMBUC dist/*

run:
	docker run --rm -v.:/usr/src/slambuc --entrypoint sh -ti czentye/slambuc:${VER}

######## Testing

test:
	python3.14 tests/validate_algs.py
	python3.14 -m pytest -vv tests/

test12:
	python3.12 -m pytest -vv tests/

test-publish: build check
	twine upload --verbose --repository test-SLAMBUC dist/*

######## Installation

install-req:
	sudo apt install python3.14-dev graphviz libgraphviz-dev pkg-config glpk-utils
	python3.14 -m pip install -U pip
	python3.14 -m pip install -U -r requirements.txt

dev-install: install-req
	python3.14 -m pip install --no-cache-dir --no-deps -e .

test-install: build
	python3.14 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ \
				--extra-index-url https://pypi.org/simple/ slambuc

uninstall:
	python3.14 -m pip uninstall slambuc

######## Documentation

doc:
	pydoc-markdown --with-processors --dump | docspec -m --dump-tree
	pydoc-markdown -p slambuc -v --py3 --render-toc > docs/slambuc_api.md

.PHONY: clean check test install-req uninstall doc
.DEFAULT_GOAL := build
