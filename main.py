import asyncio
from telethon import TelegramClient
from telethon import functions, types
from config import api_id, api_hash

channels = open('channels.txt','r', encoding="utf8").read().splitlines()

async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        for channel_name in channels:
            #normalize channel name
            channel_name=channel_name.replace("https://t.me/", "")
            result = await client(functions.contacts.SearchRequest(
                q=channel_name,
                limit=1
            ))
            
            #try ban channel if found
            if len(result.results) > 0:
                id = result.results[0].channel_id
                response = await client(functions.messages.ReportRequest(
                    peer='channel',
                    id=[id],
                    reason=types.InputReportReasonOther(),
                    message='Russian aggression'
                ))
                if response:
                    print("{} was banned".format(channel_name))
                else:
                    print("{} was NOT banned".format(channel_name))  
            else:
                print("{} was NOT found".format(channel_name))                
asyncio.run(main())