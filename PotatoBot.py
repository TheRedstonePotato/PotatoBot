# PotatoBot.py

print('Initialising...')

import discord
import asyncio
import os
import sys
import time
import random
import CommandHandler

print('Finished importing.')

client = discord.Client()
path = os.path.dirname(os.path.abspath(__file__))
serverFile = path + '/Data/servers.txt'
reactionWordsFile = path + '/Data/reactionWords.txt'
reactionChanceFile = path + '/Data/reactionChance.txt'
Echars = '🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿🥔'
alphabet = 'abcdefghijklmnopqrstuvwxyzP'

def parse(file):
	with open(file, 'r') as f:
		newlist = []
		for line in f:
			values = line.split(' ')
			vlist = []
			for value in values:
				vlist.append(value.replace('\n', ''))
			newlist.append(vlist)
		return newlist

def unparse(file,  parsed):
	with open(file, 'w') as f:
		for line in parsed:
			text = ''
			for value in line:
				text = text + value + ' '
			text = text[:len(text)-1] + '\n'
			f.write(text)		

def addline(file, text):
	with open(file, 'a') as f:
		text = text + '\n'
		f.write(text)

def getEmoji(char):
	i = alphabet.index(char)
	return str(Echars[i])

async def react(message):
	with open(reactionChanceFile, 'r') as f:
		possibilities = int(f.read())
	x = random.randint(0, possibilities)
	if x == 0:
		await client.add_reaction(message, '🥔')
	elif x <= 1:
		words = []
		with open(reactionWordsFile, 'r') as f:
			for w in f:
				words.append(w.replace('\n', ''))
		word = words[random.randint(0, len(words)-1)]
		for c in word:
			await client.add_reaction(message, getEmoji(c))

@client.event
async def on_ready():
	text = 'Successfully connected.\nLogged in as: ' + client.user.name + ' (' + client.user.id + ')\nRunning in directory: ' + path + '\nPOTATO BOT 7.0\n==================================================================='
	print(text)

@client.event
async def on_message(message):

	msg = str(message.content)
	sender = str(message.author)
	sid = message.server.id
	cid = message.channel.id
	sname = str(message.server.name)
	cname = str(message.channel.name)
	
	msgtime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

	logText = '[' + msgtime + '] ' + sname + ', ' + cname + ' (' + str(sid) + ', ' + str(cid) + '), ' + sender + ': ' + msg
	print(logText)

	prefix = '!'
	maxpotatoes = 50
	maxsentences = 10
	reactChance = 20
	inList = False
	serverList = parse(serverFile)

	for server in serverList:
		if str(sid) == server[0]:
			inList = True
			prefix = server[1]
			maxpotatoes = int(server[2])
			maxsentences = int(server[3])
			reactChance = int(server[4])

	if inList == False:
		text = str(sid) + ' ' + prefix + ' ' + str(maxpotatoes) + ' ' + str(maxsentences) + ' ' +s str(reactChance)
		addline(serverFile, text) 
		
	config = [prefix, maxpotatoes, path, maxsentences]

	if msg.startswith(prefix):
		await CommandHandler.run(client, message, config)
	else:
		await react(message)

print('Connecting...')
try:
	token = sys.argv[1]
	client.run(token)
except:
	print('Please execute the file from a command line with a valid token as an argument.')