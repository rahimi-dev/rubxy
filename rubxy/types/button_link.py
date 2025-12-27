from rubxy import types
from typing import Optional

from .object import DictLike

class ButtonLink(DictLike):
    def __init__(
        self,
        link_url: Optional[str] = None,
        joinchannel_data: Optional["types.JoinChannelData"] = None,
        open_chat_data: Optional["types.OpenChatData"] = None
    ):
        self.link_url = link_url
        self.joinchannel_data = joinchannel_data
        self.open_chat_data = open_chat_data