"""Scenario grid generation for sensitivity analysis."""
from __future__ import annotations

from dataclasses import asdict, dataclass

from pricing.black_scholes import OptionInputs, greeks, option_price


@dataclass(frozen=True)
class ScenarioPoint:
    """Single scenario output row for option repricing."""

    spot: float
    volatility: float
    time_to_expiry_years: float
    price: float
    delta: float
    gamma: float
    theta: float
    vega: float
    pct_change_vs_base: float


def build_sensitivity_grid(
    base_inputs: OptionInputs,
    stock_prices: list[float],
    volatilities: list[float],
    times_to_expiry_years: list[float],
) -> list[dict[str, float]]:
    """Create a full Cartesian scenario grid for pricing and Greeks."""
    base_price = option_price(base_inputs)
    grid: list[dict[str, float]] = []

    for spot in stock_prices:
        for volatility in volatilities:
            for time_to_expiry in times_to_expiry_years:
                scenario_inputs = OptionInputs(
                    spot=spot,
                    strike=base_inputs.strike,
                    time_to_expiry_years=time_to_expiry,
                    risk_free_rate=base_inputs.risk_free_rate,
                    volatility=volatility,
                    option_type=base_inputs.option_type,
                )
                scenario_price = option_price(scenario_inputs)
                scenario_greeks = greeks(scenario_inputs)
                pct_change = ((scenario_price - base_price) / base_price) * 100 if base_price else 0.0

                point = ScenarioPoint(
                    spot=spot,
                    volatility=volatility,
                    time_to_expiry_years=time_to_expiry,
                    price=scenario_price,
                    delta=scenario_greeks["delta"],
                    gamma=scenario_greeks["gamma"],
                    theta=scenario_greeks["theta"],
                    vega=scenario_greeks["vega"],
                    pct_change_vs_base=pct_change,
                )
                grid.append(asdict(point))

    return grid
