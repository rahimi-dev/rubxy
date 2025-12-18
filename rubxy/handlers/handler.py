import rubxy
import inspect
import traceback

from rubxy.types import Update
from rubxy.filters import Filter
from typing import Callable

class Handler:
    def __init__(
        self,
        callback: Callable,
        filters: Filter = None,
        event_type: str = None
    ):
        self.callback = callback
        self.filters = filters
        self.event_type = event_type
    
    async def check(
        self,
        client: "rubxy.Client",
        update: Update
    ):
        if not self.filters:
            await self._call_callback(client, update)           
            return True

        # All filters must be true
        f = self.filters
        
        try:
            if inspect.iscoroutinefunction(f.__call__):
                ok = await f(client, update)
            else:
                ok = f(client, update)
        except Exception:
            ok = False

        if not ok:
            return
        
        await self._call_callback(client, update)
        return True

    async def _call_callback(
        self,
        client: "rubxy.Client",
        update: Update
    ):
        if inspect.iscoroutinefunction(self.callback):
            await self.callback(client, update)
        else:
            client.loop.run_in_executor(
                client.executor,
                self.callback,
                client, update
            )