init:
	pip3 install pipenv --upgrade
	pipenv install
	pipenv install --dev

ci:
	pipenv run pytest

docs:
	cd docs && make html
	@echo "Build finished. The HTML pages are in build/html"
