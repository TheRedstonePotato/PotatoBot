# commands/amipotato.py

import discord
import asyncio

async def run(client, message, config, args):
	
	prefix = config[0]

	if len(message.content) == (len(prefix) + len('amipotato')):
		if str(message.author.id) == '163997823245746177':
			await client.send_message(message.channel, 'Yes, you are Potato.')
		else:
			await client.send_message(message.channel, 'No, you are not Potato.')
	else:
		await client.send_message(message.channel, 'This command does not take arguments.')