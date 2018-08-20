.PHONY: docs

init:
	pip3 install pipenv --upgrade

cov: init
	pip3 install codecov

dep: init
	pipenv install

dev: init
	pipenv install --dev

docs:
	cd ./docs && make html

test:
	python3 ./src/tests/test_dora.py
