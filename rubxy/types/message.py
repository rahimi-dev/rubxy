import rubxy

from rubxy import enums, types
from typing import Optional, List, Match

from .update import Update
from .object import Object

class Message(Update, Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        chat_id: Optional[str] = None,
        id: Optional[str] = None,
        text: Optional[str] = None,
        time: Optional[int] = None,
        is_edited: Optional[bool] = None,
        sender_type: Optional["enums.SenderType"] = None,
        sender_id: Optional[str] = None,
        aux_data: Optional["types.AuxData"] = None,
        file: Optional["types.File"] = None,
        reply_to_message_id: Optional[str] = None,
        forwarded_from: Optional["types.ForwardedFrom"] = None,
        matches: Optional[List[Match]] = None,
        metadata: Optional["types.MetaData"] = None
    ):
        super().__init__(client=client)
        
        self.chat_id = chat_id
        self.id = id
        self.text = text
        self.time = time
        self.is_edited = is_edited
        self.sender_type = sender_type
        self.sender_id = sender_id
        self.aux_data = aux_data
        self.file = file
        self.reply_to_message_id = reply_to_message_id
        self.forwarded_from = forwarded_from
        self.matches = matches
        self.metadata = metadata
