from .on_start import OnStart
from .on_stop import OnStop
from .on_message import OnMessage
from .on_inline_message import OnInlineMessage

class Decorators(
    OnStart,
    OnStop,
    OnMessage,
    OnInlineMessage
):
    pass