"""Black-Scholes pricing and Greeks utilities.

This module is intentionally framework-agnostic so it can be reused by:
- API routes
- portfolio analytics services
- unit tests
"""
from __future__ import annotations

from dataclasses import dataclass
from math import exp, log, sqrt

from scipy.stats import norm


@dataclass(frozen=True)
class OptionInputs:
    """Container for Black-Scholes inputs."""

    spot: float
    strike: float
    time_to_expiry_years: float
    risk_free_rate: float
    volatility: float
    option_type: str


def _validate_inputs(inputs: OptionInputs) -> None:
    """Validate numerical and enum constraints for pricing inputs."""
    if inputs.spot <= 0:
        raise ValueError("Spot price must be positive.")
    if inputs.strike <= 0:
        raise ValueError("Strike price must be positive.")
    if inputs.time_to_expiry_years <= 0:
        raise ValueError("Time to expiry must be positive.")
    if inputs.volatility <= 0:
        raise ValueError("Volatility must be positive.")
    if inputs.option_type not in {"CALL", "PUT"}:
        raise ValueError("option_type must be either 'CALL' or 'PUT'.")


def d1(inputs: OptionInputs) -> float:
    """Compute Black-Scholes d1."""
    _validate_inputs(inputs)
    numerator = log(inputs.spot / inputs.strike) + (
        inputs.risk_free_rate + 0.5 * inputs.volatility**2
    ) * inputs.time_to_expiry_years
    denominator = inputs.volatility * sqrt(inputs.time_to_expiry_years)
    return numerator / denominator


def d2(inputs: OptionInputs) -> float:
    """Compute Black-Scholes d2."""
    d1_value = d1(inputs)
    return d1_value - inputs.volatility * sqrt(inputs.time_to_expiry_years)


def option_price(inputs: OptionInputs) -> float:
    """Compute theoretical European option price."""
    d1_value = d1(inputs)
    d2_value = d2(inputs)
    discount_factor = exp(-inputs.risk_free_rate * inputs.time_to_expiry_years)

    if inputs.option_type == "CALL":
        return inputs.spot * norm.cdf(d1_value) - inputs.strike * discount_factor * norm.cdf(d2_value)

    return inputs.strike * discount_factor * norm.cdf(-d2_value) - inputs.spot * norm.cdf(-d1_value)


def greeks(inputs: OptionInputs) -> dict[str, float]:
    """Compute primary Black-Scholes Greeks for European options.

    Theta is returned as annualized value (not per-day).
    """
    d1_value = d1(inputs)
    d2_value = d2(inputs)
    sqrt_t = sqrt(inputs.time_to_expiry_years)
    discount_factor = exp(-inputs.risk_free_rate * inputs.time_to_expiry_years)
    pdf_d1 = norm.pdf(d1_value)

    gamma_value = pdf_d1 / (inputs.spot * inputs.volatility * sqrt_t)
    vega_value = inputs.spot * pdf_d1 * sqrt_t

    if inputs.option_type == "CALL":
        delta_value = norm.cdf(d1_value)
        theta_value = (
            -(inputs.spot * pdf_d1 * inputs.volatility) / (2 * sqrt_t)
            - inputs.risk_free_rate * inputs.strike * discount_factor * norm.cdf(d2_value)
        )
    else:
        delta_value = norm.cdf(d1_value) - 1
        theta_value = (
            -(inputs.spot * pdf_d1 * inputs.volatility) / (2 * sqrt_t)
            + inputs.risk_free_rate * inputs.strike * discount_factor * norm.cdf(-d2_value)
        )

    return {
        "delta": delta_value,
        "gamma": gamma_value,
        "theta": theta_value,
        "vega": vega_value,
    }


def breakeven_price(inputs: OptionInputs) -> float:
    """Compute option break-even at expiry based on premium from current model price."""
    premium = option_price(inputs)
    if inputs.option_type == "CALL":
        return inputs.strike + premium
    return inputs.strike - premium
