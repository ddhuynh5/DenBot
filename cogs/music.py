""" music.py """

import asyncio
import youtube_dl
import discord
from discord.ext import commands


youtube_dl.utils.bug_reports_message = lambda: ''

FORMAT_OPTIONS = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

FFMPEG_OPTIONS = {
    'options': '-vn'
}

youtube = youtube_dl.YoutubeDL(FORMAT_OPTIONS)


class MusicPlayer(discord.PCMVolumeTransformer):
    """ Music Player Cog """

    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        """
            Takes in URL as param and returns filename of audio file
            to be downloaded
        """

        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None,
            lambda: youtube.extract_info(url, download=not stream)
        )

        if 'entries' in data:
            data = data['entries'][0]

        return data['title'] if stream else youtube.prepare_filename(data)


class Music(commands.Cog):
    """ Commands for user to interact with music player """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', help='Make the bot to join the voice channel')
    async def join(self, ctx):
        """ Makes the bot join the channel (if the author is currently in a voice channel) """

        if not ctx.message.author.voice:
            await ctx.send(
                f"{ctx.message.author.name}... You are not connected to a voice channel."
            )
            return

        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(name='leave', help='Make the bot leave the voice channel')
    async def leave(self, ctx):
        """ Makes the bot leave the voice channel """

        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(name='play', help='Plays a song')
    async def play(self, ctx, url):
        """ Plays a song, takes in a YT URL as a parameter """

        try:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            if voice is None:
                channel = ctx.message.author.voice.channel
                await channel.connect()

            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                file_name = await MusicPlayer.from_url(url, loop=self.bot.loop)
                voice_channel.play(discord.FFmpegPCMAudio(
                    executable="ffmpeg.exe", source=file_name))

            await ctx.send(f"**Now Playing:** {url}")

        except AttributeError:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command(name='pause', help='Pause the song')
    async def pause(self, ctx):
        """ Pauses the currently playing song """

        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

    @commands.command(name='resume', help='Resumes the song')
    async def resume(self, ctx):
        """ Resumes the currently paused song """

        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use !play [song_name]")

    @commands.command(name='stop', help='Stops the song')
    async def stop(self, ctx):
        """ Stops the currently playing song """

        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")


async def setup(bot):
    """ Adds the cog to the bot """

    await bot.add_cog(Music(bot))
