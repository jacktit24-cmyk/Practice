"""Unit tests for Black-Scholes pricing and Greeks."""
from pricing.black_scholes import OptionInputs, breakeven_price, greeks, option_price
from pricing.scenarios import build_sensitivity_grid


def test_call_price_known_reference() -> None:
    """Validate call price against a known Black-Scholes benchmark case."""
    inputs = OptionInputs(
        spot=100,
        strike=100,
        time_to_expiry_years=1,
        risk_free_rate=0.05,
        volatility=0.2,
        option_type="CALL",
    )
    price = option_price(inputs)
    assert abs(price - 10.4506) < 1e-3


def test_put_price_known_reference() -> None:
    """Validate put price against a known Black-Scholes benchmark case."""
    inputs = OptionInputs(
        spot=100,
        strike=100,
        time_to_expiry_years=1,
        risk_free_rate=0.05,
        volatility=0.2,
        option_type="PUT",
    )
    price = option_price(inputs)
    assert abs(price - 5.5735) < 1e-3


def test_greeks_shapes_and_signs() -> None:
    """Check expected signs/ranges of Greeks for a call option."""
    inputs = OptionInputs(
        spot=100,
        strike=100,
        time_to_expiry_years=0.5,
        risk_free_rate=0.03,
        volatility=0.25,
        option_type="CALL",
    )
    values = greeks(inputs)

    assert 0 < values["delta"] < 1
    assert values["gamma"] > 0
    assert values["vega"] > 0


def test_breakeven_call_above_strike() -> None:
    inputs = OptionInputs(
        spot=110,
        strike=100,
        time_to_expiry_years=0.3,
        risk_free_rate=0.03,
        volatility=0.22,
        option_type="CALL",
    )
    assert breakeven_price(inputs) > inputs.strike


def test_scenario_grid_size() -> None:
    inputs = OptionInputs(
        spot=100,
        strike=105,
        time_to_expiry_years=0.5,
        risk_free_rate=0.05,
        volatility=0.3,
        option_type="PUT",
    )
    grid = build_sensitivity_grid(
        base_inputs=inputs,
        stock_prices=[95, 100, 105],
        volatilities=[0.2, 0.3],
        times_to_expiry_years=[0.25, 0.5],
    )
    assert len(grid) == 12
