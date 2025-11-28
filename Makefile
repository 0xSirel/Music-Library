.PHONY: init lint test build

init:
	python -m pip install -e .[dev]

lint:
	ruff check src

test:
	python -m coverage run -m pytest
	python -m coverage report -m

build: lint test
	python -m build
