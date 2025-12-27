import rubxy

from rubxy import types, enums, utils
from filetype import guess_mime

from typing import Union, Optional

class SendFile:
    async def send_file(
        self: "rubxy.Client",
        chat_id: Union[str, int],
        file_id: Union[str, int] = None,
        file: Union[str, bytes] = None,
        file_name: Optional[str] = None,
        file_type: Optional["enums.FileType"] = None,
        text: str = None,
        reply_to_message_id: Optional[int] = None,
        disable_notification: Optional[bool] = False,
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ):
        chat_keypad, inline_keypad, chat_keypad_type = utils.keypad_parse(chat_keypad, inline_keypad, chat_keypad_type)
        
        if not file_id:
            if isinstance(file, str):
                file = open(file, "rb")
            elif isinstance(file, bytes):
                pass
            else:
                raise TypeError("`file` must be of type bytes or str, not %s"%type(file))
            
            if file_type is None:
                guess = guess_mime(file)
                file_type = guess.split('/')[0].capitalize()

                if file_type not in list(enums.FileType):
                    raise TypeError(f"filetype not allowed, allowed types: {list(enums.FileType)}")

            upload_url = await self.request_send_file(file_type)
            file_id = await self.upload_file(upload_url, file, file_name)

        r = await self.invoke(
            "sendFile",
            chat_id=chat_id,
            file_id=file_id,
            text=text,
            reply_to_message_id=reply_to_message_id,
            disable_notification=disable_notification,
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad,
            chat_keypad_type=chat_keypad_type
        )

        return types.Message(
            chat_id=chat_id,
            text=text,
            id=r.get("message_id"),
            reply_to_message_id=reply_to_message_id,
            client=self
        )