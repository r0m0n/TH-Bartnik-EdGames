from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Priority(str, Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"


class GTDBucket(str, Enum):
    CALENDAR = "Calendar"
    ACTION = "Action"
    WAITING_FOR = "Waiting For"
    REFERENCE = "Reference"
    SOMEDAY_MAYBE = "Someday/Maybe"


class Category(str, Enum):
    TEACHING_STUDENTS = "Teaching/Students"
    TEACHING_ADMIN = "Teaching/Admin"
    WRITING_RESEARCH = "Writing/Research"
    COLLAB_EXTERNAL = "Collaboration/External"
    ADMIN_ORG = "Administration/Org"
    NEWSLETTER = "Newsletter/Info"
    OTHER = "Other/Unclassified"


class ProposedSolution(BaseModel):
    plan: str = Field(..., min_length=5)
    rationale: str = Field(..., min_length=5)
    confidence: float = Field(..., ge=0.0, le=1.0)


class ReplyOption(BaseModel):
    label: str
    body: str


class CalendarCandidate(BaseModel):
    title: str
    start_iso: Optional[str] = None
    end_iso: Optional[str] = None
    timezone: Optional[str] = None
    action: str = "propose"


class AsanaCandidate(BaseModel):
    title: str
    description: str
    due_iso: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


class EmailActionPlan(BaseModel):
    email_id: str
    email_language: str
    category_primary: Category
    gtd_bucket: GTDBucket
    priority: Priority
    proposed_solution: ProposedSolution
    reply_options: List[ReplyOption] = Field(default_factory=list)
    calendar_candidates: List[CalendarCandidate] = Field(default_factory=list)
    asana_candidates: List[AsanaCandidate] = Field(default_factory=list)
    bundle_hints: List[str] = Field(default_factory=list)
    risk_flags: List[str] = Field(default_factory=list)


class DecisionOutcome(BaseModel):
    approved: bool
    mode: str
    reason: str
    execute_email: bool = False
    execute_calendar: bool = False
    execute_asana: bool = False
