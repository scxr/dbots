import discord, time
from discord.ext import commands, tasks
import asyncio

TOKEN = 'NTIyODg4MTUyNTQ2MDE3Mjkw.Xll6eQ.6hJVzEwJBXc7KrB4TLhZxht4NxQ'
client = discord.Client()
prefix = '~'
bot = commands.Bot(command_prefix=prefix, self_bot=True)
print("""
                        .__   _____                                      
            ______ ____ |  |_/ ____\ _____________  ____   _____   ____  
            /  ___// __ \|  |\   __\  \____ \_  __ \/  _ \ /     \ /  _ \ 
            \___ \\  ___/|  |_|  |    |  |_> >  | \(  <_> )  Y Y  (  <_> )
            /____  >\___  >____/__|    |   __/|__|   \____/|__|_|  /\____/ 
                \/     \/             |__|                      \/        """)

print("Made by Jamie Sin#3499 pm for any queries or problems. Changing my code voids support.   ")
@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")

@bot.command(pass_context=True)
async def selfpromo(ctx):
    
    with open('sell.txt','r') as c:
        r = c.read()
        channels = r.split('\n')
        c.close()
        print(channels)
    with open('stuff/msg.txt','r') as f:
        msg = f.read().split('\n')
        f.close()

    while 1:
        await ctx.message.channel.send('Waiting two hours to send our batch')
        await asyncio.sleep(3600)
        for channel in channels:
            print(channel)
            try:
                chan = bot.get_channel(int(channel))
                print(chan)
                await chan.send('\n'.join(msg))
                print('SENT TO : ' + str(chan))
                await ctx.message.channel.send('Sent to : ' + str(chan))
                await asyncio.sleep(1)
            except Exception as e:
                print(e)
                next
          
        
bot.run(TOKEN, bot=False)
