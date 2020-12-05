import discord
import os
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='$$')
f = open("C://Users//carso//Desktop//PA_bot_token.txt", 'r')
token = f.read()

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')

bot.run(token)
