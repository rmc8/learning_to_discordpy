import discord
from discord import app_commands
from discord.ext import commands

from . import MY_GUILD_ID


class SelfIntroductionModal(
        discord.ui.Modal,
        title="Questionnaire Response",
):
    name = discord.ui.TextInput(label="名前")
    self_intr = discord.ui.TextInput(
        label="自己紹介",
        style=discord.TextStyle.paragraph,
    )

    async def on_submit(
        self,
        interaction: discord.Interaction,
    ):
        lines: list = [
            f"{self.name}さん、",
            "自己紹介ありがとうございます！"
            "",
            "",
            "【自己紹介】",
            f"{self.self_intr}",
        ]
        await interaction.response.send_message(
            "\n".join(lines),
            ephemeral=True,
        )


class ModalTest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Successfully loaded : PostForum")
        await self.bot.tree.sync(guild=discord.Object(MY_GUILD_ID))
        print("sync")

    @app_commands.command(name="modal_test", description="モーダルのテストです")
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.checks.has_permissions(administrator=True)
    async def modal_test(self, interaction: discord.Interaction):
        modal = SelfIntroductionModal()
        await interaction.response.send_modal(modal)


async def setup(bot: commands.Bot):
    await bot.add_cog(ModalTest(bot))
