from typing import Optional
from rubxy import enums, types

from .object import DictLike

class Button(DictLike):
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[enums.ButtonType] = enums.ButtonType.SIMPLE,
        button_text: Optional[str] = None,
        button_selection: Optional["types.ButtonSelection"] = None,
        button_calendar: Optional["types.ButtonCalendar"] = None,
        button_number_picker: Optional["types.ButtonNumberPicker"] = None,
        button_string_picker: Optional["types.ButtonStringPicker"] = None,
        button_location: Optional["types.ButtonLocation"] = None,
        button_textbox: Optional["types.ButtonTextbox"] = None,
    ):
        self.id = id
        self.type = type
        self.button_text = button_text
        self.button_selection = button_selection
        self.button_calendar = button_calendar
        self.button_number_picker = button_number_picker
        self.button_string_picker = button_string_picker
        self.button_location = button_location
        self.button_textbox = button_textbox