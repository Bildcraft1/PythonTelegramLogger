from telethon import TelegramClient, events
import os
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Telegram Logger'))

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
client = TelegramClient("session_lock", api_id, api_hash)
chat_id = int(input("Enter ChatID: "))
log_id = int(os.environ["log_id"])


@client.on(events.NewMessage(chats=chat_id))
async def logger(event):
    sender = await event.get_sender()
    if event.message.text and not event.message.media:
        print("{}: {}".format(sender.first_name, event.message.text))
        client.parse_mode = 'html'
        await client.send_message(log_id, "<b>{}</b>: {}".format(sender.first_name, event.message.text))
    else:
        print("{}: *sent a media*".format(sender.first_name))
        client.parse_mode = 'html'
        await client.send_message(log_id, "<b>{}</b>: *sent a media*".format(sender.first_name))


client.start()
print("Connected")
client.run_until_disconnected()
