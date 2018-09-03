# PotatoBot.py


if __name__ == '__main__':
    
    print("Initialising...")

import multiprocessing
import os
import sys
import time
import json
import random
import asyncio
import discord
import CommandHandler


def client_thread(pipe, queue):

    PATH = os.path.dirname(os.path.abspath(__file__))
    VERSION = "8.0"
    server_path = PATH + "/Data/servers.txt"
    reaction_words_path = PATH + "/Data/reactionWords.txt"
    emoji_chars = "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿🥔"
    alphabet = "abcdefghijklmnopqrstuvwxyzP"

    default_settings = {
    	"version": VERSION,
        "path": PATH,
        "prefix": "!",
        "max_potatoes": 50,
        "max_sentences": 10,
        "react_probability": 20,
        "personal": CommandHandler.PERSONAL_ENABLED,
    }


    def parse(file):
        with open(file, "r") as f:
            newlist = []
            for line in f:
                values = line.split(" ")
                vlist = [] 
                for value in values:
                    vlist.append(value.replace("\n", ""))
                newlist.append(vlist)
            return newlist

    def unparse(file,  parsed):
        with open(file, "w") as f:
            for line in parsed:
                text = ""
                for value in line:
                    text = text + value + " "
                text = text[:len(text)-1] + "\n"
                f.write(text)

    def addline(file, text):
        with open(file, "a") as f:
            text = text + "\n"
            f.write(text)
    
    def getEmoji(char):
        i = alphabet.index(char)
        return str(emoji_chars[i])
    
    async def react(message, reaction_probability):
        x = random.randint(0, reaction_probability)
        if x == 0:
            await client.add_reaction(message, "🥔")
        elif x == 1:
            words = []
            with open(reaction_words_path, "r") as f:
                for w in f:
                    words.append(w.replace("\n", ""))
            word = words[random.randint(0, len(words)-1)]
            for c in word:
                await client.add_reaction(message, getEmoji(c))


    client = discord.Client()
    
    @client.event
    async def on_ready():
        text = "Successfully connected.\nLogged in as: " + client.user.name + " (" + client.user.id + ")\nRunning in directory: " + PATH + "\nPOTATO BOT " + VERSION + "\n==================================================================="
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
    
        logText = "[" + msgtime + "] " + sname + ", " + cname + " (" + str(sid) + ", " + str(cid) + "), " + sender + ": " + msg
        print(logText)

        settings = default_settings

        in_list = False
        server_list = parse(server_path)
    
        for server in server_list:
            if str(sid) == server[0]:
                in_list = True
                settings["prefix"] = server[1]
                settings["max_potatoes"] = int(server[2])
                settings["max_sentences"] = int(server[3])
                settings["react_probability"] = int(server[4])
    
        if in_list == False:
            text = str(sid) + " " + settings["prefix"] + " " + str(settings["max_potatoes"]) + " " + str(settings["max_sentences"]) + " " + str(settings["react_probability"])
            addline(server_path, text)
    
        if msg.startswith(settings["prefix"]):
            cmd_properties = {
                "client": client,
                "message": message,
                "settings": settings,
                }
            await CommandHandler.run(cmd_properties)
        else:
            await react(message, settings["react_probability"])

    try:
        client.loop.run_until_complete(client.start(sys.argv[1]))
    except KeyboardInterrupt:
        client.loop.run_until_complete(client.logout())
    finally:
        client.loop.close()

def start_bot():
    queue = multiprocessing.Queue()
    parent_pipe, child_pipe = multiprocessing.Pipe()
    thread = multiprocessing.Process(target=client_thread, args=(child_pipe, queue,))
    try:
        thread.start()
    except KeyboardInterrupt:
        os.kill(thread.pid, signal.SIGINT)

if __name__ == "__main__":
    print("Finished initialisation. Connecting...")
    start_bot()