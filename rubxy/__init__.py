import asyncio

from typing import Optional, List

class Plugins:
    def __init__(
        self,
        root: str,
        include: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None
    ):
        self.root = root
        self.include = [include] if isinstance(include, str) else include
        self.exclude = [exclude] if isinstance(exclude, str) else exclude

class StopPropagation(StopAsyncIteration):
    pass

class ContinuePropagation(StopAsyncIteration):
    pass

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


from .client import Client
from . import sync