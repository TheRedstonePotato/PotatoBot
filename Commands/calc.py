# commands/calc.py

import math
import asyncio
import discord

def validfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def validint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def getNumber(value):
    if validfloat(value):
        return value
    value = value.lower()
    if value == "pi" or value == "π":
        return str(math.pi)
    elif value == "tau" or value == "τ":
        return str(math.tau)
    elif value == "e":
        return str(math.e)
    elif value == "phi" or value == "φ" or value == "gr" or value == "goldenratio":
        return "1.618033988749895"
    elif value == "γ" or value == "e-m":
        return "0.577215664901532"
    else:
        return "invalid"

def getOperator(value):
    value = value.lower()
    if value == "add" or value == "plus" or value =="+" or value == "and":
        return "+"
    elif value == "minus" or value == "subtract" or value =="-" or value == "−" or value == "takeaway":
        return "-"
    elif value == "times" or value == "multiply" or value =="multiplied-by" or value == "*" or value == "x" or value == "×" or value == "⋅":
        return "*"
    elif value == "divided-by" or value == "divide" or value == "÷" or value == "/":
        return "/"
    elif value == "pow" or value == "**" or value == "^":
        return "^"
    elif value == "mod" or value == "%":
        return "%"
    else:
        return "invalid"
        
def getSyntax(prefix):
    syntax = "`" + prefix + "calc <number1> <operator> [number2]`"
    return syntax
    
def getOperators(prefix):
    ops = "Operators are `+` `-` `*` `/` `^` `%` and `!`"
    return ops

async def run(cmd_properties):
    client = cmd_properties["client"]
    message = cmd_properties["message"]
    args = cmd_properties["args"]
    prefix = cmd_properties["settings"]["prefix"]
    syntax = getSyntax(prefix)
    ops = getOperators(prefix)
    output = ""
    
    if len(args) == 2:
        if args[1] == "!" or args[1].lower() == "factorial":
            if validint(args[0]):
                if int(args[0]) < 0:
                    output = "Undefined"
                    await client.send_message(message.channel, output)
                elif int(args[0]) > 500:
                    output = "Can't calculate factorials for numbers above 500."
                    await client.send_message(message.channel, output)
                else:
                    output = math.factorial(int(args[0]))
                    await client.send_message(message.channel, output)
            else:
                output = "Non-integer factorials are not supported."
                await client.send_message(message.channel, output)
        else:
            output = "Invalid syntax.\n" + syntax
            await client.send_message(message.channel, output)

    elif len(args) == 3:

        if getNumber(args[0]) == "invalid":
            output = "The first argument is not a valid number."
            await client.send_message(message.channel, output)
            return
        n1 = float(getNumber(args[0]))

        if getOperator(args[1]) == "invalid":
            output = "The second argument is not a valid operator.\n" + ops
            await client.send_message(message.channel, output)
            return
        op = getOperator(args[1])

        if getNumber(args[2]) == "invalid":
            output = "The third argument is not a valid number."
            await client.send_message(message.channel, output)
            return
        n2 = float(getNumber(args[2]))

        if op == "+":
            if args[1].lower() == "plus" or args[1] == "+":
                if n1 == 9 and n2 == 10:
                    output = "21"
                else:
                    output = str(n1 + n2)
            else:
                output = str(n1 + n2)
        elif op == "-":
            output = str(n1 - n2)
        elif op == "*":
            output = str(n1 * n2)
        elif op == "/":
            if n2 == 0:
                output = "Undefined"
            else:
                output = str(n1 / n2)
        elif op == "^":
            if n1 < 0 and (1 / n2) % 2 == 0:
                output = "Complex numbers are not supported."
            elif n1 == 0 and n2 == 0:
                output = "Undefined"
            else:
                output = str(n1 ** n2)
        elif op == "%":
            if validint(n1) == False or validint(n2) == False:
                output = "Modular operations are only supported for integers."
            elif n2 == 0:
                output = "Undefined"
            else:
                output = str(n1 % n2)

        if output == "-0.0" or output == "-0":
            output = "0"
        elif output.endswith(".0"):
            output = output[:-2]

        await client.send_message(message.channel, output)

    else:
        output = "Invalid syntax.\n" + syntax
        await client.send_message(message.channel, output)