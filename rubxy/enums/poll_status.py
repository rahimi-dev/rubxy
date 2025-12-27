from enum import auto
from .auto_name import AutoName

class PollStatus(AutoName):
    OPEN = auto()
    "Poll is open"

    CLOSED = auto()
    "Poll is closed"