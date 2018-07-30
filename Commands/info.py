# commands/info.py

import discord
import asyncio

def getInfo(): 
	info = '-- **PotatoBot v7.0** --\nCreated by Potato#2815\nWritten in Python 3.6 using discord.py API\nInitally written using Notepad++, then Sublime Text 3\nI don\'t have much other information to give here.'
	return info

async def run(client, message, config, args):
	await client.send_message(message.channel, getInfo())
