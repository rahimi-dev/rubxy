from enum import auto
from .auto_name import AutoName

class ParseMode(AutoName):
    MARKDOWN = auto()
    HTML = auto()