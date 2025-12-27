import rubxy

from typing import Optional

from .object import Object

class File(Object):
    def __init__(
        self,
        *,
        client: Optional["rubxy.Client"] = None,
        file_id: Optional[str] = None,
        file_name: Optional[str] = None,
        size: Optional[str] = None
    ):
        super().__init__(client=client)

        self.file_id = file_id
        self.file_name = file_name
        self.size = size
