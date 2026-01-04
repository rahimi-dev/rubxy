import rubxy

from rubxy import types, enums
from typing import Optional, Union

class EditMessageKeypad:
    async def edit_message_keypad(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        message_id: Union[str, int],
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ):
        if any(
            (
                chat_keypad,
                inline_keypad
            )
        ):
            if isinstance(chat_keypad, types.Keypad):
                chat_keypad = chat_keypad._to_dict()
                chat_keypad_type = enums.ChatKeypadType.NEW
            elif isinstance(inline_keypad, types.Keypad):
                inline_keypad = inline_keypad._to_dict()
            else:
                raise TypeError("`chat_keypad` or `inline_keypad` must be of type `types.Keypad`")

        r = await self.invoke(
            "editMessageKeypad",
            chat_id=chat_id,
            message_id=message_id,
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad,
            chat_keypad_type=chat_keypad_type
        )

        return types.Message(
            chat_id=chat_id,
            id=message_id,
            client=self
        )