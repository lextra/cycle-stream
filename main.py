import os
import random
import asyncio
import json
import colorama
import discord
from colorama import Fore
from discord.ext import commands
from discord.utils import get
import requests

import keep_alive

with open('config.json') as f:
    config = json.load(f)
    token = os.getenv('TOKEN')

bot = commands.Bot('.', description='hill', self_bot=True)


def clear():
    os.system('cls')


clear()

def init():
    token = os.getenv("TOKEN")
    try:
        bot.run(token, bot=False, reconnect=True)
        os.system('title (Activity Statuses)')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


async def ready():
    await bot.wait_until_ready()

    statuses = ["᲼᲼", "x"] # change these lol.

    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Streaming(name=status, url="https://www.twitch.tv/oversocialized")) # it can be either twitch or yt.

        await asyncio.sleep(1)


bot.loop.create_task(ready())

keep_alive.keep_alive()

if __name__ == '__main__':
    init()
