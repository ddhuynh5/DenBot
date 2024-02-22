""" Users' Birthday Module """

import os
import discord
from discord.ext import commands
from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()
DB_PASS = os.getenv("DB_PASS")

client = MongoClient(f"mongodb+srv://ddhuynh:{DB_PASS}@discordbotcluster.qshhl7v.mongodb.net/")

class Birthday(commands.Cog):
    """ All Birthday Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bday_list', help='Gets all users registered for birthday commands')
    async def bday_list(self, ctx):
        """ Runs a Find() on users collection """

        db = client.discord
        collection = db.users
        cursor = collection.find()
        embed = discord.Embed(title="Currently Registered Users", color=discord.Color.blue())

        for user in cursor:
            embed.add_field(name="User", value=f'<@{str(user["user_id"])}>', inline=False)
            embed.add_field(name="Birthdays", value=user["date"], inline=False)

        await ctx.send(embed=embed)

        client.close()

async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Birthday(bot))
