import discord
from discord import app_commands, ButtonStyle, Interaction, ui
from discord.ui import View, Button
from discord.ext import commands

from . import MY_GUILD_ID


class MusicTables(View):
    def __init__(self):
        super().__init__()

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="あ")
    async def a(self, interaction: Interaction, button: Button):
        self.clear_items()
        await interaction.edit_original_response(content="あ", view=MusicTables())

    @ui.button(label="か")
    async def ka(self, interaction: Interaction, button: Button):
        self.clear_items()
        await interaction.edit_original_response(content="か", view=MusicTables())

    @ui.button(label="さ")
    async def sa(self, interaction: Interaction, button: Button):
        self.clear_items()
        await interaction.edit_original_response(content="さ", view=MusicTables())


class EffectiveDifficulties(commands.Cog):
    NAME: str = "EffectiveDifficulties"

    def __init__(self, bot, view=None):
        self.bot = bot
        self.view = view

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Successfully loaded : {self.NAME}")

    @app_commands.command(name="effective_difficulties", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.checks.has_permissions(administrator=True)
    async def effective_difficulties(self, interaction: Interaction):
        view = MusicTables()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(EffectiveDifficulties(bot))
