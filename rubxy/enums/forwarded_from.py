from enum import auto
from .auto_name import AutoName

class ForwardedFrom(AutoName):
    USER = auto()
    "Forward from user"

    CHANNEL = auto()
    "Forward from channel"

    BOT = auto()
    "Forward from bot"