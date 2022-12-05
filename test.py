""" Test Bot """

# Imports
import os
import json
import discord
import requests
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class MyBot(commands.Bot):

    def __init__(self, command_prefix, intents):
        commands.Bot.__init__(
            self,
            command_prefix=command_prefix,
            intents=intents
        )

    # on startup
    async def on_ready(self):
        print("Connected to bot: {}".format(self.user.name))
        print("Bot ID: {}".format(self.user.id))

    # code to mention a user whenever another user joins a voice channel
    # in this example, my friend andy will be pinged
    # andy_id = 217419100018704384
    @commands.Bot.event
    async def on_voice_state_update(self, member, before, after):
        if not before.channel and after.channel and member.id == 210225328402989056:
            andy_id = 217419100018704384
            channel = self.get_channel(395879704328142849)
            await channel.send(f"<@{andy_id}> get on :smiling_imp:")

    # code to react to user msg
    @commands.Bot.event
    async def on_message(self, message):
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
            await message.channel.send("Nice try silly goose")
            await message.delete()

        await commands.Bot.process_commands(message)

    # Gets current server member count
    @commands.Bot.command()
    async def users(self, ctx):
        await ctx.send(f"""This server has {len(ctx.guild.members)} members""")

    @commands.Bot.command()
    async def test(self, ctx):
        await ctx.send("test")

    # Calls Random Cat API and sends response to channel
    @commands.Bot.command()
    async def cat(self, ctx):
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url)
        res = response.json()

        for r in res:
            await ctx.send(r["url"])


bot = MyBot(command_prefix="!", intents=discord.Intents.all())
bot.run("TOKEN")
