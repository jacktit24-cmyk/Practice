"""Wheel strategy routes for command-grid operations and summaries."""
from fastapi import APIRouter, HTTPException

from app.schemas.wheel import (
    WheelDashboardResponse,
    WheelPositionCreate,
    WheelPositionOut,
    WheelPositionUpdate,
)
from app.services import wheel_service

router = APIRouter(prefix="/wheel", tags=["wheel"])


@router.get("/positions", response_model=list[WheelPositionOut])
def list_wheel_positions() -> list[WheelPositionOut]:
    return wheel_service.list_positions()


@router.post("/positions", response_model=WheelPositionOut)
def create_wheel_position(payload: WheelPositionCreate) -> WheelPositionOut:
    return wheel_service.create_position(payload)


@router.patch("/positions/{position_id}", response_model=WheelPositionOut)
def update_wheel_position(position_id: str, payload: WheelPositionUpdate) -> WheelPositionOut:
    updated = wheel_service.update_position(position_id, payload.model_dump(exclude_none=True, mode="json"))
    if not updated:
        raise HTTPException(status_code=404, detail="Position not found")
    return updated


@router.delete("/positions/{position_id}")
def delete_wheel_position(position_id: str) -> dict[str, bool]:
    removed = wheel_service.delete_position(position_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Position not found")
    return {"deleted": True}


@router.get("/dashboard", response_model=WheelDashboardResponse)
def wheel_dashboard() -> WheelDashboardResponse:
    return wheel_service.dashboard()
