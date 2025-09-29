import rubxy

from rubxy import types, enums, utils
from typing import Optional, Union

class EditChatKeypad:
    async def edit_chat_keypad(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        message_id: Union[str, int],
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ):
        chat_keypad, inline_keypad = utils.keypad_parse(chat_keypad, inline_keypad, chat_keypad_type)

        r = await self.invoke(
            "editChatKeypad",
            chat_id=chat_id,
            message_id=message_id,
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad
        )

        return types.Message(
            chat_id=chat_id,
            id=message_id,
            client=self
        )