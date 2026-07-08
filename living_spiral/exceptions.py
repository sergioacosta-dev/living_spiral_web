"""
exceptions.py
Custom exception types for the living_spiral library.
"""


class LivingSpiralError(Exception):
    """Base exception for all living_spiral errors."""


class InvalidDateError(LivingSpiralError):
    """Raised when a date is invalid or outside the supported range."""

    def __init__(self, message: str, year: int = None, month: int = None, day: int = None):
        self.year = year
        self.month = month
        self.day = day
        super().__init__(message)


class CalendarDataError(LivingSpiralError):
    """Raised when required calendar data (JSON, text files) cannot be loaded."""
