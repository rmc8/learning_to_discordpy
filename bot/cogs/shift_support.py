import os
from pathlib import Path

import pandas as pd
import discord
from discord import app_commands, Interaction, ui
from discord.ui import View, Button
from discord.ext import commands

from . import MY_GUILD_ID


working_dir = Path(__file__).parents[2]
DB_CSV_PATH: str = os.path.join(
    working_dir,
    "input",
    "shift_support.tsv",
)


def get_embed_table(label, df):
    print(label, df)


class ShiftSupportView(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="登録")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="あ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=ShiftSupportView())

    @ui.button(label="編集")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="い", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=ShiftSupportView())


class ShiftSupport(commands.Cog):
    NAME: str = "EffectiveDifficulties"

    def __init__(self, bot, view=None):
        self.bot = bot
        self.view = view

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Successfully loaded : {self.NAME}")

    @app_commands.command(name="shift_support", description="シフト作成・募集のサポート画面を出力します")
    @app_commands.guilds(MY_GUILD_ID)
    async def shift_support(
        self, interaction: Interaction, year: int, month: int, day: int
    ):
        view = ShiftSupportView()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(ShiftSupport(bot))
