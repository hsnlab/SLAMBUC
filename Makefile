clean:
	rm -rf *.egg-info
	rm -rf ./build ./dist
	rm -rf .pytest_cache

build: clean
	#python3.11 setup.py sdist bdist_wheel
	python3.11 -m build --sdist --wheel --outdir dist/ .

check:
	twine check dist/*

publish: build check
	twine upload --repository pypi dist/*

release: build check
	git tag -a `python3.11 -c "import slambuc;print(slambuc.__version__)"` -m  "New version release"
	git pull origin main
	git push origin main
	git push --tags
	twine upload --repository pypi dist/*

######## Testing

test:
	cd tests && python3.11 -m pytest -v .

test-publish: build check
	twine upload --repository testpypi dist/*

######## Installation

install-req:
	python3.11 -m pip install -U -r requirements.txt

dev-install: install-req
	python3.11 -m pip install --no-cache-dir --no-deps -e .

test-install: build
	python3.11 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ \
				--extra-index-url https://pypi.org/simple/ slambuc

uninstall:
	python3.11 -m pip uninstall slambuc

######## Documentation

doc:
	pydoc-markdown --with-processors --dump | docspec -m --dump-tree
	pydoc-markdown -p slambuc -v --py3 --render-toc > docs/slambuc_api.md

.PHONY: clean check test install-req uninstall doc
.DEFAULT_GOAL := build
