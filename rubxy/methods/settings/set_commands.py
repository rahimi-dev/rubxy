import rubxy

from rubxy import types
from typing import List, Union

class SetCommands:
    async def set_commands(
        self: "rubxy.Client",
        bot_commands: Union["types.BotCommand", List["types.BotCommand"]]
    ):
        if isinstance(bot_commands, types.BotCommand):
            bot_commands = [bot_commands]
        
        bot_commands = [
            commands._to_dict() for commands in bot_commands
        ]

        r = await self.invoke(
            "setCommands",
            bot_commands=bot_commands
        )

        print(r)