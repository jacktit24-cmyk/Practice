"""Market signal aggregation from CNN fear/greed and Yahoo Finance VIX."""
from __future__ import annotations

import httpx
import yfinance as yf

from app.schemas.market import MarketSignals


def _fear_greed() -> tuple[float, str]:
    url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
    try:
        response = httpx.get(url, timeout=8)
        response.raise_for_status()
        score = float(response.json()["fear_and_greed"]["score"])
    except Exception:
        score = 50.0

    if score < 25:
        label = "Extreme Fear"
    elif score < 45:
        label = "Fear"
    elif score < 56:
        label = "Neutral"
    elif score < 75:
        label = "Greed"
    else:
        label = "Extreme Greed"

    return score, label


def _vix() -> tuple[float, float, str]:
    try:
        ticker = yf.Ticker("^VIX")
        history = ticker.history(period="5d", interval="1d")
        latest = float(history["Close"].iloc[-1])
        previous = float(history["Close"].iloc[-2]) if len(history) > 1 else latest
    except Exception:
        latest, previous = 20.0, 20.0

    change_pct = ((latest - previous) / previous * 100) if previous else 0.0

    if latest >= 25 or change_pct >= 10:
        alert = "VIX increasing risk"
    elif change_pct <= -10:
        alert = "VIX cooling quickly"
    else:
        alert = "VIX stable"

    return latest, change_pct, alert


def get_market_signals() -> MarketSignals:
    fear_score, fear_label = _fear_greed()
    vix_price, vix_change_pct, vix_alert = _vix()

    regime_score = max(0.0, min(100.0, 100 - vix_price * 2 + (fear_score - 50) * 0.6))
    if regime_score < 35:
        regime_label = "Risk-Off"
    elif regime_score < 65:
        regime_label = "Neutral"
    else:
        regime_label = "Risk-On"

    return MarketSignals(
        fear_greed_score=fear_score,
        fear_greed_label=fear_label,
        vix_price=vix_price,
        vix_change_pct=vix_change_pct,
        vix_alert=vix_alert,
        regime_score=regime_score,
        regime_label=regime_label,
    )
