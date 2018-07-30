# commands/rannum.py

import discord
import asyncio
import random

def isint(value):
	try:
		int(value)
		return True
	except ValueError:
		return False
		
def getSyntax(prefix):
	syntax = '`' + prefix + 'rannum <number>` for a random number between 0 and the given number, or\n`' + prefix + 'rannum <number> <number>` for a random number between the two given numbers.\nNumbers must be integers.'
	return syntax

async def run(client, message, config, args):
	prefix = config[0]
	syntax = getSyntax(prefix)
	if len(message.content) == (len(prefix) + len('rannum')):
		await client.send_message(message.channel, 'Invalid syntax.\n' + syntax)
	elif len(args) == 1:
		if isint(args[0]):
			if int(args[0]) > 0:
				await client.send_message(message.channel, str(random.randint(0, int(args[0]))))
			else:
				await client.send_message(message.channel, str(random.randint(int(args[0]), 0)))
		else:
			await client.send_message(message.channel, 'Invalid integer.')
	elif len(args) == 2:
		if isint(args[0]) and isint(args[1]):
			if int(args[0]) > int(args[1]):
				await client.send_message(message.channel, str(random.randint(int(args[1]), int(args[0]))))
			else:
				await client.send_message(message.channel, str(random.randint(int(args[0]), int(args[1]))))
		else:
			await client.send_message(message.channel, 'Invalid integer.')
	else:
		await client.send_message(message.channel, 'Invalid syntax.\n' + syntax)
