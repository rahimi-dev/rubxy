from rubxy import enums
from typing import Optional

from .object import DictLike

class OpenChatData(DictLike):
    def __init__(
        self,
        object_guid: Optional[str] = None,
        object_type: Optional["enums.ChatType"] = None
    ):
        self.object_guid = object_guid
        self.object_type = object_type