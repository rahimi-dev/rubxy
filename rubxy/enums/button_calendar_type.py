from enum import auto
from .auto_name import AutoName

class ButtonCalendarType(AutoName):
    DATE_PERSIAN = auto()
    "Display calendar in Persian format"

    DATE_GREGORIAN = auto()
    "Display calendar in Gregorian format"