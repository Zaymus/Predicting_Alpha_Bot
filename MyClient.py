import discord
from welcome import welcome

class MyClient(discord.Client):

    async def on_connect(self):
        print("Connection to Discord established!")

    async def on_disconnect(self):
        print("Connection to Discord terminated.")

    async def on_ready(self):
        print(f'{self.user} is now active and ready for use!')


    async def on_member_join(self, member):
        await member.send(welcome.message)
