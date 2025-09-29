import rubxy

from rubxy import types
from typing import Union, Optional

class ForwardMessage:
    async def forward_message(
        self: "rubxy.Client",
        from_chat_id: Union[str, int],
        message_id: Union[str, int],
        to_chat_id: Union[str, int],
        disable_notification: Optional[bool] = False
    ) -> "types.Message":
        r = await self.invoke(
            "forwardMessage",
            from_chat_id=from_chat_id,
            message_id=message_id,
            to_chat_id=to_chat_id,
            disable_notification=disable_notification
        )

        return types.Message(
            id=r.get("new_message_id"),
            client=self
        )