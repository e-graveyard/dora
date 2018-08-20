.PHONY: docs

init:
	pip3 install pipenv --upgrade

cov: init
	pip3 install codecov
	cd ./src/tests && coverage run test_dora.py

dep: init
	pipenv install

dev: init
	pipenv install --dev

docs:
	cd ./docs && make html

test:
	python3 ./src/tests/test_dora.py
