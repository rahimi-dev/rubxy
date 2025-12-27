import rubxy

from rubxy import types

from typing import Optional, List

from .object import DictLike

class MetaData(DictLike):
    def __init__(
        self,
        meta_data_parts: Optional[List["types.MetaDataParts"]],
    ):
        self.meta_data_parts = meta_data_parts