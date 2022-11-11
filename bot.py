# Imports
import os
import json
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# code to react to user msg
@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == "pog":
            await message.channel.send("very pog")
        elif message.content == "very pog":
            await message.channel.send("the poggest")

    if len(message.attachments) > 0 and message.author.id == 181438247015022592:
        await message.channel.send("Nice try dumbass")
        await message.delete()
    
    await client.process_commands(message)


@client.command()
async def test(ctx):
    await ctx.send("test")


@client.command()
async def cat(ctx, arg):
    await ctx.channel.send(arg)
    #url = "https://api.thecatapi.com/v1/images/search"
    #response = requests.get(url)
    #res = response.json()
    
    #for r in res:
    #    await ctx.send(r["url"])


client.run(TOKEN)
