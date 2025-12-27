import rubxy

from typing import Optional

from .object import DictLike

class ButtonNumberPicker(DictLike):
    def __init__(
        self,
        min_value: Optional[str] = None,
        max_value: Optional[str] = None,
        default_value: Optional[str] = None,
        title: Optional[str] = None
    ):
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value
        self.title = title
