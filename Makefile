.PHONY: lint-check test build clean ci

clean:
	rm -rf dist __pycache__ .pytest_cache .coverage src/Music_Library.egg-info coverage.json Dump src/musiclibrary/__pycache__ src/musiclibrary/Dump

lint-check: clean
	uv sync --locked --dev
	uv run ruff check

test: clean
	uv sync --locked --dev
	uv run script_tests.py
	make clean

build: clean
	uv build

ci: lint-check test build