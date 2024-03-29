import discord
from discord import app_commands, Interaction, Member
from discord.ext import commands

from . import MY_GUILD_ID


class ContextTest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Successfully loaded : ContextTest")
        await self.bot.tree.sync(guild=discord.Object(MY_GUILD_ID))
        print("sync")

    @app_commands.command(name="context_test", description="ボタンのテストです")
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.checks.has_permissions(administrator=True)
    async def greeting(self, interaction: Interaction, member: Member):
        await interaction.response.send_message(f"this is {member.nick} !")


async def setup(bot: commands.Bot):
    await bot.add_cog(ContextTest(bot))
