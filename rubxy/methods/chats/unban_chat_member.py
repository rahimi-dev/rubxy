import rubxy

from rubxy import types

from typing import Union

class UnbanChatMember:
    async def unban_chat_member(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        user_id: Union[str, int]    
    ):
        
        r = await self.invoke(
            "unbanChatMember",
            chat_id=chat_id,
            user_id=user_id
        )

        return types.Chat(
            chat_id=chat_id,
            user_id=user_id,
            client=self
        )