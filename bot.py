""" Main file where bot starts up """

import os
import asyncio
import random
import discord

from discord.ext import commands
#from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    """ on startup """

    print(f"Connected to bot: {bot.user.name}")
    print(f"Bot ID: {bot.user.id}")

    for guild in bot.guilds:
        print(guild)
        print(guild.id)


@bot.event
async def on_voice_state_update(member, before, after):

    # ---- Start Notification On Join Region ----
    """
        code to mention a user whenever another user joins a voice channel
        in this example, my friend andy will be pinged when I join a channel
        andy_id = 217419100018704384
    """
    dennis = 210225328402989056
    andy = 217419100018704384
    chat_channel = 395879704328142849

    if not before.channel and after.channel and member.id == dennis:
        channel = bot.get_channel(chat_channel)

        ids = [m.id for m in after.channel.members]

        if andy not in ids:
            await channel.send(f"<@{andy}> get on :smiling_imp:")
            # msg = await channel.send("Would you like to ")
            # await msg.add_reaction('👍')
            # await msg.add_reaction('👎')
        else:
            return

    # ---- End Notification On Join Region ----


@bot.event
async def on_message(message):
    """ code to react to user msg """

    num = random.randint(-500, 500)

    if not message.author.bot:
        if message.content == "pog":
            await message.channel.send("very pog")
        elif message.content == "very pog":
            await message.channel.send("the poggest")

    if message.author.id == 181438247015022592 and (num <= 50 and num >= 100):
        await message.delete()
        await message.channel.send(
            embed=discord.Embed(
                title=":smiling_imp:",
                description=message.content
            )
        )

    if (len(message.attachments) > 0 and
        message.author.id == 181438247015022592 and
            50 <= num <= 100):
        await message.channel.send("Nice try silly goose")
        await message.delete()

    await bot.process_commands(message)


async def main():
    """ Main function where bot loads cogs and starts up """

    async with bot:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and "music" not in filename:
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(TOKEN)

asyncio.run(main())
