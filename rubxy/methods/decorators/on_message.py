import rubxy
import inspect

from rubxy import handlers
from rubxy.filters import Filter
from typing import Optional

class OnMessage:
    def on_message(
        self: "rubxy.Client",
        *filters: Optional[Filter],
        group: int = 0
    ):
        def decorator(func):
            if not inspect.iscoroutinefunction(func):
                raise TypeError("The passed function must be asynchronous.")
            
            self.add_handler(
                handlers.MessageHandler(func, *filters),
                group=group
            )
            
            return func
        return decorator