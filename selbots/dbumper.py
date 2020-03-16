import discord, asyncio
from discord.ext import commands
print("""________ __________ ____ ___  _____ _______________________________ 
        \______ \\______   \    |   \/     \\______   \_   _____/\______   \
        |    |  \|    |  _/    |   /  \ /  \|     ___/|    __)_  |       _/
        |    `   \    |   \    |  /    Y    \    |    |        \ |    |   \
        /_______  /______  /______/\____|__  /____|   /_______  / |____|_  /
                \/       \/                \/                 \/         \/ """)
TOKEN = 'ur token'
client = discord.Client()
prefix = '~'
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print('We have reached alive status !! UWU')

@bot.command(pass_context=True)
async def dbump(ctx):
    try:
        await ctx.message.channel.send('!d bump')
    except:
        pass
    await asyncio.sleep(7200)

bot.run(TOKEN, bot=False)
