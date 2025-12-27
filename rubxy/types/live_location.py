import rubxy

from rubxy import types, enums
from typing import Optional

from .object import Object

class LiveLocation(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        start_time: Optional[str] = None,
        live_period: Optional[str] = None,
        current_location: Optional["types.Location"] = None,
        user_id: Optional[str] = None,
        status: Optional["enums.LiveLocationStatus"] = None,
        last_update_time: Optional[str] = None
    ):
        super().__init__(client=client)

        self.start_time = start_time
        self.live_period = live_period
        self.current_location = current_location
        self.user_id = user_id
        self.status = status
        self.last_update_time = last_update_time