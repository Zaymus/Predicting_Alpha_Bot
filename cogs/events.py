import discord
from discord.ext import commands

message = """
__***Welcome to the Predicting Alpha Virtual Trading Floor (VTF).***__

The VTF represents a world of potential colleagues and collaborators. Ask questions, share insight, receive feedback on your ideas and network with the best traders from around the world.

```fix\nVALIDATE YOUR MEMBERSHIP:  Send @SeanPA a message with your full name. He will assign you a community rank, unlocking all the chatrooms for you.```
```Community Rules & Guidelines
1) Nicknames: Pick a professional name/alias that you want to be called by.
2) Use the different channels for their intended purposes.
3) Analysis and claims must be accompanied by data and reasoning.
4) Posts are subject to review and may be removed at the discretion of Predicting Alpha Staff.
5) All Predicting Alpha and trade related information is CONFIDENTIAL and not to be shared with anyone outside of the VTF.```
Be sure to #introduce-yourself to the community, and we look forward to your participation in the strongest trading network.

Want to learn more about how to use the VTF? Watch this video: https://www.youtube.com/watch?v=3DmrWVgbpok&feature=youtu.be&list=PLkPHxWteEIybbId3NFNTDhV-YwE5Y27Pj
"""

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot;

    @commands.Cog.listener()
    async def on_connect(self):
        print("Connection to Discord established!")

    @commands.Cog.listener()
    async def on_disconnect(self):
        print("Connection to Discord terminated.")

    @commands.Cog.listener()
    async def on_ready(self):
        print('PA Bot is active and ready for use!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(message)

def setup(bot):
    bot.add_cog(Events(bot))
