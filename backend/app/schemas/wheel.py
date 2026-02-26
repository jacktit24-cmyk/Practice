"""Schemas for wheel strategy position management and analytics."""
from __future__ import annotations

from datetime import date
from pydantic import BaseModel, Field, field_validator


class WheelPositionBase(BaseModel):
    ticker: str = Field(..., min_length=1)
    phase: str = Field(..., description="CSP or CC")
    contracts: int = Field(..., gt=0)
    strike: float = Field(..., gt=0)
    expiration: date
    premium_collected: float = Field(..., ge=0)
    current_option_value: float = Field(..., ge=0)
    opened_dte: int = Field(..., gt=0)
    status: str = Field(default="Open")
    stock_cost_basis: float | None = Field(default=None, gt=0)
    linked_cycle_id: str | None = None

    @field_validator("ticker")
    @classmethod
    def normalize_ticker(cls, value: str) -> str:
        return value.upper().strip()

    @field_validator("phase")
    @classmethod
    def validate_phase(cls, value: str) -> str:
        normalized = value.upper().strip()
        if normalized not in {"CSP", "CC"}:
            raise ValueError("phase must be CSP or CC")
        return normalized


class WheelPositionCreate(WheelPositionBase):
    pass


class WheelPositionUpdate(BaseModel):
    contracts: int | None = Field(default=None, gt=0)
    strike: float | None = Field(default=None, gt=0)
    expiration: date | None = None
    premium_collected: float | None = Field(default=None, ge=0)
    current_option_value: float | None = Field(default=None, ge=0)
    status: str | None = None


class WheelPositionOut(WheelPositionBase):
    id: str
    dte: int
    capital_reserved: float
    unrealized_pl: float
    apy: float | None
    break_even: float


class WheelSummary(BaseModel):
    total_premium_open: float
    total_premium_mtd: float
    total_premium_ytd: float
    weighted_apy_csp: float
    capital_deployed_csp: float
    capital_at_risk_cc: float
    next_expiration_alerts: int


class WheelDashboardResponse(BaseModel):
    summary: WheelSummary
    positions: list[WheelPositionOut]
    dte_alerts: list[WheelPositionOut]
    capital_release_schedule: list[dict[str, float | str]]
