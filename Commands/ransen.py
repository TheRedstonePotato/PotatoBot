# commands/ransen.py

import discord
import asyncio
import Commands.sentencegen

def isint(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

async def run(client, message, config, args):
	maxsentences = config[3]
	path = config[2]
	dictionaryPath = path + '/Data/Dictionary'
	if isint(args[0]):
		if int(args[0]) <= maxsentences and int(args[0]) >= 1:
			sentences = ''
			for i in range(int(args[0])):
				if i < int(args[0]):
					sentences = sentences + Commands.sentencegen.getSentence(dictionaryPath) + '\n\n'
				else:
					sentences = sentences + Commands.sentencegen.getSentence(dictionaryPath)
			await client.send_message(message.channel, sentences)
		else:
			sentence = Commands.sentencegen.getSentence(dictionaryPath)
			await client.send_message(message.channel, sentence)
	else:
		sentence = Commands.sentencegen.getSentence(dictionaryPath)
		await client.send_message(message.channel, sentence)
