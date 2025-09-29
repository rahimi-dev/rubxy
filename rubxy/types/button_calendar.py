import rubxy

from rubxy import enums
from typing import Optional

from .object import DictLike

class ButtonCalendar(DictLike):
    def __init__(
        self,
        default_value: Optional[str] = None,
        type: Optional["enums.ButtonCalendarType"] = None,
        min_year: Optional[str] = None,
        max_year: Optional[str] = None,
        title: Optional[str] = None
    ):
        self.default_value = default_value
        self.type = type
        self.min_year = min_year
        self.max_year = max_year
        self.title = title