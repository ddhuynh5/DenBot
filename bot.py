""" Main file where bot starts up """

import os
import asyncio
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")

class CustomHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(color=discord.Color.blurple(), description="")

        for page in self.paginator.pages:
            embed.description += page
        
        await destination.send(embed=embed)

class BotOverride(commands.Bot):
    """ Overrides default Bot classes """

    async def process_commands(self, message):

        if message.author.id == 801145557099347968:
            return

        ctx = await self.get_context(message)
        await self.invoke(ctx)

bot = BotOverride(command_prefix="!", intents=discord.Intents.all())
bot.help_command = CustomHelpCommand()

async def main():
    """ Main function where bot loads cogs and starts up """

    async with bot:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'): #and "music" not in filename:
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(TOKEN)

asyncio.run(main())
