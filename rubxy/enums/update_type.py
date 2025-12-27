from enum import auto
from .auto_name import AutoName

class UpdateType(AutoName):
    UPDATED_MESSAGE = auto()
    "Update message, like edit message"

    NEW_MESSAGE = auto()
    "New message"

    REMOVED_MESSAGE = auto()
    "Remove message"

    STARTED_BOT = auto()
    "Started bot"

    STOPPED_BOT = auto()
    "Stopped bot"

    UPDATED_PAYMENT = auto()
    "Updated payment"