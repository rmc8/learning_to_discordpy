import discord
from discord import app_commands, ButtonStyle, Interaction
from discord.ext import commands

from . import MY_GUILD_ID


# Buttons
class YesButton(discord.ui.Button):
    def __init__(
        self, *, style: ButtonStyle = ButtonStyle.secondary, label: str = "yes"
    ):
        super().__init__(style=style, label=label)

    async def callback(self, interaction: Interaction):
        await interaction.response.send_message("Yes")
        await interaction.followup.send("あなたは８９３です...(震)")


class NoButton(discord.ui.Button):
    def __init__(
        self, *, style: ButtonStyle = ButtonStyle.secondary, label: str = "no"
    ):
        super().__init__(style=style, label=label)

    async def callback(self, interaction: Interaction):
        await interaction.response.send_message("No")
        await interaction.edit_original_response.send("あなたはゆるふわです！ゆるふわ～っ")


class YurufuwaTest(commands.Cog):
    NAME: str = "YurufuwaTest"

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Successfully loaded : {self.NAME}")

    @app_commands.command(name="yurufuwa_test", description="ボタンのテストです")
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.checks.has_permissions(administrator=True)
    async def yurufuwa_test(self, interaction: Interaction):
        view = discord.ui.View()
        view.add_item(YesButton(style=discord.ButtonStyle.primary))
        view.add_item(NoButton(style=discord.ButtonStyle.grey))
        await interaction.response.send_message(
            "総合力が36万を超えた編成を持っていますか？",
            view=view,
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(YurufuwaTest(bot))
