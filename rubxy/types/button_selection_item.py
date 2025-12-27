import rubxy

from rubxy import enums
from typing import Optional

from .object import DictLike

class ButtonSelectionItem(DictLike):
    def __init__(
        self,
        text: Optional[str] = None,
        image_url: Optional[str] = None,
        type: Optional["enums.ButtonSelectionType"] = None,
    ):
        self.text = text
        self.image_url = image_url
        self.type = type