import rubxy

from rubxy import types
from typing import Union

class GetChat:
    async def get_chat(
        self: "rubxy.Client",
        chat_id: Union[str, int]
    ) -> "types.Chat":
        r = await self.invoke(
            "getChat",
            chat_id=chat_id
        )

        chat = r.get("chat", {})

        return types.Chat(
            chat_id=chat.get("chat_id"),
            chat_type=chat.get("chat_type"),
            user_id=chat.get("user_id"),
            first_name=chat.get("first_name"),
            last_name=chat.get("last_name"),
            title=chat.get("title"),
            username=chat.get("username"),
            client=self
        )