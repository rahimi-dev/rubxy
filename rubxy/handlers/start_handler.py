import rubxy

from rubxy import enums
from rubxy.filters import Filter
from typing import Optional, Callable

from .handler import Handler

class StartHandler(Handler):
    def __init__(
        self,
        callback: Callable,
    ):
        super().__init__(callback=callback)