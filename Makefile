.PHONY: clean

clean:
	rm -rf *.egg-info
	rm -rf build dist

build: clean
	python setup.py sdist bdist_wheel
