# Import the required modules
from tkinter import Label

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#make command thatll apply the class, make the class first
class FeedbackModal(discord.ui.Modal, title="Make your quote!")
    quote_title = discord.ui.TextInput(
        style = discord.TextStyle.short,
        Label = "Title",
        required = true,
        person_whos_quoting="Who are you quoting?"
    )

    message = discord.ui.TextInput(
        style = discord.ui.TextStyle.long,
        Label = "Title",
        required = true,
        max_length = 1000,
        quote = "Enter the quote"
    )

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

# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))