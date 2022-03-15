import asyncio
import re
from telethon import TelegramClient
from telethon import functions, types
from config import api_id, api_hash

channels = open('channels.txt','r', encoding="utf8").read().splitlines()

def check_channel_name(strg, search=re.compile(r'[^_A-Za-z0-9.]').search):
    return not bool(search(strg))

async def search_channel(client, name):
    result = await client(functions.contacts.SearchRequest(
             q=name,
             limit=1
            ))
    return result.results

async def ban_channel(client, id):
    response = await client(functions.messages.ReportRequest(
                   peer='channel',
                   id=[id],
                   reason=types.InputReportReasonOther(),
                   message='Russian aggression'
                ))
    return response

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        for channel_name in channels:
            channel_name=channel_name.replace(" ", "")
            if len(channel_name) == 0:
                continue
            #normalize channel name
            channel_name=channel_name.replace("https://t.me/", "")
            if not check_channel_name(channel_name):
                print("{} has incorrect symbols in name".format(channel_name))
                continue

            found_channels = await search_channel(client, channel_name)

            #try ban channel if found
            if len(found_channels) > 0:
                id = found_channels[0].channel_id
                response = await ban_channel(client, id)
                if response:
                    print("{} was banned".format(channel_name))
                else:
                    print("{} was NOT banned".format(channel_name))  
            else:
                print("{} was NOT found".format(channel_name))                
asyncio.run(main())

