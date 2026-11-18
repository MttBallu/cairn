"""Handling of coding rules logic and artifacts."""

from enum import StrEnum


class RuleStatus(StrEnum):
    """Define the possible status for a rule."""

    PROPOSED = "PROPOSED"
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"
    SUPERSEDED = "SUPERSEDED"
    WITHDRAWN = "WITHDRAWN"
