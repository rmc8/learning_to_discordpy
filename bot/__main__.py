import os
import asyncio

import discord
from discord.ext import commands
from discord import Interaction, Member, ButtonStyle

from local_lib import MY_GUILD_ID
from local_lib.cog import INITIAL_EXTENSIONS

MY_GUILD = discord.Object(id=MY_GUILD_ID)
intents = discord.Intents.default()
client = discord.Client(intents=intents)


class MyClient(commands.Bot):

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


token = os.getenv("TestBotPythonDevToken")
bot = MyClient(intents=intents, command_prefix=".")


async def load_extension():
    for cog in INITIAL_EXTENSIONS:
        await bot.load_extension(cog)


# Events
@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")


@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")


# Contexts
@bot.tree.context_menu()
async def greeting(interaction: Interaction, member: Member):
    await interaction.response.send_message(f"this is {member.nick} !")


# Buttons
class YesButton(discord.ui.Button):

    def __init__(self,
                 *,
                 style: ButtonStyle = ButtonStyle.secondary,
                 label: str = "yes"):
        super().__init__(style=style, label=label)

    async def callback(self, interaction: Interaction):
        await interaction.response.send_message("Yes")
        await interaction.followup.send("あなたは８９３です...(震)")


class NoButton(discord.ui.Button):

    def __init__(self,
                 *,
                 style: ButtonStyle = ButtonStyle.secondary,
                 label: str = "no"):
        super().__init__(style=style, label=label)

    async def callback(self, interaction: Interaction):
        await interaction.response.send_message("No")
        await interaction.followup.send("あなたはゆるふわです！ゆるふわ～っ")


@bot.tree.command()
async def yurufuwa_test(interaction: Interaction):
    view = discord.ui.View()
    view.add_item(YesButton(style=discord.ButtonStyle.primary))
    view.add_item(NoButton(style=discord.ButtonStyle.grey))

    await interaction.response.send_message(
        "総合力が36万を超えた編成を持っていますか？",
        view=view,
    )


async def main():
    token: str = os.getenv("TestBotPythonDevToken")
    async with bot:
        await load_extension()
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
