import rubxy

from rubxy import enums, types
from typing import Optional

from .object import DictLike

class ButtonLocation(DictLike):
    def __init__(
        self,
        default_pointer_location: Optional["types.Location"] = None,
        default_map_location: Optional["types.Location"] = None,
        type: Optional["enums.ButtonLocationType"] = None,
        title: Optional[str] = None,
        location_image_url: Optional[str] = None
    ):
        self.default_pointer_location = default_pointer_location
        self.default_map_location = default_map_location
        self.type = type
        self.title = title
        self.location_image_url = location_image_url