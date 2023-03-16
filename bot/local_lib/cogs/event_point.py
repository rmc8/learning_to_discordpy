import itertools
from typing import List

import discord
from discord import app_commands
from discord.ext import commands
from pandas import DataFrame

from .. import MY_GUILD_ID

live_boost_dict: dict[int, int] = {
    0: 1,
    1: 5,
    2: 10,
    3: 15,
    4: 19,
    5: 23,
    6: 26,
    7: 29,
    8: 31,
    9: 33,
    10: 35,
}

SCORE_BASE: int = 20_000
SECTION_LIMIT: int = 126
LIVE_BONUS_LIMIT: int = 11
EVENT_BONUS_LIMIT: int = 386
MUSIC_BASE_POINT: int = 100  # Envy
CALC_RESULTS_TEMPLATE: str = """
```
{res}
```
""".strip()


def calc_event_point(base_point: int, event_bonus: int, score: int) -> int:
    event_bonus_weight: float = (100 + event_bonus) / 100
    score_bonus_f: float = (base_point +
                            (score / SCORE_BASE)) * event_bonus_weight
    return int(score_bonus_f)


def weighting_live_bonus(event_point: int, spend_live_bonus: int) -> int:
    return event_point * live_boost_dict[spend_live_bonus]


def create_event_point_table() -> List[dict]:
    table: List[dict] = []
    section_range = range(SECTION_LIMIT)
    event_bonus_range = range(EVENT_BONUS_LIMIT)
    live_bonus_range = range(LIVE_BONUS_LIMIT)
    range_tuple: tuple = (section_range, event_bonus_range, live_bonus_range)
    for section, event_bonus, live_bonus in itertools.product(*range_tuple):
        score: int = SCORE_BASE * section
        base_event_point: int = calc_event_point(
            MUSIC_BASE_POINT,
            event_bonus,
            score,
        )
        event_point: int = weighting_live_bonus(base_event_point, live_bonus)
        record: dict = {
            "event_bonus": event_bonus,
            "live_bonus": live_bonus,
            "lower_score_limit": score,
            "upper_score_limit": score + (SCORE_BASE - 1),
            "event_point": event_point,
        }
        table.append(record)
    return table


def get_ret_lines(fil_df: DataFrame) -> str:
    columns_label: str = "\t".join(fil_df.columns.tolist())
    lines: List[str] = [columns_label]
    for record in fil_df.to_dict(orient="records")[:16]:
        line_list: list = []
        line_list.append(f"{record['event_bonus']:>3}%")
        line_list.append(f"{record['live_bonus']:>2}")
        line_list.append(f"{record['lower_score_limit']:>7}")
        line_list.append(f"{record['upper_score_limit']:>7}")
        line_list.append(f"{record['event_point']:>5}")
        line: str = "\t".join(line_list)
        lines.append(line)
    return "\n".join(lines)


def sort_df(df: DataFrame) -> DataFrame:
    return df.sort_values(["live_bonus", "event_bonus", "lower_score_limit"])


def calc(num_of_points_wanted: int) -> str:
    event_point_df = DataFrame(create_event_point_table())
    fil_df = event_point_df[event_point_df["event_point"] ==
                            num_of_points_wanted]
    if fil_df.empty:
        return "該当のイベントポイントを獲得する組み合わせが見つかりませんでした。"
    sorted_df = sort_df(fil_df)
    return CALC_RESULTS_TEMPLATE.format(res=get_ret_lines(sorted_df))


class EventPoint(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Successfully loaded : EventPoint")
        await self.bot.tree.sync(guild=discord.Object(MY_GUILD_ID))
        print("sync")

    @app_commands.command(
        name="calc_point",
        description="EventPointの調整用の計算機です",
    )
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.checks.has_permissions(administrator=True)
    async def calc_point(
        self,
        interaction: discord.Interaction,
        tar_point: int,
    ):
        ret = calc(tar_point)
        print(ret)
        await interaction.response.send_message(
            ret,
            ephemeral=True,
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(EventPoint(bot))
