import rubxy

from rubxy import types
from typing import Optional, List

from .object import Object

class Poll(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        question: Optional[str] = None,
        options: Optional[List[str]] = None,
        poll_status: Optional["types.PollStatus"] = None
    ):
        super().__init__(client=client)
        
        self.question = question
        self.options = options
        self.poll_status = poll_status