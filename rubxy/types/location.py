import rubxy

from typing import Optional
from .object import Object

class Location(Object):
    def __init__(
        self,
        client: "rubxy.Client" = None,
        longitude: Optional[str] = None,
        latitude: Optional[str] = None
    ):
        super().__init__(client=client)
        
        self.longitude = longitude
        self.latitude = latitude    