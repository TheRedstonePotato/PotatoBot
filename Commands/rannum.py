# commands/rannum.py

import random
import asyncio
import discord

def validint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
        
def getSyntax(p):
    return f"`{p}rannum <number>` for a random number between 0 and the given number, or\n`{p}rannum <number> <number>` for a random number between the two given numbers.\nNumbers must be integers."

async def run(cmd_properties):
    client = cmd_properties["client"]
    message = cmd_properties["message"]
    args = cmd_properties["args"]
    prefix = cmd_properties["settings"]["prefix"]
    if len(message.content) == (len(prefix) + len("rannum")):
        await client.send_message(message.channel, "Invalid syntax.\n" + getSyntax(prefix))
    elif len(args) == 1:
        if validint(args[0]):
            if int(args[0]) > 0:
                await client.send_message(message.channel, str(random.randint(0, int(args[0]))))
            else:
                await client.send_message(message.channel, str(random.randint(int(args[0]), 0)))
        else:
            await client.send_message(message.channel, "Invalid integer.")
    elif len(args) == 2:
        if validint(args[0]) and validint(args[1]):
            if int(args[0]) > int(args[1]):
                await client.send_message(message.channel, str(random.randint(int(args[1]), int(args[0]))))
            else:
                await client.send_message(message.channel, str(random.randint(int(args[0]), int(args[1]))))
        else:
            await client.send_message(message.channel, "Invalid integer.")
    else:
        await client.send_message(message.channel, "Invalid syntax.\n" + getSyntax(prefix))
