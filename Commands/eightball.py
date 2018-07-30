# commands/eightball.py

import discord
import asyncio
import random

def getResponses(path):
	responses = []
	with open(path + '/Data/8ball.txt') as f:
		for line in f:
			responses.append(line)
	return responses


async def run(client, message, config, args):
	prefix = config[0]
	path = config[2]
	if len(message.content) == (len(prefix) + len('8ball')):
		await client.send_message(message.channel, 'Invalid question.')
	else:
		responses = getResponses(path)
		response = responses[random.randint(0, len(responses) - 1)]
		response = response.replace('%q', message.content[(len(prefix) + len('8ball') + 1):])
		name = str(message.author.display_name)
		response = response.replace('%n', name)
		response = response.replace('@everyone', 'everyone')
		response = response.replace('@here', 'here')
		await client.send_message(message.channel, response)
