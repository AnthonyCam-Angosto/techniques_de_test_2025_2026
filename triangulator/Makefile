test:
	pytest

unit_test:
	pytest -k "not perf"

perf_test:
	pytest -k "perf"

coverage:
	coverage run -m pytest -k "not perf"
	coverage html

lint:
	ruff check src --fix

doc:
	pdoc3 src --html --output-dir docs --force