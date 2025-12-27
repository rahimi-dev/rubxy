from enum import auto
from .auto_name import AutoName

class ButtonSelectionGet(AutoName):
    LOCAL = auto()
    "Display list items using the values sent in the items field"

    API = auto()
    "Search list items via API"