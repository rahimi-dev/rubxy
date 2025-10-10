import rubxy
import warnings

from rubxy import handlers
from rubxy.filters import Filter
from typing import Optional

class OnInlineMessage:
    def on_inline_message(
        self: "rubxy.Client",
        filters: Optional[Filter] = None,
        group: int = 0
    ):
        if self.is_long_polling:
            warnings.warn(
                "Note: long-polling cannot receive `InlineMessage` updates",
                UserWarning
            )

        def decorator(func):
            self.add_handler(
                handlers.InlineMessageHandler(func, filters),
                group=group
            )
            
            return func
        return decorator