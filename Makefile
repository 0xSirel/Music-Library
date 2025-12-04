.PHONY: init lint-fix lint-check lint test build all clean

clean:
	rm -rf dist __pycache__ .pytest_cache .coverage src/Music_Library.egg-info

init:
	pip install --upgrade pip
	pip install -e .[dev]

lint-check:
	ruff check src
	ruff check tests

lint-fix:
	ruff check src --fix
	ruff check tests --fix

test:
	python -m pytest

build: lint-check test
	python -m build

all : init build
