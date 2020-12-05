import discord
from discord.ext import commands
import os

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot;

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)#gets ping of the user from the bot and converts it to ms instead of seconds

        if(ping <= 80):
            await ctx.send(f':satellite:```diff\n PONG!\n+ {ping}ms```:satellite_orbital:')
        elif(ping <= 150):
            await ctx.send(f':satellite:```fix\nPONG!\n+ {ping}ms```:satellite_orbital:')
        else:
            await ctx.send(f':satellite:```diff\nPONG!\n- {ping}ms```:satellite_orbital:')

    @commands.command()
    async def ranks(self, ctx):
        await ctx.message.author.send('WIP')
        await ctx.send('I have sent you a dm where the ranks are explained. If you need any other clarification, feel free to ask a PA staff member.')


def setup(bot):
    bot.add_cog(Commands(bot))
