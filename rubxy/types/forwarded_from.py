import rubxy

from rubxy import enums
from typing import Optional

from .object import Object

class ForwardedFrom(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        type_from: Optional["enums.ForwardedFrom"] = None,
        id: Optional[str] = None,
        from_chat_id: Optional[str] = None,
        from_sender_id: Optional[str] = None
    ):
        super().__init__(client=client)

        self.type_from = type_from
        self.id = id
        self.from_chat_id = from_chat_id
        self.from_sender_id = from_sender_id