import rubxy

from rubxy import types, enums
from typing import Optional, Union, Dict

class SendMessage:
    async def send_message(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        text: str,
        metadata: Optional[Union[Dict, "types.MetaData"]] = None,
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

        if isinstance(metadata, types.MetaData):
            metadata = metadata.__dict__
        else:
            text, metadata = self.markdown.parser(text).values()
        
        r = await self.invoke(
            "sendMessage",
            text=text,
            metadata=metadata,
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