from enum import auto
from .auto_name import AutoName

class ButtonSelectionSearch(AutoName):
    NONE = auto()
    "Default state"

    LOCAL = auto()
    "Search list items using the values sent in the items field"

    API = auto()
    "Search list items via API"