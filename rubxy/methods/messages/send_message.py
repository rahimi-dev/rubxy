import rubxy

from rubxy import types, enums, utils
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
        chat_keypad, inline_keypad, chat_keypad_type = utils.keypad_parse(chat_keypad, inline_keypad, chat_keypad_type)

        if (
            text and
            metadata is None
        ):
            _parse = self._formatter.to_metadata(text)
            text, metadata = _parse["text"], _parse["metadata"]
        
        elif isinstance(metadata, types.MetaData):
            metadata = metadata.__dict__
        
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