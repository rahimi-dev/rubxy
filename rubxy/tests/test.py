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
    kos = await client.get_chat(update.chat_id)
    await update.reply(f"**Salam** [{kos.first_name}]({update.new_message.sender_id})")


client.run()