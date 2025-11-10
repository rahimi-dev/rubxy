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

@client.on_message()
async def m(_, update: Update):
    print(update.new_message.metadata.meta_data_parts)


client.run()