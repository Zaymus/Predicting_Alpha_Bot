import discord
from welcome import welcome

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'{self.user} is now active')

    async def on_member_join(self, member):
        for message in welcome_message:
            await member.send(message)
