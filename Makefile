clean:
	rm -rf *.egg-info
	rm -rf ./build ./dist

build: clean
	#python3.11 setup.py sdist bdist_wheel
	python3.11 -m build --sdist --wheel --outdir dist/ .

check:
	twine check dist/*

release: build check
	git tag -a `python3.11 -c "import slambuc;print(slambuc.__version__)"` -m  "New version release"
	git pull origin main
	git push --all --tags

test-publish: build check
	twine upload --repository testpypi dist/*

publish: release
	twine upload --repository pypi dist/*

########################################################################################################################

install-req:
	python3.11 -m pip install -U -r requirements.txt

dev-install:
	python3.11 -m pip install --no-cache-dir --ignore-requires-python --no-deps -e .

test-install: build
	python3.11 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ \
				--extra-index-url https://pypi.org/simple/ slambuc

uninstall:
	python3.11 -m pip uninstall slambuc

########################################################################################################################

doc:
	pydoc-markdown --with-processors --dump | docspec -m --dump-tree
	pydoc-markdown -p slambuc -v --py3 --render-toc > docs/slambuc_api.md

.PHONY: clean check install-req dev-install uninstall doc
.DEFAULT_GOAL := build
