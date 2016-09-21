from datetime import datetime

import pytz

__all__ = [
    'utc_now',
]


def utc_now():
    """
    Returns current UTC time and sets the time zone info
    to UTC
    """
    d = datetime.utcnow()
    return d.replace(tzinfo=pytz.UTC)
