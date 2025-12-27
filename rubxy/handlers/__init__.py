from .message_handler import MessageHandler
from .inline_message_handler import InlineMessageHandler
from .start_handler import StartHandler
from .stop_handler import StopHandler
from .handler import Handler

class Handlers(
    MessageHandler,
    InlineMessageHandler,
    StartHandler,
    StopHandler
):
    pass