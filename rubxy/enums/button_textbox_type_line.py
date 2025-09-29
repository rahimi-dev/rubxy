from enum import auto
from .auto_name import AutoName

class ButtonTextboxTypeLine(AutoName):
    SINGLE_LINE = auto()
    "Write text message in a single line"

    MULTI_LINE = auto()
    "Write text message in multiple lines"