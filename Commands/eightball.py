# commands/eightball.py

import random
import asyncio
import discord

def getResponses(path):
    responses = []
    with open(path + "/Data/8ball.txt") as f:
        for line in f:
            responses.append(line)
    return responses


async def run(cmd_properties):
    client = cmd_properties["client"]
    message = cmd_properties["message"]
    prefix = cmd_properties["settings"]["prefix"]
    path = cmd_properties["settings"]["path"]
    if len(message.content) <= (len(prefix) + len("8ball")):
        await client.send_message(message.channel, "Invalid question.")
    else:
        responses = getResponses(path)
        response = responses[random.randint(0, len(responses)-1)]
        response = response.replace("%q", message.content[(len(prefix) + len("8ball") + 1):])
        response = response.replace("%n", str(message.author.display_name))
        response = response.replace("@everyone", "everyone")
        response = response.replace("@here", "here")
        await client.send_message(message.channel, response)
