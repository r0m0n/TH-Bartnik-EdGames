from __future__ import annotations

from dataclasses import dataclass

from .models import DecisionOutcome, EmailActionPlan


@dataclass
class Policy:
    confidence_threshold: float = 0.88
    safe_recipients_only: bool = True


def decide(plan: EmailActionPlan, mode: str, policy: Policy) -> DecisionOutcome:
    """Evaluate whether a plan can execute under a selected mode."""
    if mode in {"dry-run", "shadow"}:
        return DecisionOutcome(
            approved=False,
            mode=mode,
            reason="Execution disabled by run mode.",
        )

    if plan.proposed_solution.confidence < policy.confidence_threshold:
        return DecisionOutcome(
            approved=False,
            mode=mode,
            reason="Confidence below threshold.",
        )

    if plan.risk_flags:
        return DecisionOutcome(
            approved=False,
            mode=mode,
            reason=f"Risk flags present: {', '.join(plan.risk_flags)}",
        )

    return DecisionOutcome(
        approved=True,
        mode=mode,
        reason="Approved by policy.",
        execute_email=bool(plan.reply_options),
        execute_calendar=bool(plan.calendar_candidates),
        execute_asana=bool(plan.asana_candidates),
    )
