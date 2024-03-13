import imp
from re import I
import discord
import os
from dotenv import load_dotenv
import requests
import json
import random
from replit import db #Or any other database available
#How can I log in to the bot(make it discord' active)
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client()

sad_words = [
    "sad",
    "depressed",
    "unhappy",
    "angry",
    "miserable",
    "depressing",
]  # To look for this words in the dictionary: Text Mining

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot !",
]

if "responding" not in db.keys():
    db["responding"] = True

def get_quote():
    response = requests.get("https://zenquotes.io/api/quotes/")
    json_data = json.load(
        response.text
    )  # no need to dump if data is from API(generate data)
    quote = (
        json_data[0]["q"] + " -" + json_data[0]["a"]
    )  # To get the quote and it's author out of it
    return quote

def update_encouragements(encouraging_message):
    if "encouragments" in db.keys():
        encouragements = db["encouragements"] #Back-end in python
        encouragements.append(encouraging_message)
        db["enouragements"] = encouragements
    else:
        db["encouragements"] =[encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements(index)
        db["encouragements"] = encouragements

@client.event  # asynchronous Discord lybrary(registering an event)
async def on_ready():
    print(f"We have logged in as {client.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith(
        "$hello"
    ):  # A command is represented by the $ in front of it
        quote = get_quote()
        await message.channel.send("Hello!")
        
    if msg.startswith(
        "$inspire"
    ):  # A command is represented by the $ in front of it
        quote = get_quote()
        await message.channel.send(quote)
        
    if db["responding"]: #To being able to turning it on and off
        options = starter_encouragements
        if "encouragements" is db.key():
            options += db["encouragements"]
        
        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(starter_encouragements))
            
    #Create new encouraging message
    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1] #first part starting in 2nd position
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")
        
    #Deletes encouragement message
    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.key:
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)
        
    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)
        
    if msg.startswith("$responding"):
        value = msg.split("$responding", 1)[1]
        
        if value.lowr() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on!")
        else:
            db["responding"] = False
            await message.channel.send("Responding is offf :(")

keep_alive()
client.run(os.getenv('TOKEN'))  # os used to get a file env
