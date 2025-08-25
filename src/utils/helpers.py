"""
Utility functions for various operations.
Contains helper functions for formatting, validation, and calculations.
"""

import swisseph as swe
from datetime import datetime, time
from typing import Dict, Any, List
from config.settings import AstrologyConfig


def format_datetime_display(dt: datetime) -> str:
    """
    Format datetime for display.
    
    Args:
        dt (datetime): Datetime object to format
        
    Returns:
        str: Formatted datetime string
    """
    return dt.strftime('%B %d, %Y at %I:%M %p')


def get_default_birth_time() -> time:
    """
    Get default birth time (12:00 PM).
    
    Returns:
        time: Default time object
    """
    return datetime.strptime("12:00", "%H:%M").time()


def validate_name(name: str) -> bool:
    """
    Validate if name is provided and not empty.
    
    Args:
        name (str): Name to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    return name and name.strip() != ""


def validate_location(location: str) -> bool:
    """
    Validate if location is provided and not empty.
    
    Args:
        location (str): Location to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    return location and location.strip() != ""


class AstrologyCalculator:
    """Utility class for astrology calculations using Swiss Ephemeris"""
    
    def __init__(self):
        self.zodiac_signs = AstrologyConfig.ZODIAC_SIGNS
        self.planet_emojis = AstrologyConfig.PLANET_EMOJIS
    
    def calculate_julian_day(self, birth_datetime: datetime) -> float:
        """
        Calculate Julian Day from datetime.
        
        Args:
            birth_datetime (datetime): Birth date and time
            
        Returns:
            float: Julian Day number
        """
        return swe.julday(
            birth_datetime.year,
            birth_datetime.month,
            birth_datetime.day,
            birth_datetime.hour + birth_datetime.minute / 60 + birth_datetime.second / 3600
        )
    
    def get_planetary_positions(self, julian_day: float) -> Dict[str, Dict[str, Any]]:
        """
        Calculate planetary positions for given Julian Day.
        
        Args:
            julian_day (float): Julian Day number
            
        Returns:
            Dict[str, Dict[str, Any]]: Planetary positions data
        """
        planets = {}
        planet_names = [
            "Sun", "Moon", "Mars", "Mercury", "Jupiter",
            "Venus", "Saturn", "Uranus", "Neptune", "Pluto"
        ]
        
        planet_ids = [
            swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER,
            swe.VENUS, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO
        ]
        
        try:
            for i, planet in enumerate(planet_ids):
                position, ret = swe.calc_ut(julian_day, planet)
                degrees = position[0]  # Longitude in the zodiac
                sign = int(degrees // 30)
                
                planets[planet_names[i]] = {
                    "degrees": degrees,
                    "sign": sign,
                    "sign_name": self.zodiac_signs[sign],
                    "degree_in_sign": degrees % 30,
                    "emoji": self.planet_emojis.get(planet_names[i], "🪐")
                }
        except Exception as e:
            # Return empty dict if calculation fails
            return {}
        
        return planets
    
    def format_planetary_display(self, planets: Dict[str, Dict[str, Any]]) -> List[str]:
        """
        Format planetary positions for display.
        
        Args:
            planets (Dict[str, Dict[str, Any]]): Planetary positions
            
        Returns:
            List[str]: Formatted strings for display
        """
        formatted_results = []
        
        for planet, details in planets.items():
            emoji = details.get("emoji", "🪐")
            formatted_text = f"""
            **{emoji} {planet}:**  
            🔸 Sign: {details['sign_name']}  
            🔸 Position: {details['degrees']:.2f}°  
            🔸 Degree in Sign: {details['degree_in_sign']:.2f}°  
            """
            formatted_results.append(formatted_text)
        
        return formatted_results


def combine_date_time(date_obj, time_obj) -> datetime:
    """
    Combine date and time objects into datetime.
    
    Args:
        date_obj: Date object
        time_obj: Time object
        
    Returns:
        datetime: Combined datetime object
    """
    return datetime.combine(date_obj, time_obj)


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to maximum length with ellipsis.
    
    Args:
        text (str): Text to truncate
        max_length (int): Maximum length
        
    Returns:
        str: Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
