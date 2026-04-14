"""Astrology route definitions."""

from fastapi import APIRouter, HTTPException

from src.api.controllers.astrology_controller import handle_astrology, handle_astrology_reading
from src.api.schemas.astrology_schema import (
    AstrologyReadingRequest,
    AstrologyReadingResponse,
    AstrologyRequest,
    AstrologyResponse,
)

router = APIRouter()


@router.post("/astrology", response_model=AstrologyResponse, summary="Get planetary positions")
def astrology(request: AstrologyRequest) -> AstrologyResponse:
    """Calculate horoscope planetary positions from birth details."""
    try:
        return handle_astrology(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Error calculating horoscope: {str(exc)}") from exc


@router.post(
    "/astrology-reading",
    response_model=AstrologyReadingResponse,
    summary="Get full astrology reading with interpretation",
)
def astrology_reading(request: AstrologyReadingRequest) -> AstrologyReadingResponse:
    """Generate a full personalized astrology reading with planetary positions and interpretation."""
    try:
        return handle_astrology_reading(request)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Error generating astrology reading: {str(exc)}") from exc
