import rubxy
import asyncio

from rubxy import types, enums, utils
from typing import Optional, Union

class SendMessage:
    async def send_message(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        text: str,
        disable_notification: Optional[bool] = False,
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        reply_to_message_id: Optional[int] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ) -> "types.Message":
        chat_keypad, inline_keypad, chat_keypad_type = utils.keypad_parse(chat_keypad, inline_keypad, chat_keypad_type)
            
        r = await self.invoke(
            "sendMessage",
            text=text,   
            chat_id=chat_id,
            disable_notification=disable_notification,
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad,
            reply_to_message_id=reply_to_message_id,
            chat_keypad_type=chat_keypad_type
        )

        return types.Message(
            chat_id=chat_id,
            id=r.get("message_id"),
            client=self
        )