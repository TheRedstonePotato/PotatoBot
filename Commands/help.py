# commands/help.py

import discord
import asyncio

def getHelp(p): 
	h = f'Commands:\n`{p}8ball` - Ask a yes/no question and get a yes/no/other answer.\n`{p}amipotato` - Tells you whether you are Potato.\n`{p}calc` - Calculates based on given numbers and operators.\n`{p}cm` - Convert an amount of money between two currencies.\n`{p}info` - Get info about the bot.\n`{p}potatoes` - Produces a given amount of potatoes.\n`{p}rannum` - Produces a random number from a given range.\n`{p}ransen` - Produces a random sentence.'
	return h

async def run(client, message, config, args):
	await client.send_message(message.channel, getHelp(config[0]))

