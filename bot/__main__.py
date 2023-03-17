import os
import sys
import asyncio

import discord
from discord.ext import commands

from cogs import MY_GUILD_ID, INITIAL_EXTENSIONS

MY_GUILD = discord.Object(id=MY_GUILD_ID)
intents = discord.Intents.default()
client = discord.Client(intents=intents)


class MyClient(commands.Bot):

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


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


async def main():
    token: str = os.getenv("TestBotPythonDevToken")
    if len(sys.argv) > 1:
        token = sys.argv[1]
    async with bot:
        await load_extension()
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
