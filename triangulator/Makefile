test:
	pytest

unit_test:
	pytest -k "not perf"

perf_test:
	pytest -k "perf"

coverage:
	coverage run -m pytest -k "not perf"

lint:
	ruff check src

doc:
	pdoc3

help:
	@echo "test"