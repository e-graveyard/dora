init:
	pip3 install pipenv --upgrade
	pipenv install
	pipenv install --dev

ci:
	pipenv run pytest
