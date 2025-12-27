import rubxy

from rubxy import enums
from rubxy.filters import Filter
from typing import Optional, Callable

from .handler import Handler

class MessageHandler(Handler):
    def __init__(
        self,
        callback: Callable,
        filters: Optional[Filter] = None,
    ):
        super().__init__(
            callback=callback,
            filters=filters,
            event_type=enums.EventType.MESSAGE
        )