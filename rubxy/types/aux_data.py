import rubxy

from typing import Optional

from .object import Object

class AuxData(Object):
    def __init__(
        self,
        *, 
        client: "rubxy.Client" = None,
        start_id: Optional[str] = None,
        button_id: Optional[str] = None
    ):
        super().__init__(client=client)
        
        self.start_id = start_id
        self.button_id = button_id