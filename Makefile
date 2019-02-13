.PHONY: docs

docs:
	cd ./docs && make html

test:
	./tests/test_dora.py
