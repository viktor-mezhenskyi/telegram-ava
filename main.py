import asyncio
from telethon import TelegramClient
from telethon import functions, types
from config import api_id, api_hash

channels = open('channels.txt','r', encoding="utf8").read().splitlines()
async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        for channel_name in channels:
            result = await client(functions.contacts.SearchRequest(
                q=channel_name,
                limit=1
            ))
            id = result.results[0].channel_id
            result = await client(functions.messages.ReportRequest(
                peer='channel',
                id=[id],
                reason=types.InputReportReasonOther(),
                message='Russian aggression'
            ))
            print(result)      
asyncio.run(main())