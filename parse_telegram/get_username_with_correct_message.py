import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, sync, connection
from pprint import pprint


load_dotenv()

TEST_API = str(os.environ.get('TEST_API'))
TEST_HASH = str(os.environ.get('TEST_HASH'))

with TelegramClient("session", TEST_API, TEST_HASH) as client:
    participants = set()
    for message in client.get_messages("https://t.me/Parsinger_Telethon_Test", limit=1000):
        if message.text and client.get_entity(message.from_id.user_id).username:
            participants.add(client.get_entity(message.from_id.user_id).username)

print(list(participants))
