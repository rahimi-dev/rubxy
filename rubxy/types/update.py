import rubxy

from rubxy import enums, types
from typing import Union, Optional, Match

from .object import Object

class Update(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        type: Optional["enums.UpdateType"] = None,
        chat_id: Optional[str] = None,
        removed_message_id: Optional[str] = None,
        new_message: Optional["types.Message"] = None,
        updated_message: Optional["types.Message"] = None,
        updated_payment: Optional["types.PaymentStatus"] = None,
        matches: Optional[list[Match]] = None
    ):
        super().__init__(client=client)
        
        self.type = type
        self.chat_id = chat_id
        self.removed_message_id = removed_message_id
        self.new_message = new_message
        self.updated_message = updated_message
        self.updated_payment = updated_payment
        self.matches = matches

    async def reply(
        self: Union["types.Update", "types.Message", "types.InlineMessage"],
        text: str,
        qoute: Optional[bool] = None,
        chat_id: Optional[str] = None,
        disable_notification: Optional[bool] = False,
        chat_keypad: Optional["types.Keypad"] = None,
        inline_keypad: Optional["types.Keypad"] = None,
        reply_to_message_id: Optional[str] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = enums.ChatKeypadType.NONE
    ):
        if qoute is None:
            qoute = not self.chat_id.startswith(('u', 'b')) # true if message in group
        
        if qoute and reply_to_message_id is None:
            reply_to_message_id = self.message_id or self.new_message.id or self.updated_message.id

        return await self._client.send_message(
            text=text,
            chat_id=chat_id or self.chat_id,
            disable_notification=disable_notification,
            chat_keypad=chat_keypad,
            inline_keypad=inline_keypad,
            reply_to_message_id=reply_to_message_id,
            chat_keypad_type=chat_keypad_type
        )
    
    async def delete(
        self: Union["types.Update", "types.Message", "types.InlineMessage"],
        chat_id: Optional[Union[str, int]] = None,
        message_id: Optional[Union[str, int]] = None
    ):
        return await self._client.delete_message(
            chat_id=chat_id or self.chat_id,
            message_id=message_id or self.id or self.new_message.id or self.updated_message.id
        )
    
    def continue_propagation(self):
        raise rubxy.ContinuePropagation
    
    def stop_propagation(self):
        raise rubxy.StopPropagation