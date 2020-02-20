from googletrans import Translator
import discord
from discord.ext import commands

TOKEN = <redacted>
client = discord.Client()
prefix = '~'
translator = Translator()
bot = commands.Bot(command_prefix=prefix, self_bot=True)


@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")


@bot.command()
async def translate(ctx):
    totrans = ' '.join(ctx.message.content.split()[1::])
    await ctx.message.delete()
    try:  
        transd = translator.translate(totrans, 'en')
        embed = discord.Embed(title="Translation", description="Translated from: {} \n Translated text: {}".format(transd.src,transd.text))
        await ctx.message.channel.send(embed=embed)
    except Exception as e:
        print(e)



bot.run(TOKEN, bot=False)
