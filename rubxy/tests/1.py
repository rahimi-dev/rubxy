# {'meta_data_parts': [{'type': 'Link', 'from_index': 11, 'length': 4, 'link': {'type': 'hyperlink', 'hyperlink_data': {'url': 'https://rubika.ir'}}}]}

# {'text': 'Hello from Amir', 'metadata': {'meta_data_parts': [{'type': 'Link', 'from_index': 11, 'length': 4, 'link': {'type': 'hyperlink', 'hyperlink_data': {'url': 'https://rubika.ir'}}}]}}
import rubpy

c = rubpy.BotClient("DBDHE0WYUPOBBNWEENWGZUHPEXXIPDFJIWNMQKNYUCVXHFVOIODELKQZFCHLOBTQ", persist_offset=True)

@c.on_update()
async def updas(c: rubpy.BotClient, update):
    kos = await c.get_chat(update.chat_id)
    await update.reply(f"**Salam** [{kos.first_name}]({update.new_message.sender_id})")


c.run()