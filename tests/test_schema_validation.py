import json
from pathlib import Path
import unittest

import jsonschema


class SchemaValidationTests(unittest.TestCase):
    def test_action_plan_schema_accepts_valid_example(self):
        schema = json.loads(Path("schemas/action_plan.schema.json").read_text())
        payload = {
            "email_id": "abc",
            "email_language": "de",
            "category_primary": "Teaching/Students",
            "gtd_bucket": "Action",
            "priority": "P1",
            "proposed_solution": {
                "plan": "Antwort mit Rückfrage senden.",
                "rationale": "Anfrage ist unvollständig.",
                "confidence": 0.9,
            },
            "reply_options": [{"label": "Rückfrage", "body": "Könnten Sie ..."}],
            "calendar_candidates": [],
            "asana_candidates": [],
            "bundle_hints": ["thread:1"],
            "risk_flags": [],
        }

        jsonschema.validate(payload, schema)


if __name__ == "__main__":
    unittest.main()
