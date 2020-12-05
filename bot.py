import discord
import os
from MyClient import MyClient

intents = discord.Intents.all()

token = "Nzg0NjA5MDg3Mzk2MzgwNjcz.X8ryJw.aW3S_bCh8JNCCOpv7Ius0i9HeZ8"

client = MyClient(intents=intents, command_prefix='.')
client.run(token)#runs the bot using the token that was read from the txt file
