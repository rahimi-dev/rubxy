import rubxy

from rubxy import types, enums, utils
from typing import Optional, Union

class EditMessage:
    async def edit_message(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        text: str,
        message_id: Union[str, int],
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ) -> "types.Message":
        r = await self.edit_message_text(
            text=text,
            chat_id=chat_id,
            message_id=message_id
        )

        if utils.anies(chat_keypad, inline_keypad):
            if inline_keypad:
                await self.edit_message_keypad(
                    chat_id=r.chat_id,
                    message_id=r.id,
                    chat_keypad=chat_keypad,
                    inline_keypad=inline_keypad,
                    chat_keypad_type=chat_keypad_type
                )
        
        return r