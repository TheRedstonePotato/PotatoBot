# commands/info.py

import asyncio
import discord

def getInfo(V): 
    return f"__**PotatoBot v{V}**__\n\nCreated by *Potato#2815*\nWritten in Python 3.6 using discord.py API\nInitally written using Notepad++, then Sublime Text 3"

async def run(cmd_properties):
    await cmd_properties["client"].send_message(cmd_properties["message"].channel, getInfo(cmd_properties["settings"]["version"]))
