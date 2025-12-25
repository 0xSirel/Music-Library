.PHONY: clean lint typecheck test build install ci help

.DEFAULT_GOAL := help

DIST_DIR := dist
SRC_DIR := src
COVERAGE_FILE := coverage.json

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

clean: ## Clean build artifacts and cache
	rm -rf $(DIST_DIR) __pycache__ .pytest_cache .coverage $(COVERAGE_FILE)
	rm -rf $(SRC_DIR)/Music_Library.egg-info $(SRC_DIR)/musiclibrary/__pycache__
	rm -rf Dump $(SRC_DIR)/musiclibrary/Dump .mypy_cache

lint: ## Run linter (ruff)
	uv sync --locked --dev
	uv run ruff check

typecheck: ## Run type checker (mypy)
	uv sync --locked --dev
	uv run mypy $(SRC_DIR)/

test: clean ## Run tests with coverage
	uv sync --locked --dev
	uv run script_tests.py
	$(MAKE) clean

build: clean ## Build wheel package
	uv build

install: build ## Build and install package
	uv pip install $(DIST_DIR)/*.whl

ci: lint typecheck test build ## Run full CI pipeline

all: ci ## Alias for ci
