.PHONY: docs

docs:
	cd ./docs && make html

test:
	python3 ./src/tests/test_dora.py
