"""Pricing and sensitivity API routes."""
from fastapi import APIRouter

from app.schemas.pricing import SensitivityRequest, SensitivityResponse
from pricing.black_scholes import OptionInputs, option_price
from pricing.scenarios import build_sensitivity_grid

router = APIRouter(prefix="/pricing", tags=["pricing"])


@router.post("/sensitivity", response_model=SensitivityResponse)
def sensitivity(request: SensitivityRequest) -> SensitivityResponse:
    """Run Black-Scholes scenario grid across stock/vol/time inputs."""
    base_inputs = OptionInputs(
        spot=request.current_stock_price,
        strike=request.strike,
        time_to_expiry_years=request.expiration_days / 365,
        risk_free_rate=request.risk_free_rate,
        volatility=request.implied_volatility,
        option_type=request.option_type,
    )
    scenarios = build_sensitivity_grid(
        base_inputs=base_inputs,
        stock_prices=request.stock_price_scenarios,
        volatilities=request.volatility_scenarios,
        times_to_expiry_years=[max(days, 1) / 365 for days in request.time_horizon_days],
    )
    return SensitivityResponse(base_price=option_price(base_inputs), scenarios=scenarios)
