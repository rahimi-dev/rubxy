import rubxy

from rubxy import enums, types
from typing import Optional, List

from .object import DictLike

class ButtonSelection(DictLike):
    def __init__(
        self,
        selection_id: Optional[str] = None,
        search_type: Optional[str] = None,
        get_type: Optional[str] = None,
        items: Optional[List["types.ButtonSelectionItem"]] = None,
        is_multi_selection: Optional[bool] = None,
        columns_count: Optional[str] = None,
        title: Optional[str] = None
    ):
        self.selection_id = selection_id
        self.search_type = search_type
        self.get_type = get_type
        self.items = items
        self.is_multi_selection = is_multi_selection
        self.columns_count = columns_count
        self.title = title