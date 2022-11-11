# Imports
import os
import json
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.command()
async def test(ctx):
    await ctx.send("test")


@client.command(name="users", description="shows number of members in server")
async def users(ctx):
    await ctx.send(f"""This server has {id.member_count} members""")


@client.command()
async def cat(ctx, arg):
    await ctx.channel.send(arg)
    #url = "https://api.thecatapi.com/v1/images/search"
    #response = requests.get(url)
    #res = response.json()
    
    #for r in res:
    #    await ctx.send(r["url"])


client.run(TOKEN)
