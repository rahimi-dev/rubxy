import rubxy

from rubxy import types

from typing import Union

class BanChatMember:
    async def ban_chat_member(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        user_id: Union[str, int]
    ) -> "types.Chat":
        r = await self.invoke(
            "banChatMember",
            chat_id=chat_id,
            user_id=user_id
        )

        return types.Chat(
            chat_id=chat_id,
            user_id=user_id,
            client=self
        )