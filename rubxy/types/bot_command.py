from typing import Optional

from .object import DictLike

class BotCommand(DictLike):
    def __init__(
        self,
        command: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.command = command.strip('/') if command else command
        self.description = description