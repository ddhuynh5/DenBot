""" general.py """

import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from typing import Optional

class General(commands.Cog):
    """ General/Basic Commands Cog """

    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(name="remind", help="Usage: !remind [number] [s/m/h/d] [msg]")
    async def remind(self, ctx, duration: Optional[str], *, msg: Optional[str]):
        """ Removes a specified number of messages depicted by user """

        if duration is None:
            embed = discord.Embed(
                title="Usage",
                description="!remind [number] [s/m/h/d] [msg]",
                color=discord.Color.purple()
            )
            
            await ctx.send(embed=embed)
            return
        elif msg is None:
            embed = discord.Embed(
                title="Usage",
                description="Don't forget your message! !remind [number] [s/m/h/d] [msg]",
                color=discord.Color.purple()
            )
            
            await ctx.send(embed=embed)
            return
        else:
            seconds = self.parse_duration(duration)
            
            if seconds is None:
                await ctx.send("Invalid duration format. Please use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.")
                return
            
            embed = discord.Embed(title=f"Duration: {duration}", description=msg, color=0x00ff00)

            await ctx.send(f"Reminder set for {duration}: {msg}")
            await asyncio.sleep(seconds)
            await ctx.send(f"Hey {ctx.author.mention}, here's the reminder you requested")
            await ctx.send(embed=embed)
    
    @commands.command(name="users", help="Gets the # of users in the server")
    async def users(self, ctx):
        """ Get number of server members """

        await ctx.send(f"This server has {len(ctx.guild.members)} members")

    @commands.command(name="members", help="List members")
    async def members(self, ctx):
        """ Gets an embedded list of all server members """

        mentions = [member.mention for member in ctx.guild.members]
        data = "\n".join(mentions)
        embed = discord.Embed(
            title="Server Members:",
            description=f"{data}",
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

    @commands.command(name="timer", help="Countdown [s/m/h/d]")
    async def timer(self, ctx, duration: Optional[str]):
        """ Countdown for x duration inputted by user """
        
        if duration is None:
            embed = discord.Embed(
                title="Usage",
                description="!timer duration [s/m/h/d]",
                color=discord.Color.purple()
            )
            
            await ctx.send(embed=embed)
            return
        else:
            try:
                seconds = self.parse_duration(duration)

                if seconds is None:
                    await ctx.send("Invalid duration format. Please use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.")
                    return

                if seconds <= 0:
                    await ctx.send("Negatives numbers don't exist, try a positive number!")
                    return
                message = await ctx.send("**Countdown Timer:** {seconds}")

                while True:
                    seconds -= 1
                    if seconds == 0:
                        await message.edit(content="Finished!")
                        break
                    await message.edit(content=f"**Countdown Timer:** {seconds}")
                    await asyncio.sleep(1)

                await ctx.send(f"{ctx.author.mention} Your countdown timer ({duration}) has ended!")
            except ValueError:
                await ctx.send("Must be a number!")

    @commands.command(name="roles", help="Customize your roles!")
    async def roles(self, ctx, selection: Optional[str]):
        """ Role management for non-moderator+ """

        roles_list = [
            "palworld",
            "osu",
            "minecraft",
            "bloons",
            "Hazbin",
            "cleanup",
            "denbot"
        ]

        if selection is None:
            data = "\n".join(roles_list)

            embed = discord.Embed(
                title="Available Roles:",
                description=f"{data}",
                color=discord.Color.purple()
            )

            await ctx.send(embed=embed)
            return
        else:
            if selection not in roles_list:
                await ctx.send("Name not found in available roles!")
                return

            member = ctx.message.author
            role = get(ctx.guild.roles, name=selection)
            
            if role not in ctx.author.roles:
                await member.add_roles(role)
                await ctx.send(f"Added {role}! To remove: !roles {role}")
            else:
                await member.remove_roles(role)
                await ctx.send(f"Removed {role}!")

async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(General(bot))
