import rubxy

from rubxy import enums
from typing import Optional, List

from .object import Object

class PollStatus(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        state: Optional["enums.PollStatus"] = None,
        selection_index: Optional[int] = None,
        percent_vote_options: Optional[List[int]] = None,
        total_vote: Optional[int] = None,
        show_total_votes: Optional[bool] = None
    ):
        super().__init__(client=client)
        
        self.state = state
        self.selection_index = selection_index
        self.percent_vote_options = percent_vote_options
        self.total_vote = total_vote
        self.show_total_vote = show_total_votes