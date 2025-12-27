from enum import auto
from .auto_name import AutoName

class SenderType(AutoName):
    USER = auto()
    BOT = auto()