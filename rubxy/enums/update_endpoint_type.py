from enum import auto
from .auto_name import AutoName

class UpdateEndpointType(AutoName):
    RECEIVE_UPDATE = auto()
    RECEIVE_INLINE_MESSAGE = auto()
    RECEIVE_QUERY = auto()
    GET_SELECTION_ITEM = auto()
    SEARCH_SELECTION_ITEMS = auto()