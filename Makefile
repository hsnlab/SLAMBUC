clean:
	rm -rf *.egg-info
	rm -rf build dist

build: clean
	#python3.11 setup.py sdist bdist_wheel
	python3.11 -m build

dev-install:
	python3.11 -m pip install --no-cache-dir -e .

uninstall:
	pip uninstall slambuc

.PHONY: clean dev-install uninstall
.DEFAULT_GOAL := build
