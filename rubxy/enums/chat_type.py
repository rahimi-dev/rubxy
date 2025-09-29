from enum import auto
from .auto_name import AutoName

class ChatType(AutoName):
    USER = auto()
    "Chat is a private chat with a user"

    BOT = auto()
    "Chat is a private chat with a bot"

    GROUP = auto()
    "Chat is a basic group"

    CHANNEL = auto()
    "Chat is the channel"