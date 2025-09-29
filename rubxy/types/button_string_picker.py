import rubxy

from typing import Optional, List

from .object import DictLike

class ButtonStringPicker(DictLike):
    def __init__(
        self,
        items: Optional[List[str]] = None,
        default_value: Optional[str] = None,
        title: Optional[str] = None
    ):
        self.items = items
        self.default_value = default_value
        self.title = title