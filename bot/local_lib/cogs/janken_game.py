import random

import discord
from discord import app_commands
from discord.ext import commands
from pandas import DataFrame

from .. import MY_GUILD_ID

hands: list = "グー,チョキ,パー".split(",")

judge_dict: dict = {
    "グー": {
        "グー": "あいこ",
        "チョキ": "勝ち",
        "パー": "負け",
    },
    "チョキ": {
        "グー": "負け",
        "チョキー": "あいこ",
        "パー": "勝ち",
    },
    "パー": {
        "グー": "勝ち",
        "チョキ": "負け",
        "パー": "あいこ",
    }
}


def choice() -> str:
    return random.choice(hands)


def judgment(me) -> str:
    judge = judge_dict.get(me)
    if judge is None:
        return "無効試合"
    rival = choice()
    w_l = judge[rival]
    return f"勝敗: {w_l}, 自分: {me}, 相手: {rival}"


class Janken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Successfully loaded : EventPoint")
        await self.bot.tree.sync(guild=discord.Object(MY_GUILD_ID))
        print("sync")

    @app_commands.command(name="janken", description="じゃんけんができます")
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.checks.has_permissions(administrator=True)
    async def calc_point(self, interaction: discord.Interaction, hands: str):
        ret = judgment(hands)
        print(ret)
        await interaction.response.send_message(ret, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Janken(bot))
