import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
f = open("C://Users//carso//Desktop//PA_bot_token.txt", 'r')
token = f.read()

# client = MyClient(intents=intents)
# client.run(token)#runs the bot using the token that was read from the txt file

bot = commands.Bot(intents=intents, command_prefix='$$')

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')

bot.run(token)
