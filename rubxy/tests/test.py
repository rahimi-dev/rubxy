from rubxy import Client, filters, enums, types, Plugins
from rubxy.types import Update, Keypad, Button, InlineMessage
import logging

logging.basicConfig(level=logging.INFO)

client = Client(bot_token="DBDHE0WYUPOBBNWEENWGZUHPEXXIPDFJIWNMQKNYUCVXHFVOIODELKQZFCHLOBTQ")
    
# @client.on_start()
# def s(client):
#     print('start handler')

# @client.on_stop()
# def t(client):
#     print('stop handler')

# @client.on_message(filters.commands("start") | filters.commands("stop"))
# async def m(_, update: Update):
#     m = await update.reply("Hello",
#                            inline_keypad=Keypad(
#                                [
#                                    [
#                                        Button(id="test", button_text="Test")
#                                    ]
#                                ]
#                            ))


# @client.on_inline_message(filters.regex("^s$") | filters.regex("^test$"))
# async def m2(_, update):
#     print(update)

client.run("https://cognitive-commonly-brings-manual.trycloudflare.com", update_endpoints=False)