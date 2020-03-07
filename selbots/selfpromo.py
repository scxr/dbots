 import discord, time
from discord.ext import commands, tasks
import asyncio

TOKEN = 'NTIyODg4MTUyNTQ2MDE3Mjkw.Xll6eQ.6hJVzEwJBXc7KrB4TLhZxht4NxQ'
client = discord.Client()
prefix = '~'
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")


@bot.command(pass_context=True)
async def selfpromo(ctx):
    while 1:
        with open('channels.txt','r') as c:
            r = c.read()
            channels = r.split('\n')
            c.close()
            print(channels)
        for channel in channels:
            try:
                chan = bot.get_channel(int(channel))
                print(channel, chan)
                await chan.send('and i oop')
            except ValueError:
                print('We have reached the end of the channels')
        asyncio.sleep(1)
bot.run(TOKEN, bot=False)
