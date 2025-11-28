.PHONY: init lint-fix lint-check lint test build

init:
	pip install -e .[dev]

lint-check:
	ruff check src

lint-fix:
	ruff check src --fix

test:
	coverage run -m pytest
	coverage report -m

build: lint-fix test
	python -m build

all : init build
