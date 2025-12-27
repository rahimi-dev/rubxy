import rubxy

from typing import Union

class GetFile:
    async def get_file(
        self: "rubxy.Client",
        file_id: Union[str, int]
    ):
        r = await self.invoke(
            "getFile",
            file_id=file_id
        )

        return r.get("download_url")