# CommandHandler.py

import asyncio
import discord
import Commands.calc
import Commands.rannum
import Commands.ransen
import Commands.potatoes
import Commands.amipotato
import Commands.eightball
import Commands.info
import Commands.help
import Commands.test
import Commands.cm

PERSONAL_ENABLED = False
try:
    import Personal.CommandHandler
    PERSONAL_ENABLED = True
    print("Personal module is enabled.")
except ImportError:
    pass

async def invalid(cmd_properties):
    await client.send_message(cmd_properties["message"].channel, "That is not a valid command. For a list of commands, use `" + cmd_properties["settings"]["prefix"] + "help`.")

async def run(cmd_properties):
    
    msg = cmd_properties["message"].content[len(cmd_properties["settings"]["prefix"]):]
    command = msg.split(" ")[0]
    cmd_properties["args"] = msg[len(command)+1:].split(" ")

    if command == "calc" or command == "calculate":
        await Commands.calc.run(cmd_properties)
    elif command == "rannum" or command == "randomnumber":
        await Commands.rannum.run(cmd_properties)
    elif command == "ransen" or command == "randomsentence":
        await Commands.ransen.run(cmd_properties)
    elif command == "potatoes":
        await Commands.potatoes.run(cmd_properties)
    elif command == "amipotato":
        await Commands.amipotato.run(cmd_properties)
    elif command == "8ball":
        await Commands.eightball.run(cmd_properties)
    elif command == "info":
        await Commands.info.run(cmd_properties)
    elif command == "help":
        await Commands.help.run(cmd_properties)
    elif command == "test":
        await Commands.test.run(cmd_properties)
    elif command == "cm" or command == "convertmoney":
        await Commands.cm.run(cmd_properties)

    elif PERSONAL_ENABLED and str(cmd_properties["message"].author.id) == "163997823245746177":
        await Personal.CommandHandler.run(cmd_properties)
    else:
        await invalid(cmd_properties)