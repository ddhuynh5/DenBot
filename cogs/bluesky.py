""" bluesky.py """

import discord
from discord.ext import commands


class BlueSky(commands.Cog):
    """ Cog to interact with BlueSky """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        """ Fix BlueSky Embeds """

        old_url = "https://bsky.app/"

        if old_url in message.content:
            modified_url = "https://fxbsky.app/"
            new_content = message.content.replace(old_url, modified_url)
            await message.delete()
            await message.channel.send(new_content + " | Sent by: **__" + str(message.author.display_name) + "__**")

async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(BlueSky(bot))
