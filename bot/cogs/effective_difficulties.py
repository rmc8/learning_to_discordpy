import gc
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
    "EffectiveDifficultiesForBot - dl.csv",
)


def get_embed_table(label: str, df):
    fil_df = df[df["label"] == label]
    embed = discord.Embed(
        title=f"曲名が「{label}」からはじまる曲の効率表",
        color=discord.Colour.from_rgb(114, 137, 218),
    )
    embed.add_field(
        name="Title",
        value="\n".join(list(fil_df.title)),
        inline=True,
    )
    embed.add_field(
        name="Score",
        value="\n".join(list(fil_df.score)),
        inline=True,
    )
    embed.add_field(
        name="Event",
        value="\n".join(list(fil_df.event)),
        inline=True,
    )
    return embed


class MusicTablesA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="あ")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="あ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesA())

    @ui.button(label="い")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="い", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesA())

    @ui.button(label="う")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="う", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesA())

    @ui.button(label="え")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="え", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesA())

    @ui.button(label="お")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="お", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesA())


class MusicTablesKA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="か")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="か", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesKA())

    @ui.button(label="き")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="き", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesKA())

    @ui.button(label="く")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="く", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesKA())

    @ui.button(label="け")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="け", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesKA())

    @ui.button(label="こ")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="こ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesKA())


class MusicTablesSA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="さ")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="さ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesSA())

    @ui.button(label="し")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="し", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesSA())

    @ui.button(label="す")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="す", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesSA())

    @ui.button(label="せ")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="せ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesSA())

    @ui.button(label="そ")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="そ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesSA())


class MusicTablesTA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="た")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="た", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesTA())

    @ui.button(label="ち")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ち", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesTA())

    @ui.button(label="つ")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="つ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesTA())

    @ui.button(label="て")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="て", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesTA())

    @ui.button(label="と")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="と", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesTA())


class MusicTablesNA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="な")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="な", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesNA())

    @ui.button(label="に")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="に", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesNA())

    @ui.button(label="ぬ")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ぬ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesNA())

    @ui.button(label="ね")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ね", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesNA())

    @ui.button(label="の")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="の", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesNA())


class MusicTablesHA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="は")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="は", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesHA())

    @ui.button(label="ひ")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ひ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesHA())

    @ui.button(label="ふ")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ふ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesHA())

    @ui.button(label="へ")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="へ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesHA())

    @ui.button(label="ほ")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ほ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesHA())


class MusicTablesMA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="ま")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ま", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesMA())

    @ui.button(label="み")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="み", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesMA())

    @ui.button(label="む")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="む", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesMA())

    @ui.button(label="め")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="め", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesMA())

    @ui.button(label="も")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="も", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesMA())


class MusicTablesYA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="や")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="や", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesYA())

    @ui.button(label="ゆ")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ゆ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesYA())

    @ui.button(label="よ")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="よ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesYA())


class MusicTablesRA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="ら")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ら", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesRA())

    @ui.button(label="り")
    async def i(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="り", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesRA())

    @ui.button(label="る")
    async def u(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="る", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesRA())

    @ui.button(label="れ")
    async def e(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="れ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesRA())

    @ui.button(label="ろ")
    async def o(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="ろ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesRA())


class MusicTablesWA(View):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv(DB_CSV_PATH)

    async def on_error(self, interaction, error, item):
        print(error)

    @ui.button(label="わ")
    async def a(self, interaction: Interaction, button: Button):
        embed = get_embed_table(label="わ", df=self.df)
        self.clear_items()
        await interaction.response.edit_message(view=self)
        await interaction.edit_original_response(embed=embed, view=MusicTablesWA())


class EffectiveDifficulties(commands.Cog):
    NAME: str = "EffectiveDifficulties"

    def __init__(self, bot, view=None):
        self.bot = bot
        self.view = view

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Successfully loaded : {self.NAME}")

    @app_commands.command(name="effective_difficulties_a", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_a(self, interaction: Interaction):
        view = MusicTablesA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_ka", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_ka(self, interaction: Interaction):
        view = MusicTablesKA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_sa", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_sa(self, interaction: Interaction):
        view = MusicTablesSA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_ta", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_ta(self, interaction: Interaction):
        view = MusicTablesTA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_na", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_na(self, interaction: Interaction):
        view = MusicTablesNA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_ha", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_ha(self, interaction: Interaction):
        view = MusicTablesHA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_ma", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_ma(self, interaction: Interaction):
        view = MusicTablesMA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_ya", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_ya(self, interaction: Interaction):
        view = MusicTablesYA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )

    @app_commands.command(name="effective_difficulties_wa", description="効率難易度の表を表示します")
    @app_commands.guilds(MY_GUILD_ID)
    async def effective_difficulties_wa(self, interaction: Interaction):
        view = MusicTablesWA()
        await interaction.response.send_message(
            content="ボタンを押すと効率難易度が表示されます",
            view=view,
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(EffectiveDifficulties(bot))
