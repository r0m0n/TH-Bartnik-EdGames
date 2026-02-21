.PHONY: test pipeline dashboard ingest playbook

test:
	python -m unittest discover -s tests -p 'test_*.py'

pipeline:
	python scripts/run_pipeline.py --mode dry-run

dashboard:
	python scripts/run_dashboard.py

ingest:
	python scripts/run_ingest.py --dry-run

playbook:
	python scripts/update_playbook.py
