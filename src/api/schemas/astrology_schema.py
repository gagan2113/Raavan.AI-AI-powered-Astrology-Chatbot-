"""Schemas for astrology endpoint payloads."""

import datetime as dt
from typing import Dict

from pydantic import BaseModel, Field


class AstrologyRequest(BaseModel):
    """Schema for astrology input payload."""

    name: str = Field(..., min_length=1, description="Full name of the person")
    dob: dt.date = Field(..., description="Birth date in YYYY-MM-DD format")
    time: dt.time = Field(..., description="Birth time in HH:MM format")
    location: str = Field(..., min_length=1, description="Birth location")


class PlanetPosition(BaseModel):
    """Schema for a single planet position in response."""

    degrees: float
    sign: int
    sign_name: str
    degree_in_sign: float
    emoji: str


class AstrologyResponse(BaseModel):
    """Schema for astrology output payload."""

    planets: Dict[str, PlanetPosition]


class AstrologyReadingRequest(BaseModel):
    """Schema for requesting a full astrology reading (includes interpretation)."""

    name: str = Field(..., min_length=1, description="Full name of the person")
    dob: dt.date = Field(..., description="Birth date in YYYY-MM-DD format")
    time: dt.time = Field(..., description="Birth time in HH:MM format")
    location: str = Field(..., min_length=1, description="Birth location")


class AstrologyReadingResponse(BaseModel):
    """Schema for astrology reading response with interpretation."""

    name: str
    dob: str
    time: str
    location: str
    planets: Dict[str, PlanetPosition]
    reading: str = Field(..., description="Personalized astrology reading/interpretation")
