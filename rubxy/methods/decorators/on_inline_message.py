import rubxy
import warnings

from rubxy import handlers
from rubxy.filters import Filter
from typing import Optional, Union

class OnInlineMessage:
    def on_inline_message(
        self: Union["rubxy.Client", "Filter"] = None,
        filters: Optional[Filter] = None,
        group: int = 0
    ):
        def decorator(func):
            if isinstance(self, rubxy.Client):
                self.add_handler(
                    handlers.InlineMessageHandler(func, filters),
                    group=group
                )
            
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []
                
                func.handlers.append(
                    (
                        handlers.InlineMessageHandler(func, self),
                        group if filters is None else filters
                    )
                )
            
            return func
        return decorator