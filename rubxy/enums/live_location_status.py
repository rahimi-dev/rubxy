from enum import auto
from .auto_name import AutoName

class LiveLocationStatus(AutoName):
    STOPPED = auto()
    "Stopped status"

    LIVE = auto()
    "Live online status"