# Imports
import os
import json
import discord
import requests
import random
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# on startup


@bot.event
async def on_ready():
    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))

    for guild in bot.guilds:
        print(guild)
        print(guild.id)

# code to mention a user whenever another user joins a voice channel
# in this example, my friend andy will be pinged
# andy_id = 217419100018704384


@bot.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel and member.id == 210225328402989056:
        andy_id = 217419100018704384
        channel = bot.get_channel(395879704328142849)
        await channel.send(f"<@{andy_id}> get on :smiling_imp:")


# code to react to user msg
@bot.event
async def on_message(message):
    num = random.randint(-1000, 1000)

    if not message.author.bot:
        if message.content == "pog":
            await message.channel.send("very pog")
        elif message.content == "very pog":
            await message.channel.send("the poggest")

    if message.author.id == 181438247015022592 and (num <= 50 and num >= 100):
        await message.delete()
        await message.channel.send(embed=discord.Embed(title=":smiling_imp:", description=message.content))

    if len(message.attachments) > 0 and message.author.id == 181438247015022592:
        await message.channel.send("Nice try dumbass")
        await message.delete()

    await bot.process_commands(message)


@bot.command()
async def users(ctx):
    server = bot.get_guild(395872472370642944)
    await ctx.send(f"""This server has {server.members} members""")


@bot.command()
async def test(ctx):
    await ctx.send("test")


@bot.command()
async def cat(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    res = response.json()

    for r in res:
        await ctx.send(r["url"])


bot.run(TOKEN)
