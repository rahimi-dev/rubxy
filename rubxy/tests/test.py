from rubxy import Client, filters, enums, types, Plugins
from rubxy.types import Update, Keypad, Button, InlineMessage
import logging

logging.basicConfig(level=logging.INFO)

client = Client(bot_token="")

@client.on_start()
def s(client):
    print('start handler')

@client.on_stop()
def t(client):
    print('stop handler')

@client.on_message(filters.commands("start"))
async def m(_, update: Update):
    await update.delete()
    m = await update.reply("Hello", inline_keypad=Keypad(
        [
            [
                Button("salam", button_text="Hi", button_calendar="rr")
            ]
        ]
    ))


@client.on_inline_message(filters.regex("^salam$"))
async def m2(_, update):
    print(update)

client.run()