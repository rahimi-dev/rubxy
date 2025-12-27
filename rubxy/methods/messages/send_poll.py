import rubxy

from rubxy import types
from typing import List

class SendPoll:
    async def send_poll(
        self: "rubxy.Client",
        chat_id: str,
        question: str,
        options: List[str]
    ) -> "types.Message":
        r = await self.invoke(
            "sendPoll",
            chat_id=chat_id,
            question=question,
            options=options
        )

        return types.Message(
            chat_id=chat_id,
            id=r.get("message_id"),
            client=self
        )