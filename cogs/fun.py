""" Fun Commands """

import asyncio
import discord
import requests

from discord.ext import commands


class Fun(commands.Cog):
    """ Misc. Fun Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='users', help='Gets the # of users in the server')
    async def users(self, ctx):
        """ Get number of server members """
        await ctx.send(f"""This server has {len(ctx.guild.members)} members""")

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

    @commands.command(name="timer", help="Countdown [currently only works with seconds]")
    async def timer(self, ctx, seconds):
        """ Counts down the number of seconds inputted by user """
        try:
            converted_seconds = int(seconds)
            if converted_seconds <= 0:
                await ctx.send("Negatives numbers don't exist, try a positive number!")
                return
            message = await ctx.send("**Countdown Timer:** {seconds}")

            while True:
                converted_seconds -= 1
                if converted_seconds == 0:
                    await message.edit(content="Finished!")
                    break
                await message.edit(content=f"**Countdown Timer:** {converted_seconds}")
                await asyncio.sleep(1)

            await ctx.send(f"{ctx.author.mention} Your countdown timer has ended!")
        except ValueError:
            await ctx.send("Must be a number!")


async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Fun(bot))
