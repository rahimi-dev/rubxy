import rubxy

from rubxy import enums, types

class UpdateEndpoints:
    async def update_endpoints(
        self: "rubxy.Client",
        url: str,
        type: "enums.UpdateEndpointType"
    ):
        return await self.invoke(
            "updateBotEndpoints",
            url=url,
            type=type
        )