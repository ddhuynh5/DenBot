# Imports
import os
import json
import discord
import requests
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# on startup


@client.event
async def on_ready():
    print("Connected to bot: {}".format(client.user.name))
    print("Bot ID: {}".format(client.user.id))

# code to mention a user whenever another user joins a voice channel
# in this example, my friend andy will be pinged
# andy_id = 217419100018704384


@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel and member.id == 210225328402989056:
        andy_id = 217419100018704384
        channel = client.get_channel(395879704328142849)
        await channel.send(f"<@{andy_id}> get on :smiling_imp:")



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
async def users(ctx):
    server = client.get_guild(395872472370642944)
    await ctx.send(f"""This server has {server.members} members""")


@client.command()
async def test(ctx):
    await ctx.send("test")


@client.command()
async def cat(ctx, *, arg):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    res = response.json()
    
    for r in res:
        await ctx.send(r["url"])


client.run(TOKEN)
