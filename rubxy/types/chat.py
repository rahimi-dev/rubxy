import rubxy

from rubxy import enums
from typing import Optional

from .object import Object

class Chat(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        chat_id: Optional[str] = None,
        chat_type: Optional["enums.ChatType"] = None,
        user_id: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        title: Optional[str] = None,
        username: Optional[str] = None
    ):
        super().__init__(client=client)
        
        self.chat_id = chat_id
        self.chat_type = chat_type
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.username = username