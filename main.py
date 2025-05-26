import discord
import os
import random
import asyncio
from discord.ext import commands
from keep_alive import keep_alive




intents = discord.Intents.default()
prefix = '-'

token = os.getenv("D_TOKEN")

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True,
                   intents=intents)

async def update_presence():
    statuses = [discord.Status.online, discord.Status.idle, discord.Status.dnd]
    while True:
        await bot.change_presence(status=random.choice(statuses))
        await asyncio.sleep(random.randint(1800, 7200))  # Change status every 30-120 minutes



@bot.event
async def on_message(message):
    if message.author.id != bot.user.id:  # Ignore self messages
        await bot.typing()
        await asyncio.sleep(random.randint(2, 5))  # Mimic human response time

keep_alive()
bot.run(token, bot=False)
