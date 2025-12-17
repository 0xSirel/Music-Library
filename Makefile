.PHONY: lint-fix lint-check test build clean

clean:
	rm -rf dist __pycache__ .pytest_cache .coverage src/Music_Library.egg-info coverage.json

lint-check:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

test: clean
	uv run script_tests.py

build: lint-check test
	uv build
