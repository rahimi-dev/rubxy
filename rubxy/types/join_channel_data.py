from typing import Optional

from .object import DictLike

class JoinChannelData(DictLike):
    def __init__(
        self,
        username: Optional[str] = None,
        ask_join: Optional[bool] = False
    ):
        self.username = username.replace("@", "") if username else username
        self.ask_join = ask_join        