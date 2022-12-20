import youtube_dl
import discord
import asyncio


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
        filename = data['title'] if stream else youtube.prepare_filename(data)
        return filename
