import rubxy

from rubxy import enums

class RequestSendFile:
    async def request_send_file(
        self: "rubxy.Client",
        type: enums.FileType
    ):
        if not isinstance(type, enums.FileType) and type not in list(enums.FileType):
            raise TypeError("`type` must be of type enums.FileType or in %s"%list(enums.FileType))
        
        r = await self.invoke(
            "requestSendFile",
            type=type
        )

        return r.get("upload_url")