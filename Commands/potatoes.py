# commands/potatoes.py

import asyncio
import discord

def validint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

async def run(cmd_properties):
    client = cmd_properties["client"]
    message = cmd_properties["message"]
    args = cmd_properties["args"]
    prefix = cmd_properties["settings"]["prefix"]
    max_potatoes = cmd_properties["settings"]["max_potatoes"]

    if len(message.content) == (len(prefix) + len("potatoes")):
        await client.send_message(message.channel, "Invalid syntax.\n`" + prefix + "potatoes <amount>`")
    elif len(args) != 1:
        await client.send_message(message.channel, "Invalid syntax.\n`" + prefix + "potatoes <amount>`")
    else:
        if validint(args[0]) == False:
            await client.send_message(message.channel, "Invalid integer.")
        else:
            potatoes = int(args[0])
            if potatoes >= 1 and potatoes <= max_potatoes:
                potatoes_string = ""
                for potato in range(0, potatoes):
                    potatoes_string = potatoes_string + ":potato: "
                await client.send_message(message.channel, potatoes_string)
            elif potatoes > 9000:
                await client.send_message(message.channel, "That's too many potatoes to post. You wanna know why it's too many? Because IT'S OVER 9000! Bet you didn't see that reference coming, did you?")
            else:
                await client.send_message(message.channel, "Invalid integer; must be between 1 and " + str(max_potatoes) + ".")