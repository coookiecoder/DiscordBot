# This example requires the 'members' and 'message_content' privileged intents to function.

import os

import discord
from discord.ext import commands

description = "UwU"

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.environ.get('TOKEN', 'nope'))