# commands/potatoes.py

import discord
import asyncio

def isint(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

async def run(client, message, config, args):
	prefix = config[0]
	maxpotatoes = config[1]

	if len(message.content) == (len(prefix) + len('potatoes')):
		await client.send_message(message.channel, 'Invalid syntax.\n`' + prefix + 'potatoes <amount>`')
	elif len(args) != 1:
		await client.send_message(message.channel, 'Invalid syntax.\n`' + prefix + 'potatoes <amount>`')
	else:
		if isint(args[0]) == False:
			await client.send_message(message.channel, 'Invalid integer.')
		else:
			potatoes = int(args[0])
			if potatoes >= 1 and potatoes <= maxpotatoes:
				potatoes_string = ''
				for potato in range(0, potatoes):
					potatoes_string = potatoes_string + ':potato: '
				await client.send_message(message.channel, potatoes_string)
			elif potatoes > 9000:
				await client.send_message(message.channel, 'That\'s too many potatoes to post. You wanna know why it\'s too many? Because IT\'S OVER 9000! Bet you didn\'t see that reference coming, did you?')
			else:
				await client.send_message(message.channel, 'Invalid integer; must be between 1 and ' + str(maxpotatoes) + '.')