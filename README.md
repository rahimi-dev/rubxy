# rubxy

> **rubxy** is a Python library for interacting with the **Rubika** bot API.  
> It makes it easy to send and receive messages, handle events, and build bots quickly.

---

## Features

- Send and receive messages via Rubika API
- Easy-to-use event handlers
- Fully asynchronous & Support sync

---

## Installation

```bash
pip install rubxy
```

---

## Usage


### Messages Updates
```python
from rubxy import Client, filters
from rubxy.types import Update

client = Client(bot_token="BOT_TOKEN")

@client.on_message(filters.commands("start"))
async def start_handler(client: Client, update: Update):
    await update.reply("Hello from rubxy")

# Run in long-polling mode
client.run()

# Or run in webhook mode (recommended)

client.run(endpoint="https://example.com")
```

### Inline Updates

```python
from rubxy import Client, filters
from rubxy.types import InlineMessage

client = Client(bot_token="BOT_TOKEN")

@client.on_inline_message(filters.regex("^button-(\w+)"))
async def inline_message_handler(client: Client, i: InlineMessage):
    await i.answer(
        text="you clicked button-id: {}".format(
            i.matches[0].group(1)
        )
    )

# Run in long-polling mode
client.run()

# Or run in webhook mode (recommended)

client.run(endpoint="https://example.com")
```