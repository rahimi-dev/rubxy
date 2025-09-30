import rubxy

from rubxy import enums
from rubxy.filters import Filter
from typing import Optional, Callable

from .handler import Handler

class InlineMessageHandler(Handler):
    def __init__(
        self,
        callback: Callable,
        filters: Optional[Filter] = None,
    ):
        super().__init__(
            callback=callback,
            filters=filters,
            event_type=enums.EventType.INLINE_MESSAGE
        )