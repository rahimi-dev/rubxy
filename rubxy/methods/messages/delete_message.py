import rubxy

from rubxy import types
from typing import Union

class DeleteMessage:
    async def delete_message(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        message_id: Union[str, int]
    ) -> "types.Message":
        r = await self.invoke(
            "deleteMessage",
            chat_id=chat_id,
            message_id=message_id
        )

        return types.Message(
            chat_id=chat_id,
            id=message_id,
            client=self
        )