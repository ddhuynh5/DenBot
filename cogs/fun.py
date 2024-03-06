""" fun.py """

import os
import discord
import requests
import random
from discord.ext import commands
from urllib import parse
from typing import Optional

GIPHY = os.getenv("GIPHY")


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

    @commands.command(name="gif", help="get a random GIF")
    async def gif(self, ctx, *, msg: Optional[str]):
        if msg is None:
            embed = discord.Embed(
                title="Usage",
                description="!gif [msg]",
                color=discord.Color.purple()
            )
            
            await ctx.send(embed=embed)
            return
        else:
            url = "http://api.giphy.com/v1/gifs/search"
            num = random.randint(0, 9)

            params = parse.urlencode({
                "q": msg,
                "api_key": GIPHY,
                "limit": "10"
            })

            response = requests.get(url=url, params=params)
            res = response.json()

            await ctx.send(res["data"][num]["url"])


async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Fun(bot))
