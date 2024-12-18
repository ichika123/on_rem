import discord
import os
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


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd)
    print(f'Onliner installed in ' + bot.user.name)

keep_alive()
bot.run(token, bot=False)
