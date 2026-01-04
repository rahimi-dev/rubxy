import rubxy

from rubxy import types
from typing import Union, Optional

class EditMessageText:
    async def edit_message_text(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        text: str,
        message_id: Union[str, int],
    ) -> "types.Message":
        r = await self.invoke(
            "editMessageText",
            text=text,
            chat_id=chat_id,
            message_id=message_id,
        )

        return types.Message(
            text=text,
            chat_id=chat_id,
            id=message_id,
            client=self
        )