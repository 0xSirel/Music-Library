.PHONY: init lint test build

init:
	pip install -e .[dev]

lint:
	ruff check src

test:
	coverage run -m pytest
	coverage report -m

build: lint test
	python -m build

all : init build