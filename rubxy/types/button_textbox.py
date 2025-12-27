from rubxy import enums
from typing import Optional

from .object import DictLike

class ButtonTextbox(DictLike):
    def __init__(
        self,
        type_line: Optional["enums.ButtonTextboxTypeLine"] = None,
        type_keypad: Optional[enums.ButtonTextboxTypeKeypad] = None,
        place_holder: Optional[str] = None,
        title: Optional[str] = None,
        default_value: Optional[str] = None
    ):
        self.type_line = type_line
        self.type_keypad = type_keypad
        self.place_holder = place_holder
        self.title = title
        self.default_value = default_value