import os
import json
import discord
import requests
import random

from discord.ext import commands, tasks
from music_player import MusicPlayer
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    """ on startup """

    print("Connected to bot: {}".format(bot.user.name))
    print("Bot ID: {}".format(bot.user.id))

    for guild in bot.guilds:
        print(guild)
        print(guild.id)


@bot.event
async def on_voice_state_update(member, before, after):
    """ 
        code to mention a user whenever another user joins a voice channel
        in this example, my friend andy will be pinged
        andy_id = 217419100018704384
    """

    if not before.channel and after.channel and member.id == 210225328402989056:
        andy_id = 217419100018704384
        channel = bot.get_channel(395879704328142849)
        await channel.send(f"<@{andy_id}> get on :smiling_imp:")


@bot.event
async def on_message(message):
    """ code to react to user msg """

    num = random.randint(-500, 500)

    if not message.author.bot:
        if message.content == "pog":
            await message.channel.send("very pog")
        elif message.content == "very pog":
            await message.channel.send("the poggest")

    if message.author.id == 181438247015022592 and (num <= 50 and num >= 100):
        await message.delete()
        await message.channel.send(embed=discord.Embed(title=":smiling_imp:", description=message.content))

    if len(message.attachments) > 0 and message.author.id == 181438247015022592 and (num <= 50 and num >= 100):
        await message.channel.send("Nice try silly goose")
        await message.delete()

    await bot.process_commands(message)


@bot.command(name='users', help='Gets the # of users in the server')
async def users(ctx):
    await ctx.send(f"""This server has {len(ctx.guild.members)} members""")


@bot.command()
async def test(ctx):
    await ctx.send("test")


@bot.command(name='cat', help='A random cat appears!')
async def cat(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    res = response.json()

    for r in res:
        await ctx.send(r["url"])


@bot.command(name='join', help='Make the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='leave', help='Make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='play', help='Plays a song')
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await MusicPlayer.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(
                executable="ffmpeg.exe", source=filename))

        await ctx.send('**Now playing:** {}'.format(filename))

    except:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='pause', help='Pause the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use !play [song_name]")


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


bot.run(TOKEN)
