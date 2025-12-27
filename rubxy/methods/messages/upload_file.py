import rubxy
import aiohttp

from random import randint

class UploadFile:
    async def upload_file(
        self: "rubxy.Client",
        upload_url,
        file,
        file_name: str = None
    ):
        if file_name is None:
            file_name = "file-{}".format(randint(1, 999999))

        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
            filename=file_name,
            content_type="application/octet-stream"
        )

        async with self.http.post(upload_url, data=form) as response:
            response.raise_for_status()
            result = await response.json()
            
            return result["data"]["file_id"]