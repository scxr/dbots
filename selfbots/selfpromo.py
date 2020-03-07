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

'''
METHODS
PREPAID 50$ GIFT CARD METHOD : $5
AMAZON REFUND METHOD: $5
AMAZON STORE CARD METHOD:$4
AMAZON GIFT CARD METHOD: $5
STOCKX METHOD: $3
EWHORE METHOD:$2
HOLY BIBLE OF JIGS: $3
AMAZON STORE CARDS
1000-1500: $22.50
8000-9000 : $45
5000-6000 : $40
2000 - 3000 : $35
3000 - 4000 : $37.50
all cards come with a method
SELF BOTS
all self bots are custom made in python
SELF PROMO BOT
desc: tired of spamming your invite link everywhere manually? well paste the channel ids you want to put your invite link in and this bot will do all of the work for you!
cost : $12.50
DISBOARD BOT
desc: send your d!bump message every 2 hours without any manual effort
costL $5
MESSAGE SPAMMER
desc: send messages for you rapidly
cost: $2
ALL OTHER BOTS
I can make pretty much any bot you want, PM me and i will give you a quote on the cost
'''
@bot.command(pass_context=True)
async def selfpromo(ctx):
    myembed = discord.Embed(title='My Services', description='''
                                                                    **__AMAZON STORE CARDS__**\n
                                                                    1000-1500: $22.50\n
                                                                    2000-3000: $35\n
                                                                    3000-4000: $37.50\n
                                                                    5000-6000: $40\n
                                                                    8000-9000: $45\n\n
                                                                    **__SELF BOTS__**\n
                                                                    __SELF PROMO BOT__\n
                                                                    *this is the bot being used to send this message ;)*\n
                                                                    tired of spamming your invite link everywhere manually? well paste the channel ids you want to put your invite link in and this bot will do all of the work for you!\n 
                                                                    cost : $12.50 \n
                                                                    DISBOARD BOT\n
                                                                    desc: send your d!bump message every 2 hours without any manual effort\n
                                                                    cost: $5\n
                                                                    ALL OTHER BOTS\n
                                                                    I can make pretty much any bot you want, PM me and i will give you a quote on the cost
                                                                    ''', colour=0xFF0000)

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
                await chan.send(embed=myembed)
            except ValueError:
                print('We have reached the end of the channels')
        await asyncio.sleep(10)
        print('waiting')
bot.run(TOKEN, bot=False)
