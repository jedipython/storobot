import asyncio
import hashlib

from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest, \
    GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, \
    ChannelParticipantsRecent
import time


api_id = 6601326
api_hash = '96a90b56538ab4321e01c5fa69499d89'
name = 'test'
client = TelegramClient('anon', api_id, api_hash)

# async def main():
#     async for dialog in client.iter_dialogs():
#         print(dialog.name, 'has ID', dialog.id)


letters = ['.','й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','ё','я','ч','с','м','и','т','ь','б','ю','1','2','3','4','5','6','7','8','9']
async def main():
    channel = await client.get_entity(1001146470778)  # id = 753519298
    agr = set()
    async for user in client.iter_participants(entity=channel, aggressive=True, limit=None):
        agr.add(user.id)
        print(user.status,user.first_name)
    start_time = time.time()
    for letter in letters:
        async for user in client.iter_participants(entity=channel, aggressive=True, limit=None, filter=ChannelParticipantsSearch(letter)):
            agr.add(user.id)
            print(user.status, user.first_name)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(agr))

with client:
    client.loop.run_until_complete(main())
#
#
# async def search_del_user():
#     channel = await client.get_entity('@buyanddelegate')  # id = 753519298
#     i = 0
#     async for user in client.iter_participants(entity=channel):
#                                                # filter=types.ChannelParticipantsBanned):
#         print(user.id)
#         i += 1
#         print(i)
# client.connect()
