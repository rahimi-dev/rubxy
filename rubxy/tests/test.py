from rubxy import Client, filters, enums, types, Plugins
from rubxy.types import Update, Keypad, Button, InlineMessage
import logging

logging.basicConfig(level=logging.INFO)

client = Client(bot_token="DBDHE0WYUPOBBNWEENWGZUHPEXXIPDFJIWNMQKNYUCVXHFVOIODELKQZFCHLOBTQ")
    
@client.on_start()
async def s(_):
    print(await client.get_me())

@client.on_stop()
def t(client):
    print('stop handler')

@client.on_message(filters.commands("start") | filters.commands("stop"))
async def m(_, update: Update):
    r = await client.send_file(update.chat_id, file="rubxy/tests/download.jpg")

@client.on_inline_message(filters.regex("^s$") | filters.regex("^test$"))
async def m2(_, update):
    print(update)

client.run()