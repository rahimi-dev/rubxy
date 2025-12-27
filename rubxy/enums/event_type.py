from enum import auto
from .auto_name import AutoName

class EventType(AutoName):
    MESSAGE = auto()
    INLINE_MESSAGE = auto()