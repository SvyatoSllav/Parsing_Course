import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, sync, connection
from pprint import pprint


load_dotenv()

TEST_API = str(os.environ.get('TEST_API'))
TEST_HASH = str(os.environ.get('TEST_HASH'))

client = TelegramClient('session_name2', TEST_API, TEST_HASH)
client.start()
participants = client.get_participants("https://t.me/Parsinger_Telethon_Test")

participants_data = []
for participant in participants:
    for profile_photo in client.iter_profile_photos(participant):
        client.download_media(profile_photo, file="Parsing_Course/img/")
