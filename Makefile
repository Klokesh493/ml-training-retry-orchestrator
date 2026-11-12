PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) retry_orchestrator.py sample_failures.csv

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
