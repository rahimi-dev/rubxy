import rubxy

from rubxy import types
from typing import Optional

from .update import Update
from .object import Object

class InlineMessage(Update, Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        sender_id: Optional[str] = None,
        text: Optional[str] = None,
        file: Optional["types.File"] = None,
        location: Optional["types.Location"] = None,
        aux_data: Optional["types.AuxData"] = None,
        message_id: Optional[str] = None,
        chat_id: Optional[str] = None
    ):
        super().__init__(client=client)
        
        self.sender_id = sender_id
        self.text = text
        self.file = file
        self.location = location
        self.aux_data = aux_data
        self.message_id = message_id
        self.chat_id = chat_id