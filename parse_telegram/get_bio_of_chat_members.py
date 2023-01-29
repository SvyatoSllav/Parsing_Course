import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest


load_dotenv()

TEST_API = str(os.environ.get('TEST_API'))
TEST_HASH = str(os.environ.get('TEST_HASH'))

lst = ['Anthony_Hills', 'Craig_Moody', 'Kathleen_Browns', 'Vicki_Baileys', 'Jorge_Garrett', 'Larry_Summers', 'Tommy_Sullivan', 'Edward_Murrray', 'Nicholas_Gonzales', 'Virgina_Garcia', 'Denise_Barker', 'Jessie_Wright', 'Mary_Baileyn', 'Claytons_Riley', 'Joshuan_Chandler', 'Jameson_Powell', 'Harry_Valdes', 'Chriss_Yong', 'Sarah_Wilis', 'Frances_Ross', 'Joseph_Anderson']

client = TelegramClient('session_name2', TEST_API, TEST_HASH)
client.start()
participants = client.iter_participants("https://t.me/Parsinger_Telethon_Test")

result = 0
for participant in participants:
    user_full_info = client(GetFullUserRequest(participant))
    if participant.username in lst:
        result += int(user_full_info.full_user.about)

print(result)
