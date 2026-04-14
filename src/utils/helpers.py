"""Helper utilities used by API controllers and services."""

from datetime import date, datetime, time


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
    return bool(name and name.strip() != "")


def validate_location(location: str) -> bool:
    """
    Validate if location is provided and not empty.
    
    Args:
        location (str): Location to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    return bool(location and location.strip() != "")


def combine_date_time(date_obj: date, time_obj: time) -> datetime:
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
