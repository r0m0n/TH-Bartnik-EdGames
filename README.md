# GenAI Executive Assistant (Local)

A local-first executive-assistant workflow that triages Thunderbird email, prepares multilingual reply drafts, and synchronizes approved actions to Google Calendar and Asana.

## v1 Scope
- Thunderbird ingestion via profile parsing (MBOX/Maildir), IMAP fallback.
- LLM pipeline using LM Studio OpenAI-compatible endpoint.
- Structured action plans validated against JSON schemas in `schemas/`.
- Decision engine with confidence gating, risk flags, dry-run/shadow/execute modes.
- Dashboard-first UX with one-click **Approve & Execute All Suggested Actions**.
- Connectors for SMTP, Google Calendar, and Asana (initial local stubs in this repo).

## Repository layout
- `app/` core models and orchestrator stubs
- `config/` YAML configuration templates
- `context/` FAQ playbook placeholders
- `schemas/` strict output contracts for pipeline stages
- `tests/` schema and pipeline smoke tests
- `scripts/` run entrypoints (`run_ingest`, `run_pipeline`, `run_dashboard`, `update_playbook`)

## Run modes
- `--dry-run`: no external side effects, log all proposed actions.
- `--shadow`: run decisioning and proposal generation while suppressing execution.
- `--execute-approved`: execute only approved items.
- `--auto-exec-safe`: execute low-risk/high-confidence items according to policy.

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py --dry-run
```

## Configuration
Copy and edit templates in `config/`:
- `app.yaml`
- `connectors.yaml`
- `contacts.yaml`
- `links.yaml`
- `signatures.yaml`

Use `.env` for development credentials only. Do not commit secrets.

## Testing
```bash
python -m unittest discover -s tests -p 'test_*.py'
```
