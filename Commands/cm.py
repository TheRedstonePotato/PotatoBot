# commands/cm.py

import discord
import asyncio
import json
import requests
import decimal

key = 'ce3d20709b5a1c25677aa932b976348f'
base = 'http://data.fixer.io/api/latest?access_key=' + key

async def run(client, message, config, args):
	if len(args) != 3:
		await client.send_message(message.channel, 'Args: `amount`, `from`, `to` ')
	else:
		try:
			amt = float(args[0])
		except:
			await client.send_message(message.channel, 'Invalid amount.')
			return
		frm = args[1].upper()
		to = args[2].upper()
		url = base + '&from=' + frm + '&to=' + to + '&amount=' + str(amt)
		try:
			response = requests.get(url)
		except:
			await client.send_message(message.channel, 'An error occurred.')
			return
		data = response.json()
		rates = data['rates']
		try:
			inEuro = amt / rates[frm]
			converted = inEuro * rates[to]
		except:
			await client.send_message(message.channel, 'Invalid currency code.')
			return
		convDec = decimal.Decimal(converted)
		convRou = round(convDec, 2)
		await client.send_message(message.channel, str(amt) + ' ' + frm + ' = ' + str(convRou) + ' ' + to)