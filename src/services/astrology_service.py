"""Service for astrology calculations using Swiss Ephemeris."""

from datetime import datetime
from typing import Any, Dict

import swisseph as swe

from src.config.settings import AstrologyConfig


class AstrologyService:
    """Calculates Julian day and planetary positions."""

    def __init__(self):
        self.zodiac_signs = AstrologyConfig.ZODIAC_SIGNS
        self.planet_emojis = AstrologyConfig.PLANET_EMOJIS

    def calculate_julian_day(self, birth_datetime: datetime) -> float:
        """Convert datetime into Julian Day number."""
        return swe.julday(
            birth_datetime.year,
            birth_datetime.month,
            birth_datetime.day,
            birth_datetime.hour + birth_datetime.minute / 60 + birth_datetime.second / 3600,
        )

    def get_planetary_positions(self, julian_day: float) -> Dict[str, Dict[str, Any]]:
        """Calculate planet positions in zodiac signs for a Julian day."""
        planets: Dict[str, Dict[str, Any]] = {}
        planet_names = [
            "Sun",
            "Moon",
            "Mars",
            "Mercury",
            "Jupiter",
            "Venus",
            "Saturn",
            "Uranus",
            "Neptune",
            "Pluto",
        ]

        planet_ids = [
            swe.SUN,
            swe.MOON,
            swe.MARS,
            swe.MERCURY,
            swe.JUPITER,
            swe.VENUS,
            swe.SATURN,
            swe.URANUS,
            swe.NEPTUNE,
            swe.PLUTO,
        ]

        try:
            for index, planet in enumerate(planet_ids):
                position, _ = swe.calc_ut(julian_day, planet)
                degrees = position[0]
                sign = int(degrees // 30)

                planet_name = planet_names[index]
                planets[planet_name] = {
                    "degrees": degrees,
                    "sign": sign,
                    "sign_name": self.zodiac_signs[sign],
                    "degree_in_sign": degrees % 30,
                    "emoji": self.planet_emojis.get(planet_name, "🪐"),
                }
        except Exception:
            return {}

        return planets


astrology_service = AstrologyService()
