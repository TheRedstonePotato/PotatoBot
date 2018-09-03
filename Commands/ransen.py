# commands/ransen.py

import asyncio
import discord
import Commands.sentencegen

def validint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

async def run(cmd_properties):
    arg = cmd_properties["args"][0]
    client = cmd_properties["client"]
    message = cmd_properties["message"]
    max_sentences = cmd_properties["settings"]["max_sentences"]
    dict_path = cmd_properties["settings"]["path"] + "/Data/Dictionary"
    if validint(arg):
        if int(arg) <= max_sentences and int(arg) >= 1:
            sentences = ''
            for i in range(int(arg)):
                if i < int(arg):
                    sentences = sentences + Commands.sentencegen.getSentence(dict_path) + "\n\n"
                else:
                    sentences = sentences + Commands.sentencegen.getSentence(dict_path)
            await client.send_message(message.channel, sentences)
        else:
            sentence = Commands.sentencegen.getSentence(dict_path)
            await client.send_message(message.channel, sentence)
    else:
        sentence = Commands.sentencegen.getSentence(dict_path)
        await client.send_message(message.channel, sentence)
