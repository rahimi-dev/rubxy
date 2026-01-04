import re
import inspect
import asyncio
import rubxy

from rubxy import enums
from rubxy.types import Update, InlineMessage

from typing import Callable, Any, Union, Optional, Pattern, List

class Filter:
    def __call__(self, client, update):
        return NotImplementedError
    
    def __and__(self, other):
        return And(self, other)
    
    def __or__(self, other):
        return Or(self, other)

    def __invert__(self, other):
        return Not(other) 

class And(Filter):
    def __init__(self, base, other):
        self.base = base
        self.other = other
    
    async def __call__(self, client, update):
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(client, update)
        else:
            client.loop.run_in_executor(
                client.executor,
                self.base,
                client, update
            )
        
        if not x:
            return False
        
        if inspect.iscoroutinefunction(self.other.__call__):
            y = await self.other(client, update)
        else:
            y = client.loop.run_in_executor(
                client.executor,
                self.other,
                client, update
            )
        
        return x and y

class Or(Filter):
    def __init__(self, base, other):
        self.base = base
        self.other = other
    
    async def __call__(self, client, update):
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(client, update)
        else:
            x = client.loop.run_in_executor(
                client.executor,
                self.base,
                client, update
            )
        
        if x:
            return True
        
        if inspect.iscoroutinefunction(self.other.__call__):
            y = await self.other(client, update)
        else:
            y = client.loop.run_in_executor(
                client.executor,
                self.other,
                client, update
            )
        
        return x or y

class Not(Filter):
    def __init__(self, base):
        self.base = base
    
    async def __call__(self, client, update):
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(client, update)
        else:
            x = client.loop.run_in_executor(
                client.executor,
                self.base,
                client, update
            )
        
        return not x
    
def create(
    func: Callable,
    name: Optional[str] = None,
    **kwargs
) -> "Filter":
    return type(
        name or func.__name__,
        (Filter,),
        {"__call__": func, **kwargs}
    )()

def commands(commands: Union[str, List[str]], prefixes: Optional[List[str]] = ['/'], ignore_case: bool = False)-> bool:
    async def func(flt, __, update: Union[Update, InlineMessage]):
        string = (
            getattr(update.new_message, "text", None) or
            getattr(update.updated_message, "text", None)
        )
        
        if not string:
            return False
        
        p = re.compile(flt.pattern, re.IGNORECASE if flt.ignore_case else 0)

        update.matches = list(p.finditer(string))
            
        return bool(update.matches)
    
    cmds = commands if isinstance(commands, list) else [commands]
    escaped_prefixes = [re.escape(p) for p in prefixes]

    pattern = r"^(?:{})(?:{})".format(
        "|".join(escaped_prefixes),
        "|".join(cmds)
    ) + r"(?:\s|$)"

    return create(
        func,
        cmds=cmds,
        escaped_prefixes=escaped_prefixes,
        pattern=pattern,
        ignore_case=ignore_case
    )
        
def regex(pattern: Union[Pattern, str], flags: int = 0)-> bool:
    async def func(flt, _, update: Union[Update, InlineMessage]):
        string = (
            getattr(update.new_message, "text", None) or getattr(update.updated_message, "text", None)
        ) or (
            getattr(update.aux_data, "button_id", None) or update.text
        )
        
        if not string:
            return False
        
        update.matches = list(flt.p.finditer(string)) or None

        return bool(update.matches)
    
    return create(
        func,
        p=pattern if isinstance(pattern, Pattern) else re.compile(pattern=pattern, flags=flags)
    )
    
async def private_filter(_, __, update: Union[Update, InlineMessage])-> bool:
    return update.chat_id.startswith(("u", "b"))

private = create(private_filter)

async def group_filter(_, __, update: Union[Update, InlineMessage]) -> bool:
    return update.chat_id.startswith("g0")

group = create(group_filter)


async def channel_filter(_, __, update: Union[Update, InlineMessage]) -> bool:
    return update.chat_id.startswith("c0")

channel = create(channel_filter)

async def text_filter(self, _, update: Union[Update, InlineMessage]) -> bool:
    return any(
        (
            update.new_message.text,
            update.updated_message.text
        )
    )

text = create(text_filter)

async def file_filter(_, __, update: Union[Update, InlineMessage]) -> bool:
    return any(
        (
            update.new_message.file,
            update.updated_message.file
        )
    )

file = create(file_filter)

async def forwarded_filter(_, __, update: Union[Update, InlineMessage])-> bool:
    return any(
        (
            update.new_message.forwarded_from,
            update.updated_message.forwarded_from
        )
    )
    
forwarded = create(forwarded_filter)

class chat(Filter):
    def __init__(self, chat_id: Union[str, List[str]])-> bool:
        if not isinstance(chat_id, (list, str)):
            raise TypeError("`chat_id` must be type of list or str")
        
        self.chat_id = [chat_id] if isinstance(chat_id, str) else chat_id
    
    async def __call__(self, _, update: Union[Update, InlineMessage]):
        return update.chat_id in self.chat_id

async def edited_filter(_, __, update: Union[Update, InlineMessage])-> bool:
    return getattr(update.new_message, "is_edited", None) or getattr(update.new_message, "is_edited", None)
    
edited = create(edited_filter)