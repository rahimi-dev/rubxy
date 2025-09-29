from .send_message import SendMessage
from .send_contact import SendContact
from .send_location import SendLocation
from .send_poll import SendPoll
from .edit_message import EditMessage
from .edit_message_text import EditMessageText
from .edit_message_keypad import EditMessageKeypad
from .delete_message import DeleteMessage
from .forward_message import ForwardMessage

class Messages(
    SendMessage,
    SendContact,
    SendLocation,
    SendPoll,
    DeleteMessage,
    EditMessage,
    EditMessageText,
    EditMessageKeypad,
    ForwardMessage
):
    pass