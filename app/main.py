from __future__ import annotations

from fastapi import FastAPI

from .models import DecisionOutcome, EmailActionPlan
from .pipeline import Policy, decide

app = FastAPI(title="GenAI Executive Assistant Local")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/decide", response_model=DecisionOutcome)
def run_decision(plan: EmailActionPlan, mode: str = "execute-approved") -> DecisionOutcome:
    return decide(plan=plan, mode=mode, policy=Policy())
