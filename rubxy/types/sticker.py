import rubxy

from rubxy import types
from typing import Optional

from .object import Object

class Sticker(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        sticker_id: Optional[str] = None,
        file: Optional["types.File"] = None,
        emoji_character: Optional[str] = None
    ):
        super().__init__(client=client)

        self.sticker_id = sticker_id
        self.file = file
        self.emoji_character = emoji_character