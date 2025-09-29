import rubxy

from typing import Optional

from .object import Object

class Contact(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        phone_number: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None
    ):
        super().__init__(client=client)
        
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name