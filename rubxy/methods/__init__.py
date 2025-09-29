from .advanced import Advanced
from .chats import Chats
from .decorators import Decorators
from .messages import Messages
from .updates import Updates
from .users import Users
from .utilities import Utilities
from .settings import Settings

class Methods(
    Advanced,
    Chats,
    Decorators,
    Messages,
    Updates,
    Users,
    Utilities,
    Settings
):
    pass