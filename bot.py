# Imports
import os
from tkinter.messagebox import askyesno
from unittest import async_case
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')

# on startup


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# code to mention a user whenever another user joins a voice channel
# in this example, my friend andy will be pinged
# andy_id = 217419100018704384


@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel and member.id == 210225328402989056:
        andy_id = "217419100018704384"
        channel = client.get_channel(395879704328142849)
        await channel.send(f"<@{andy_id}> get on :smiling_imp:")

# code to react to user msg


@client.event
async def on_message(message):
    if message.content == "pog":
        await message.channel.send('very pog')

# code to kick a user on first vc join instance


@client.event
async def on_voice_state_update(member, before, after):
    kick_counter = 0
    while (kick_counter == 0):
        if not before.channel and after.channel and member.id == 181438247015022592:
            channel = client.get_channel(395879704328142849)
            await member.move_to(None)
            kick_counter = 1

client.run(TOKEN)
