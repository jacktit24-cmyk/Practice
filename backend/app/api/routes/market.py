"""Market sentiment route for dashboard side widgets."""
from fastapi import APIRouter

from app.schemas.market import MarketSignals
from app.services.market_service import get_market_signals

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/signals", response_model=MarketSignals)
def market_signals() -> MarketSignals:
    return get_market_signals()
