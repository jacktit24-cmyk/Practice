from datetime import date, timedelta

from app.models import wheel as wheel_model
from app.schemas.wheel import WheelPositionCreate
from app.services import wheel_service


def test_wheel_dashboard_summary(tmp_path) -> None:
    original = wheel_model.DATA_PATH
    wheel_model.DATA_PATH = tmp_path / "wheel_positions.json"
    try:
        exp = date.today() + timedelta(days=14)
        wheel_service.create_position(
            WheelPositionCreate(
                ticker="AAPL",
                phase="CSP",
                contracts=1,
                strike=170,
                expiration=exp,
                premium_collected=2.0,
                current_option_value=1.0,
                opened_dte=30,
                status="Open",
                stock_cost_basis=170,
                linked_cycle_id=None,
            )
        )

        dashboard = wheel_service.dashboard()
        assert dashboard.summary.total_premium_open > 0
        assert len(dashboard.positions) == 1
        assert dashboard.positions[0].dte >= 0
    finally:
        wheel_model.DATA_PATH = original
