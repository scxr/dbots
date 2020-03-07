import discord, time
from discord.ext import commands, tasks
import asyncio

TOKEN = 'TOKEN'
client = discord.Client()
prefix = '~'
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")

@bot.command(pass_context=True)
async def selfpromo(ctx):
    myembed = discord.Embed(title='My Services', description='''Msg to send ''', footer='Made by Jamie Sin#3499',colour=0xFF0000)
    while 1:
        with open('channels.txt','r') as c:
            r = c.read()
            channels = r.split('\n')
            c.close()
            print(channels)
        await asyncio.sleep(3600)
        print('waiting')
        for channel in channels:
            try:
                chan = bot.get_channel(int(channel))
                print('SENT TO : ' + str(chan))
                await chan.send(embed=myembed)
                await asyncio.sleep(1)
            except Exception:
                print('We have an error')
                next
        
bot.run(TOKEN, bot=False)
