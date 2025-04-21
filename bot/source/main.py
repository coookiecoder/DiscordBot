import os

import discord
from discord.ext import commands

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.slash_command(name="ping", description="command to ping the bot")
async def ping(interaction):
    await interaction.response.send_message('pong')

bot.run(os.environ.get('TOKEN', 'nope'))