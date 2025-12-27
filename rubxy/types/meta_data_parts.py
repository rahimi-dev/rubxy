from typing import Optional

from .object import DictLike

class MetaDataParts(DictLike):
    def __init__(
        self,
        from_index: Optional[int] = None,
        length: Optional[int] = None,
        type: Optional[str] = None,
        link_url: Optional[str] = None,
        mention_text_user_id: Optional[str] = None,
    ):
        self.from_index = from_index
        self.length = length
        self.type = type
        self.link_url = link_url
        self.mention_text_user_id = mention_text_user_id