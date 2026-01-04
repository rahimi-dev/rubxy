from .send_message import SendMessage
from .send_contact import SendContact
from .send_location import SendLocation
from .send_poll import SendPoll
from .edit_message_text import EditMessageText
from .edit_message_keypad import EditMessageKeypad
from .delete_message import DeleteMessage
from .forward_message import ForwardMessage
from .request_send_file import RequestSendFile
from .get_file import GetFile
from .send_file import SendFile
from .upload_file import UploadFile

class Messages(
    SendMessage,
    SendContact,
    SendLocation,
    SendPoll,
    DeleteMessage,
    EditMessageText,
    EditMessageKeypad,
    ForwardMessage,
    RequestSendFile,
    GetFile,
    SendFile,
    UploadFile
):
    pass