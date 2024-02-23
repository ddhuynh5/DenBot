""" fun.py """

import asyncio
import discord
import requests

from discord.ext import commands


class Fun(commands.Cog):
    """ Misc. Fun Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cat', help='A Fun cat appears!')
    async def cat(self, ctx):
        """ Uses TheCatAPI to get a fun cat picture/GIF """

        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url, timeout=5)
        res = response.json()
        await ctx.send(res[0]["url"])

    @commands.command(name="austin", help="'I just need a command that @ austin - Richard'")
    async def austin(self, ctx):
        """ Command to @ my friend austin """

        austin = 181438247015022592
        await ctx.send(f"Hey <@{austin}>, {ctx.author.mention} wanted you")


async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Fun(bot))
