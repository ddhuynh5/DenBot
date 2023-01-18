""" Startup cog """

import random
import discord

from discord.ext import commands


class Startup(commands.Cog):
    """ Bot startup """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        """ on startup """

        print(f"Connected to bot: {self.bot.user.name}")
        print(f"Bot ID: {self.bot.user.id}")

        for guild in self.bot.guilds:
            print(guild)
            print(guild.id)

    @commands.Cog.listener("on_voice_state_update")
    async def on_voice_state_update(self, member, before, after):
        """
            code to mention a user whenever another user joins a voice channel
            in this example, my friend andy will be pinged when I join a channel
            andy_id = 217419100018704384

            Sends a cat picture/GIF when a user leaves the channel
        """
        # ---- Start Notification On Join Region ----

        dennis = 210225328402989056
        andy = 217419100018704384
        chat_channel = 395879704328142849
        channel = self.bot.get_channel(chat_channel)

        if not before.channel and after.channel and member.id == dennis:
            ids = [m.id for m in after.channel.members]

            if andy not in ids:
                await channel.send(f"<@{andy}> get on :smiling_imp:")
                # msg = await channel.send("Would you like to ")
                # await msg.add_reaction('👍')
                # await msg.add_reaction('👎')
            else:
                return

        # ---- End Notification On Join Region ----

        if before.channel is not None and after.channel is None:
            await channel.send(file=discord.File(r"img\cat.gif"))
            await channel.send(f"Goodbye, <@{member.id}>!")

    @commands.Cog.listener("on_message")
    async def on_message(self, message):
        """ code to react to user msg """

        num = random.randint(-500, 500)

        if not message.author.bot:
            if message.content == "pog":
                await message.channel.send("very pog")
            elif message.content == "very pog":
                await message.channel.send("the poggest")

        if message.author.id == 181438247015022592 and 50 <= num <= 100:
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

    @commands.command()
    async def shutdown(self, ctx):
        """ Shuts down the bot """
        dennis = 210225328402989056
        if ctx.message.author.id == dennis:
            print("shutdown")
            try:
                await self.bot.logout()
            except EnvironmentError:
                print("EnvironmentError")
                self.bot.clear()
        else:
            await ctx.send("You do not own this bot!")


async def setup(bot):
    """ Adds cog to bot """

    await bot.add_cog(Startup(bot))
