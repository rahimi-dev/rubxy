from .get_chat import GetChat
from .ban_chat_member import BanChatMember
from .unban_chat_member import UnbanChatMember

class Chats(
    GetChat,
    BanChatMember,
    UnbanChatMember
):
    pass