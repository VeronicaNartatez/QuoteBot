# Import the required modules
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

# Set the confirmation message when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Set the commands for your bot
@bot.command()
async def greet(ctx):
    response = 'Hello, I am your discord bot'
    await ctx.send(response)

@bot.command()
async def list_command(ctx):
    response = 'You can use the following commands: \n !greet \n !list_command \n !functions'
    await ctx.send(response)

@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord chatbot! I will reply to your command!'
    await ctx.send(response)

message =

@client.even


#to get bot to respond
@client.event
async def on_message(message):
    if message.content.startswith(“!”):
        split_message = message.content.split()  # [“!!reply”, “messageid”]
        if split_message[0] == “!reply”:
            message_id = int(split_message[1])  # message.content is a str
            reply_to = await message.channel.fetch_message(message_id)
            await reply_to.reply(“Hello
            World!”)


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))