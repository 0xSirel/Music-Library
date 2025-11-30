.PHONY: init lint-fix lint-check lint test build

init:
	pip install -e .[dev]

lint-check:
	ruff check src
	ruff check tests

lint-fix:
	ruff check src --fix
	ruff check tests --fix

test:
	pytest --cov=src/musiclibrary --cov-report=term-missing

build: lint-fix test
	python -m build

all : init build
