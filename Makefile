clean:
	rm -rf *.egg-info
	rm -rf ./build ./dist
	rm -rf .pytest_cache

build: clean
	@#python3.13 setup.py sdist bdist_wheel
	python3.13 -m build --sdist --wheel --outdir dist/ .

check:
	twine check dist/*

release: build check
	git tag -a `python3.13 -c "import slambuc;print(slambuc.__version__)"` -m  "New version release"
	git pull origin main github
	git push origin main github
	git push --tags main github

publish: build check
	@#cat token.txt | xargs -I {} twine upload --repository pypi -u __token__ -p {} dist/*
	twine upload --verbose --repository SLAMBUC dist/*

######## Testing

test:
	python3.13 tests/validate_algs.py
	python3.13 -m pytest -vv tests/

test12:
	python3.12 -m pytest -vv tests/

test-publish: build check
	twine upload --verbose --repository test-SLAMBUC dist/*

######## Installation

install-req:
	sudo apt install python3.13-dev graphviz libgraphviz-dev pkg-config glpk-utils
	python3.13 -m pip install -U pip
	python3.13 -m pip install -U -r requirements.txt

dev-install: install-req
	python3.13 -m pip install --no-cache-dir --no-deps -e .

test-install: build
	python3.13 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ \
				--extra-index-url https://pypi.org/simple/ slambuc

uninstall:
	python3.13 -m pip uninstall slambuc

######## Documentation

doc:
	pydoc-markdown --with-processors --dump | docspec -m --dump-tree
	pydoc-markdown -p slambuc -v --py3 --render-toc > docs/slambuc_api.md

.PHONY: clean check test install-req uninstall doc
.DEFAULT_GOAL := build
