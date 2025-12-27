import rubxy

class getUpdates:
    async def get_updates(
        self: "rubxy.Client",
        limit: int = 100,
        offset_id: str = None
    ):
        return await self.invoke(
            method="getUpdates",
            offset_id=offset_id,
            limit=limit
        )