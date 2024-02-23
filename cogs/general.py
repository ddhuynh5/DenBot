""" general.py """

import discord
from discord.ext import commands
import asyncio

class General(commands.Cog):
    """ General/Basic Commands Cog """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remind", help="Usage: !remind [number] [s/m/h/d] [msg]")
    async def remind(self, ctx, duration: str, *, msg: str):
        """ Removes a specified number of  """

        seconds = self.parse_duration(duration)

        if seconds is None:
            await ctx.send("Invalid duration format. Please use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.")
            return
        
        embed = discord.Embed(title=f"Duration: {duration}", description=msg, color=0x00ff00)

        await ctx.send(f"Reminder set for {duration}: {msg}")
        await asyncio.sleep(seconds)
        await ctx.send(f"Hey {ctx.author.mention}, here's the reminder you requested")
        await ctx.send(embed=embed)

    def parse_duration(self, duration: str) -> int:
        """ Parse the duration string and convert it to seconds """

        try:
            unit = duration[-1].lower()
            value = int(duration[:-1])

            if unit == 's':
                return value
            elif unit == 'm':
                return value * 60
            elif unit == 'h':
                return value * 3600
            elif unit == 'd':
                return value * 86400
            else:
                return None
        except ValueError:
            return None

async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(General(bot))
