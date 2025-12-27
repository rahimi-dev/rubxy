from enum import auto
from .auto_name import AutoName

class ButtonTextboxTypeKeypad(AutoName):
    STRING = auto()
    "Allows sending all characters"

    NUMBER = auto()
    "Allows sending numeric characters"