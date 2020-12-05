import discord
import os
from MyClient import MyClient

intents = discord.Intents.all()

f = open("C://Users//carso//Desktop//PA_bot_token.txt", 'r')
token = f.read()

client = MyClient(intents=intents, command_prefix='.')
client.run(token)#runs the bot using the token that was read from the txt file
