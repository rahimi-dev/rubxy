from enum import auto
from .auto_name import AutoName

class ChatKeypadType(AutoName):
    NONE = auto()
    "None type, default"

    NEW = auto()
    "Add new keypad"

    REMOVE = auto()
    "Remove keypad"