import discord
from discord.ext import commands

TOKEN = <redacted>
client = discord.Client()
prefix = '~'
bot = commands.Bot(command_prefix=prefix, self_bot=True)


@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")


@bot.command()
async def embed(ctx):
    splitmsg = ctx.message.content.split('\n')
    try:
        embed = discord.Embed(title=splitmsg[1][6::], description=splitmsg[2][6::])
        await ctx.message.channel.send(embed=embed)
        await ctx.message.delete()
    except IndexError:
        await ctx.message.channel.send("You are using the command wrong, please refer to documentation sent for proper usage")
        await ctx.message.delete()


bot.run(TOKEN, bot=False
