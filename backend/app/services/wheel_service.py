"""Wheel strategy business logic for cycle analytics and dashboard views."""
from __future__ import annotations

from datetime import date
from uuid import uuid4

from app.models.wheel import load_positions, save_positions
from app.schemas.wheel import WheelDashboardResponse, WheelPositionCreate, WheelPositionOut, WheelSummary


def _compute_position(row: dict) -> WheelPositionOut:
    today = date.today()
    expiration = date.fromisoformat(row["expiration"])
    dte = max((expiration - today).days, 0)

    capital_reserved = row["strike"] * 100 * row["contracts"]
    unrealized_pl = (row["premium_collected"] - row["current_option_value"]) * 100 * row["contracts"]

    apy = None
    if row["phase"] == "CSP" and row["opened_dte"] > 0 and capital_reserved > 0:
        apy = (row["premium_collected"] * 100 * row["contracts"] / capital_reserved) * (365 / row["opened_dte"]) * 100

    break_even = row["strike"] - row["premium_collected"] if row["phase"] == "CSP" else row["strike"] + row["premium_collected"]

    return WheelPositionOut(
        **row,
        dte=dte,
        capital_reserved=capital_reserved,
        unrealized_pl=unrealized_pl,
        apy=apy,
        break_even=break_even,
    )


def list_positions() -> list[WheelPositionOut]:
    return [_compute_position(row) for row in load_positions()]


def create_position(payload: WheelPositionCreate) -> WheelPositionOut:
    rows = load_positions()
    row = payload.model_dump(mode="json")
    row["id"] = str(uuid4())
    rows.append(row)
    save_positions(rows)
    return _compute_position(row)


def update_position(position_id: str, patch: dict) -> WheelPositionOut | None:
    rows = load_positions()
    for row in rows:
        if row["id"] == position_id:
            row.update({key: value for key, value in patch.items() if value is not None})
            save_positions(rows)
            return _compute_position(row)
    return None


def delete_position(position_id: str) -> bool:
    rows = load_positions()
    kept = [row for row in rows if row["id"] != position_id]
    if len(kept) == len(rows):
        return False
    save_positions(kept)
    return True


def dashboard() -> WheelDashboardResponse:
    positions = list_positions()
    today = date.today()

    total_premium_open = sum(position.premium_collected * 100 * position.contracts for position in positions if position.status.lower() == "open")
    total_premium_mtd = sum(
        position.premium_collected * 100 * position.contracts
        for position in positions
        if date.fromisoformat(str(position.expiration)).month == today.month
    )
    total_premium_ytd = sum(
        position.premium_collected * 100 * position.contracts
        for position in positions
        if date.fromisoformat(str(position.expiration)).year == today.year
    )

    csp_positions = [position for position in positions if position.phase == "CSP"]
    csp_capital = sum(position.capital_reserved for position in csp_positions)
    weighted_apy = (
        sum((position.apy or 0) * position.capital_reserved for position in csp_positions) / csp_capital if csp_capital else 0.0
    )

    cc_positions = [position for position in positions if position.phase == "CC"]
    capital_at_risk_cc = sum(
        (position.stock_cost_basis or position.strike) * position.contracts * 100 for position in cc_positions
    )

    dte_alerts = [position for position in positions if position.dte <= 7 and position.status.lower() == "open"]

    schedule = [
        {
            "ticker": position.ticker,
            "expiration": str(position.expiration),
            "capital_release": position.capital_reserved if position.phase == "CSP" else 0,
        }
        for position in sorted(positions, key=lambda row: row.expiration)
    ]

    summary = WheelSummary(
        total_premium_open=total_premium_open,
        total_premium_mtd=total_premium_mtd,
        total_premium_ytd=total_premium_ytd,
        weighted_apy_csp=weighted_apy,
        capital_deployed_csp=csp_capital,
        capital_at_risk_cc=capital_at_risk_cc,
        next_expiration_alerts=len(dte_alerts),
    )

    return WheelDashboardResponse(
        summary=summary,
        positions=positions,
        dte_alerts=dte_alerts,
        capital_release_schedule=schedule,
    )
