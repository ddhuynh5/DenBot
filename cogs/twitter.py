""" Twitter/X Cog """

import discord
from discord.ext import commands


class Twitter(commands.Cog):
    """ Cog to interact with Twitter/X """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        """ Fix Twitter/X Embeds """

        if ("https://twitter.com/" in message.content):
            suffix = message.content.split("twitter.com/")[1]
            modified_url = "http://fxtwitter.com/" + suffix
            await message.delete()
            await message.channel.send(modified_url + " | **__" + str(message.author) + "__**")
        elif ("https://x.com/" in message.content):
            suffix = message.content.split("x.com/")[1]
            modified_url = "http://fixupx.com/" + suffix
            await message.delete()
            await message.channel.send(modified_url + " | **__" + str(message.author) + "__**")

async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Twitter(bot))
