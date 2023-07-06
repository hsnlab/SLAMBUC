clean:
	rm -rf *.egg-info
	rm -rf build dist

build: clean
	#python3.11 setup.py sdist bdist_wheel
	python3.11 -m build

check:
	twine check dist/*

test-publish: build
	twine upload --repository testpypi dist/*

publish: build
	twine upload --repository pypi dist/*

install-req:
	python3.11 -m pip install -U -r requirements.txt

dev-install:
	python3.11 -m pip install --no-cache-dir --ignore-requires-python --no-deps -e .

test-install: build
	python3.11 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ \
				--extra-index-url https://pypi.org/simple/ slambuc

uninstall:
	pip uninstall slambuc

.PHONY: clean dev-install uninstall
.DEFAULT_GOAL := build
