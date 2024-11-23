from datetime import datetime

def parse_date(date_str: str) -> datetime:
    """
    Parse a date string in ISO format and return a datetime object.
    """
    return datetime.fromisoformat(date_str)