#!/usr/bin/env python3
"""Run decisioning against a sample action plan."""

import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.models import EmailActionPlan
from app.pipeline import Policy, decide


SAMPLE = {
    "email_id": "msg-001",
    "email_language": "en",
    "category_primary": "Collaboration/External",
    "gtd_bucket": "Action",
    "priority": "P1",
    "proposed_solution": {
        "plan": "Reply with two available time slots and create a follow-up task.",
        "rationale": "Sender requested scheduling and project confirmation.",
        "confidence": 0.91,
    },
    "reply_options": [
        {"label": "Direct reply", "body": "Thanks, I can meet Tue or Thu at 14:00."}
    ],
    "calendar_candidates": [
        {"title": "Project sync", "action": "propose"}
    ],
    "asana_candidates": [
        {
            "title": "Prepare project sync agenda",
            "description": "Draft agenda before meeting",
            "tags": ["email", "follow-up"],
        }
    ],
    "bundle_hints": ["thread:abc"],
    "risk_flags": [],
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["dry-run", "shadow", "execute-approved", "auto-exec-safe"],
        default="dry-run",
    )
    args = parser.parse_args()

    plan = EmailActionPlan.model_validate(SAMPLE)
    outcome = decide(plan=plan, mode=args.mode, policy=Policy())
    print(outcome.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
