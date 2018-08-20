.PHONY: docs

dep:
	pipenv install

dev:
	pipenv install --dev

docs:
	cd ./docs && make html

test:
	python3 ./src/tests/test_dora.py
