import rubxy

from rubxy import types, enums
from typing import Optional, Union

class SendContact:
    async def send_contact(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        first_name: str,
        last_name: str,
        phone_number: Union[str, int],
        disable_notification: Optional[bool] = False,
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        reply_to_message_id: Optional[int] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ) -> "types.Message":
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
            "sendContact",
            chat_id=chat_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
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