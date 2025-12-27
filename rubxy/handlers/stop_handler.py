import rubxy

from rubxy import enums
from typing import Optional, Callable

from .handler import Handler

class StopHandler(Handler):
    def __init__(
        self,
        callback: Callable,
    ):
        super().__init__(callback=callback)