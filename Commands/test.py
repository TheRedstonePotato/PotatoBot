# commands/test.py

import asyncio
import discord

async def run(cmd_properties):
    await cmd_properties["client"].send_message(cmd_properties["message"].channel, "Test successful.")