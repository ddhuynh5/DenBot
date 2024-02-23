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

        if "https://twitter.com/" in message.content:
            modified_url = "https://fxtwitter.com/"
            new_content = message.content.replace("https://twitter.com/", modified_url)
            await message.delete()
            await message.channel.send(new_content + " | Sent by: **__" + str(message.author.nick) + "__**")

        elif "https://x.com/" in message.content:
            modified_url = "https://fixupx.com/"
            new_content = message.content.replace("https://x.com/", modified_url)
            await message.delete()
            await message.channel.send(new_content + " | Sent by: **__" + str(message.author.nick) + "__**")


async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Twitter(bot))
