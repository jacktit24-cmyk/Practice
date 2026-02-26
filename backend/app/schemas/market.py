"""Schemas for market sentiment widgets used on dashboard."""
from pydantic import BaseModel


class MarketSignals(BaseModel):
    fear_greed_score: float
    fear_greed_label: str
    vix_price: float
    vix_change_pct: float
    vix_alert: str
    regime_score: float
    regime_label: str
