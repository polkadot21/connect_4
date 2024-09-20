# Makefile for Connect 4 game project

# Variables
PYTHON_FILES = connect_4 tests

# Commands
.PHONY: check format lint type test run

# Run all checks
check: format lint type

# Format code using black (replacing ruff format)
format:
	ruff format $(PYTHON_FILES)

# Lint code with ruff and fix issues
lint:
	ruff check . --fix

# Type checking with mypy
type:
	mypy $(PYTHON_FILES)

# Run tests
test:
	pytest . -v

# Run the game
run:
	python main.py