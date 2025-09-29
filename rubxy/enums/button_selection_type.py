from enum import auto
from .auto_name import AutoName

class ButtonSelectionType(AutoName):
    TEXT_ONLY = auto()
    "Display button as text"

    TEXT_IMG_THU = auto()
    "Display button as text and thumbnail"

    TEXT_IMG_BIG = auto()
    "Display the button as text and large image"