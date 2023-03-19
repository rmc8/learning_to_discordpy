import os
import sys
import asyncio

import discord
from discord.ext import commands


from cogs import MY_GUILD_ID, INITIAL_EXTENSIONS

MY_GUILD = discord.Object(id=MY_GUILD_ID)
intents = discord.Intents.default()
client = discord.Client(intents=intents)
token: str = os.getenv("TestBotPythonDevToken")
if len(sys.argv) > 1:
    token = sys.argv[1]


class MyClient(commands.Bot):
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)


bot = MyClient(intents=intents, command_prefix=".")


async def load_extension():
    print("Load extension")
    for n, cog in enumerate(INITIAL_EXTENSIONS, 1):
        print(f"{n}/{len(INITIAL_EXTENSIONS)}: {n/len(INITIAL_EXTENSIONS)*100:.02f}%")
        await bot.load_extension(cog)


# Events
@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")
    await bot.tree.sync()
    await bot.tree.sync(guild=MY_GUILD)
    print("Sync")


@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")


async def main():
    async with bot:
        await load_extension()
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
