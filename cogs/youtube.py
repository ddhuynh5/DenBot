""" youtube.py """

import os
import discord
from discord.ext import commands
from googleapiclient.discovery import build

class YouTube(commands.Cog):
    """ Cog to interact with YouTube """

    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv("YT_KEY")
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    @commands.command(name="search", help="Look up the most recent 50 videos of a channel; Usage: !search [channel name]")
    async def lookup(self, ctx, channel_name: str):
        """ 
            Looks up a YT channel by name

            Returns: List of 50 videos sorted by date (descending)
        """

        channel_request = self.youtube.search().list(
            q=channel_name,
            part="snippet",
            type="channel",
            maxResults=1
        )
        channel_response = channel_request.execute()
        actual_name = channel_response["items"][0]["snippet"]["title"]
        description = channel_response["items"][0]["snippet"]["description"]

        if channel_response["items"]:
            channel_id = channel_response["items"][0]["id"]["channelId"]
        else:
            await ctx.send("No channel found with the provided name")

        request = self.youtube.search().list(
            part="snippet",
            order="date",
            channelId=channel_id,
            type="video",
            maxResults=50
        )

        response = request.execute()
        fields = []

        for item in response["items"]:
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_link = f"https://www.youtube.com/watch?v={video_id}"

            fields.append((video_title, video_link))
        
        embed = discord.Embed(
            title=actual_name, 
            description=description, 
            color=discord.Color.blue()
        )

        max_fields_per_page = 5

        pages = [fields[i:i + max_fields_per_page] for i in range(0, len(fields), max_fields_per_page)]

        emoji_back = "⬅️"
        emoji_forward = "➡️"
        current_page = 0

        for name, value in pages[current_page]:
            embed.add_field(name=name, value=f"[Watch]({value})", inline=False)

        message = await ctx.send(embed=embed)

        if len(pages) > 1:
            await message.add_reaction(emoji_back)
            await message.add_reaction(emoji_forward)

        def check(reaction, user):
            """ Checks if the user reacting to the embed is the author of the command, and that the arrow emotes are used only """
            return user == ctx.author and str(reaction.emoji) in [emoji_back, emoji_forward]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
            except TimeoutError:
                break
            else:
                if str(reaction.emoji) == emoji_back:
                    current_page = (current_page - 1) % len(pages)
                elif str(reaction.emoji) == emoji_forward:
                    current_page = (current_page + 1) % len(pages)

                embed.clear_fields()
                for name, value in pages[current_page]:
                    embed.add_field(name=name, value=f"[Watch]({value})", inline=False)

                await message.edit(embed=embed)
                await reaction.remove(ctx.author)

async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(YouTube(bot))
