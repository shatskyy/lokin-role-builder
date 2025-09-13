PY = python3
PIP = pip

.PHONY: dev run test lint

dev:
	$(PY) -m venv .venv && . .venv/bin/activate && $(PIP) install -e .[dev]

run:
	. .venv/bin/activate && uvicorn app.main:app --reload

test:
	. .venv/bin/activate && pytest -q

lint:
	. .venv/bin/activate && ruff check . && mypy .
