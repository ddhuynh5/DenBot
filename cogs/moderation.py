""" moderation.py """

from discord.ext import commands

class Moderation(commands.Cog):
    """ General Server Moderation Cog """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", help="Deletes x amount of messages; to use: !purge x")
    async def purge(self, ctx, amount: int):
        """ Removes a specified number of messages """

        if ctx.author.guild_permissions.manage_messages:

            if amount <= 0:
                await ctx.send("Please provide a valid number of messages to purge.")
                return
            
            # Delete the command message as well
            amount += 1

            try:
                deleted = await ctx.channel.purge(limit=amount)
                await ctx.send(f"Deleted {len(deleted)} message(s) including my message!", delete_after=5)
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
        else:
            await ctx.send("You don't have permissions to do that")
        
async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Moderation(bot))
