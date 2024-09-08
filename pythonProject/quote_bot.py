# Import the required modules
from tkinter import Label

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

import settings
import utils

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
GUILD_ID = 1279194893037867021

#make command thatll apply the class, make the class first
class QuoteModal(discord.ui.Modal, title="Put in your quote!"):
    quotePerson = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Person to quote",
        required=True,
        placeholder="Who are you quoting?"
    )

    quoteMessage = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Person to quote",
        required=True,
        placeholder="Who are you quoting?",
        max_length=500
    )

@bot.event
async def on_ready():
    bot.tree.copy_global_to(guild=settings.GUILDS_ID)
    await bot.tree.sync(guild=settings.GUILDS_ID)
    await utils.load_videocmds(bot)

@bot.tree.command()
async def quote(interaction: discord.Interaction):
    quote_modal = QuoteModal(),
    await interaction.response.send_modal(quote_modal)


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