""" Fun Commands """

import discord
import requests

from discord.ext import commands


class Fun(commands.Cog):
    """ Fun Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='users', help='Gets the # of users in the server')
    async def users(self, ctx):
        """ Get number of server members """

        await ctx.send(f"""This server has {len(ctx.guild.members)} members""")

    @commands.command(name='cat', help='A Fun cat appears!')
    async def cat(self, ctx):
        """ Uses TheCatAPI to get a Fun cat picture/GIF """

        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url, timeout=5)
        res = response.json()

        await ctx.send(res[0]["url"])

    @commands.command(name="austin", help="'I just need a command that @ austin - Richard'")
    async def austin(self, ctx):
        """ Command to @ my friend austin """

        austin = 181438247015022592
        await ctx.send(f"Hey <@{austin}>, {ctx.author.mention} wanted you")

    @commands.command(name="member_list", help="List of members in embed")
    async def member_list(self, ctx):
        """ Gets an embedded list of all server members """

        members = ctx.guild.members
        data = "\n".join([member.name for member in members])
        embed = discord.Embed(
            title="RAH",
            description=f"{data}",
            color=discord.Color.purple()
        )

        await ctx.send(embed=embed)


async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Fun(bot))
