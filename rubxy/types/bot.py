import rubxy

from rubxy import types
from typing import Optional

from .object import Object

class Bot(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        bot_id: Optional[str] = None,
        bot_title: Optional[str] = None,
        avatar: Optional["types.File"] = None,
        description: Optional[str] = None,
        username: Optional[str] = None,
        start_message: Optional[str] = None,
        share_url: Optional[str] = None,
    ):
        super().__init__(client=client)
        
        self.bot_id = bot_id
        self.bot_title = bot_title
        self.avatar = avatar
        self.description = description
        self.username = username
        self.start_message = start_message
        self.share_url = share_url