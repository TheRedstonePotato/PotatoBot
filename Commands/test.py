# commands/test.py

import discord
import asyncio

async def run(client, message, config, args):
	await client.send_message(message.channel, 'Test successful.')
