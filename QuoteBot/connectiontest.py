# bot.py
#this is an instance of a client. this helps implement the bot in general!
#client = an object that represents a connection to Discord

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#on_ready = handles event when client makes request to Discord
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)