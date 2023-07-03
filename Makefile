.PHONY: clean

clean:
	rm -rf *.egg-info
	rm -rf build dist

build: clean
	python3.11 setup.py sdist bdist_wheel
