import os

from discord import Interaction
from discord.ext import commands

from psycopg2 import connect

from database_io import validate_table_role, add_role, remove_role
from database_io import validate_table_twitch, add_twitch, remove_twitch
from database_io import validate_table_youtube, add_youtube, remove_youtube

bot = commands.Bot()
connection = connect(dbname="default", user="postgres", password=os.environ.get('DATABASE_PASSWORD', 'nope'), host="database", port="5432")
cursor = connection.cursor()

@bot.event
async def on_ready():
    validate_table_role()
    validate_table_twitch()
    validate_table_youtube()
    print(f'Logged in as {bot.user} (ID: {bot.user.id}) database version {cursor.execute('SELECT version()')}')

@bot.slash_command(name="ping", description="command to ping the bot")
async def ping(interaction: Interaction):
    await interaction.response.send_message('pong')

@bot.slash_command(name="debug", description="UwU")
async def ping(interaction: Interaction):
    cursor.execute('SELECT version()')
    await interaction.response.send_message(f'Logged in as {bot.user} (ID: {bot.user.id}) database version {cursor.fetchone()}')

@bot.slash_command(name="add_role", description="Add a role to the database")
async def add_role(interaction: Interaction, name: str, role_id: str, emoji:str):
    for role in interaction.user.roles:
        if role.permissions.manage_channels:
            add_role(name, role_id, emoji)
            await interaction.response.send_message(f'added {name} with role id {role_id} with emoji {emoji}')
            return

    interaction.response.send_message('You can do that')

@bot.slash_command(name="add_twitch_link", description="Add a twitch link to the database")
async def add_twitch_link(interaction: Interaction, link: str):
    for role in interaction.user.roles:
        if role.permissions.manage_channels:
            add_twitch(link)
            await interaction.response.send_message(link)
            return

    interaction.response.send_message('You can do that')

@bot.slash_command(name="add_youtube_link", description="Add a youtube link to the database")
async def add_youtube_link(interaction: Interaction, link: str):
    for role in interaction.user.roles:
        if role.permissions.manage_channels:
            add_youtube(link)
            await interaction.response.send_message(link)
            return

    interaction.response.send_message('You can do that')

bot.run(os.environ.get('TOKEN', 'nope'))