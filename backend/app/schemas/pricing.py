"""Pydantic schemas for pricing and sensitivity endpoints."""
from pydantic import BaseModel, Field, field_validator


class SensitivityRequest(BaseModel):
    ticker: str = Field(..., min_length=1, examples=["AAPL"])
    option_type: str = Field(..., description="CALL or PUT")
    strike: float = Field(..., gt=0)
    expiration_days: int = Field(..., gt=0, description="Days until expiration")
    implied_volatility: float = Field(..., gt=0, description="Annualized volatility in decimal form")
    current_stock_price: float = Field(..., gt=0)
    stock_price_scenarios: list[float] = Field(..., min_length=1)
    volatility_scenarios: list[float] = Field(..., min_length=1)
    time_horizon_days: list[int] = Field(..., min_length=1)
    risk_free_rate: float = Field(0.05, ge=0)

    @field_validator("option_type")
    @classmethod
    def validate_option_type(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in {"CALL", "PUT"}:
            raise ValueError("option_type must be CALL or PUT")
        return normalized


class SensitivityResponse(BaseModel):
    base_price: float
    scenarios: list[dict[str, float]]
