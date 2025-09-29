import rubxy

from rubxy.types import Message
from rubxy.errors import raise_exception
from typing import Optional

HEADERS = {'Content-Type': 'application/json'}

class Invoke:
    async def invoke(
        self: "rubxy.Client",
        method: str,
        **parameters
    ) -> dict:
        if not self.is_started:
            raise ConnectionError("Client has not been started yet")
        
        await self._rate_limit()
        
        async with self.http.post(method, json=parameters, headers=HEADERS) as response:
            if not response.ok:
                raise

            result = await response.json()

            if result.get("status") != "OK":
                raise_exception(
                    result.get("status"),
                    result.get("dev_message")
                )
            
            return result.get("data")