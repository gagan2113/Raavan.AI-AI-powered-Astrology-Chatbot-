"""Controller logic for astrology API endpoint."""

from src.api.schemas.astrology_schema import (
    AstrologyReadingRequest,
    AstrologyReadingResponse,
    AstrologyRequest,
    AstrologyResponse,
)
from src.services.astrology_interpretation_service import astrology_interpretation_service
from src.services.astrology_service import astrology_service
from src.utils.helpers import combine_date_time, validate_location, validate_name


def handle_astrology(request: AstrologyRequest) -> AstrologyResponse:
    """Calculate planetary positions from request birth details."""
    if not validate_name(request.name) or not validate_location(request.location):
        raise ValueError("Name and location are required.")

    birth_datetime = combine_date_time(request.dob, request.time)
    julian_day = astrology_service.calculate_julian_day(birth_datetime)
    planets = astrology_service.get_planetary_positions(julian_day)

    return AstrologyResponse(planets=planets)


def handle_astrology_reading(request: AstrologyReadingRequest) -> AstrologyReadingResponse:
    """Generate a personalized astrology reading with planetarypositions and interpretation."""
    if not validate_name(request.name) or not validate_location(request.location):
        raise ValueError("Name and location are required.")

    # Calculate planetary positions
    birth_datetime = combine_date_time(request.dob, request.time)
    julian_day = astrology_service.calculate_julian_day(birth_datetime)
    planets = astrology_service.get_planetary_positions(julian_day)

    # Generate astrology reading/interpretation
    reading = astrology_interpretation_service.generate_reading(
        name=request.name,
        dob=str(request.dob),
        time=str(request.time),
        location=request.location,
        planets=planets,
    )

    return AstrologyReadingResponse(
        name=request.name,
        dob=str(request.dob),
        time=str(request.time),
        location=request.location,
        planets=planets,
        reading=reading,
    )
