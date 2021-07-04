import discord
from discord.ext import commands
from discord.ext.commands import Context

import os

TEST_MODE = os.environ.get('TEST_MODE', False)
DISCORD_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

client = commands.Bot(command_prefix = commands.when_mentioned_or('.'))

@client.event
async def on_ready():
    print("Discord Bot is ready")
    activity = discord.Activity(type=discord.ActivityType.playing, name="Waiting for your commands.")
    await client.change_presence(activity=activity)

@client.command()
async def commands(ctx: Context):
    commandFile = open("/app/src/command_text/commands.txt", "r")
    commandsFromFile = commandFile.read()

    title = "Overview of all commands"
    description = commandsFromFile

    embeddedMessage = discord.Embed(title = title, description = description)
    await ctx.send(embed = embeddedMessage)

client.run(DISCORD_TOKEN)