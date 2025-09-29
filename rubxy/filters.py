import re
import inspect
import asyncio
import rubxy

from rubxy import enums
from rubxy.types import Update, InlineMessage
from rubxy.utils import anies
from typing import Callable, Any, Union, Optional

class Filter:
    async def __call__(self, client, update) -> bool:
        raise NotImplementedError

    def __and__(self, other: "Filter") -> "Filter":
        return AndFilter(self, other)

    def __or__(self, other: "Filter") -> "Filter":
        return OrFilter(self, other)

    def __invert__(self) -> "Filter":
        return InvertFilter(self)


class InvertFilter(Filter):
    def __init__(self, base: Filter):
        self.base = base

    async def __call__(self, client: "rubxy.Client", update) -> bool:
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(client, update)
        else:
            x = await client.loop.run_in_executor(client.executor, self.base, client, update)
        return not x


class AndFilter(Filter):
    def __init__(self, base: Filter, other: Filter):
        self.base = base
        self.other = other

    async def __call__(self, client: "rubxy.Client", update) -> bool:
        # base
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(client, update)
        else:
            x = await client.loop.run_in_executor(client.executor, self.base, client, update)

        if not x:  # short-circuit
            return False

        # other
        if inspect.iscoroutinefunction(self.other.__call__):
            y = await self.other(client, update)
        else:
            y = await client.loop.run_in_executor(client.executor, self.other, client, update)

        return x and y


class OrFilter(Filter):
    def __init__(self, base: Filter, other: Filter):
        self.base = base
        self.other = other

    async def __call__(self, client: "rubxy.Client", update: Update) -> bool:
        # base
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(client, update)
        else:
            x = await client.loop.run_in_executor(client.executor, self.base, client, update)

        if x:  # short-circuit
            return True

        # other
        if inspect.iscoroutinefunction(self.other.__call__):
            y = await self.other(client, update)
        else:
            y = await client.loop.run_in_executor(client.executor, self.other, client, update)

        return x or y

class commands(Filter):
    def __init__(self, commands: Union[list, str], prefixes: Optional[list] = ['/'], ignore_case: bool = False):
        self.ignore_case = ignore_case
        cmds = commands if isinstance(commands, list) else [commands]
        escaped_prefixes = [re.escape(p) for p in prefixes]

        self.pattern = r"^(?:{})(?:{})".format(
            "|".join(escaped_prefixes),
            "|".join(cmds)
        ) + r"(?:\s|$)"
    
    def __call__(self, _, update: Update):
        _text = update.new_message.text or update.updated_message.text
        
        if not _text:
            return False
        
        p = re.compile(self.pattern, re.IGNORECASE if self.ignore_case else 0)
        update.matches = list(p.finditer(_text))
            
        return bool(update.matches)


class regex(Filter):
    def __init__(self, pattern: str, flags: int = 0):
        self.p = re.compile(pattern, flags)

    def __call__(self, _, update: Union[Update, InlineMessage]):
        string: str = None

        if isinstance(update, Update):
            string = update.new_message.text or update.updated_message.text
        
        elif isinstance(update, InlineMessage):
            string = update.aux_data.button_id or update.text
        
        if not string:
            return False
        
        update.matches = list(self.p.finditer(string))

        return bool(update.matches)
    
class private_filter(Filter):
    def __call__(self, _, update: Update):
        return update.chat_id.startswith(("u", "b"))
    
private = private_filter()

class group_filter(Filter):
    def __call__(self, _, update: Update):
        return update.chat_id.startswith("g0")

group = group_filter()

class channel_filter(Filter):
    def __call__(self, _, update: Update) -> bool:
        return update.chat_id.startswith("c0")

channel = channel_filter()

class text_filter(Filter):
    def __call__(self, _, update: Update) -> bool:
        return anies(
            update.new_message.text,
            update.updated_message.text
        )

text = text_filter()

class file_filter(Filter):
    def __call__(self, _, update: Update) -> bool:
        return anies(
            update.new_message.file,
            update.updated_message.file
        )

file = file_filter()

class forwarded_filter(Filter):
    def __call__(self, _, update: Update):
        return anies(
            update.new_message.forwarded_from,
            update.updated_message.forwarded_from
        )
    
forwarded = forwarded_filter()