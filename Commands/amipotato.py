# commands/amipotato.py

import asyncio
import discord

async def run(cmd_properties):
    client = cmd_properties["client"]
    message = cmd_properties["message"]
    if len(message.content) == (len(cmd_properties["settings"]["prefix"]+"amipotato")):
        if str(message.author.id) == "163997823245746177":
            await client.send_message(message.channel, "Yes, you are Potato.")
        else:
            await client.send_message(message.channel, "No, you are not Potato.")
    else:
        await client.send_message(message.channel, "This command does not take arguments.")