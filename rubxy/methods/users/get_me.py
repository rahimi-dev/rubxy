import rubxy

from rubxy import types

class getMe:
    async def get_me(
        self: "rubxy.Client",
    ) -> "types.Bot":
        r = (await self.invoke("getMe")).get("bot")

        return types.Bot(
            bot_id=r.get("bot_id", ""),
            bot_title=r.get("bot_title", ""),
            description=r.get("description", ""),
            username=r.get("username", ""),
            start_message=r.get("start_message", ""),
            share_url=r.get("share_url", ""),
            client=self
        )