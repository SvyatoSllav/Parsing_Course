import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, sync, connection
from telethon.types import InputMessagesFilterPinned
from pprint import pprint


load_dotenv()

TEST_API = str(os.environ.get('TEST_API'))
TEST_HASH = str(os.environ.get('TEST_HASH'))

with TelegramClient("session", TEST_API, TEST_HASH) as client:
    all_messages = client.get_messages("https://t.me/Parsinger_Telethon_Test", limit=1000, filter=InputMessagesFilterPinned)
    for message in all_messages:
        print(message.from_id.user_id)
