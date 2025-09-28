.PHONY: install test run

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

test:
	pytest -q

run:
	python -m src.my_agent.cli
