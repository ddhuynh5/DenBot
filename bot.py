# Imports
import os
import json
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!")

@client.command()
async def test(ctx):
    await ctx.send("test")


client.run(TOKEN)
