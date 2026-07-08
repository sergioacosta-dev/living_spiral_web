"""
living_spiral
=============
A Python library implementing the Dreamspell / 13-Moon calendar system
as defined by the Foundation for the Law of Time (https://www.lawoftime.org).

Quick Start
-----------
>>> from living_spiral import get_kin_for_date, get_today_moon_data
>>>
>>> # Find your galactic signature
>>> kin = get_kin_for_date(1990, 6, 15)
>>> print(kin["kin_number"], kin["tone"], kin["seal"])
>>>
>>> # Today's moon position and daily affirmation
>>> today = get_today_moon_data()
>>> if not today["is_day_out_of_time"]:
...     print(today["moon"])
...     print(today["affirmation"])
"""

from .calendar_logic import (
    get_kin_for_date,
    get_today_moon_data,
    KinData,
    MoonData,
    DayOutOfTimeData,
)
from .exceptions import LivingSpiralError, InvalidDateError, CalendarDataError
from .constants import MOON_QUESTIONS

__all__ = [
    # Core functions
    "get_kin_for_date",
    "get_today_moon_data",
    # TypedDicts
    "KinData",
    "MoonData",
    "DayOutOfTimeData",
    # Exceptions
    "LivingSpiralError",
    "InvalidDateError",
    "CalendarDataError",
    # Constants
    "MOON_QUESTIONS",
]

__version__ = "1.0.0"
__author__ = "Living Spiral"
__license__ = "MIT"
