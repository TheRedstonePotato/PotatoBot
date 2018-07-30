# CommandHandler.py

import discord
import asyncio
import Commands.calc
import Commands.rannum
import Commands.potatoes
import Commands.amipotato
import Commands.info
import Commands.help
import Commands.eightball
import Commands.ransen
import Commands.test
import Commands.cm

personal = False
try:
	import Personal.CommandHandler
	personal = True
	print('Personal module is enabled.')
except ImportError:
	pass

async def invalid(client, message, config):
	prefix = config[0]
	await client.send_message(message.channel, 'That is not a valid command. For a list of commands, use `' + prefix + 'help`.')

async def run(client, message, config):
	
	prefix = config[0]
	msg = message.content[len(prefix):]
	command = msg.split(' ')[0] 
	args = msg[len(command)+1:].split(' ')

	if command == 'calc' or command == 'calculate':
		await Commands.calc.run(client, message, config, args)
	elif command == 'rannum' or command == 'randomnumber':
		await Commands.rannum.run(client, message, config, args)
	elif command == 'ransen' or command == 'randomsentence':
		await Commands.ransen.run(client, message, config, args)
	elif command == 'potatoes':
		await Commands.potatoes.run(client, message, config, args)
	elif command == 'amipotato':
		await Commands.amipotato.run(client, message, config, args)
	elif command == '8ball':
		await Commands.eightball.run(client, message, config, args)
	elif command == 'info':
		await Commands.info.run(client, message, config, args)
	elif command == 'help':
		await Commands.help.run(client, message, config, args)
	elif command == 'test':
		await Commands.test.run(client, message, config, args)
	elif command == 'cm' or command == 'convertmoney':
		await Commands.cm.run(client, message, config, args)
	elif personal and str(message.author.id) == '163997823245746177':
		await Personal.CommandHandler.run(client, message, config)
	else:
		await invalid(client, message, config)