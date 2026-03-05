.PHONY: install install-gpu check lint format test run-report

install:
	pip install -r requirements.txt

install-gpu:
	pip install -r requirements-gpu.txt

lint:
	ruff check src

format:
	ruff format src

test:
	pytest

check:
	ruff check src
	python -m compileall src

run-report:
	python src/report/generate_report.py --input-dir output --out-dir output
