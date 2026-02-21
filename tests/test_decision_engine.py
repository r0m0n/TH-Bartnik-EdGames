import unittest

from app.models import EmailActionPlan
from app.pipeline import Policy, decide


class DecisionEngineTests(unittest.TestCase):
    def test_dry_run_never_executes(self):
        plan = EmailActionPlan.model_validate(
            {
                "email_id": "msg",
                "email_language": "en",
                "category_primary": "Administration/Org",
                "gtd_bucket": "Action",
                "priority": "P2",
                "proposed_solution": {
                    "plan": "Send confirmation.",
                    "rationale": "Straightforward request.",
                    "confidence": 0.99,
                },
                "reply_options": [{"label": "reply", "body": "Done."}],
                "calendar_candidates": [],
                "asana_candidates": [],
                "bundle_hints": [],
                "risk_flags": [],
            }
        )
        outcome = decide(plan=plan, mode="dry-run", policy=Policy())
        self.assertFalse(outcome.approved)
        self.assertFalse(outcome.execute_email)


if __name__ == "__main__":
    unittest.main()
