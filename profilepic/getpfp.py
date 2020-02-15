import discord
from discord.utils import get
from discord.ext import commands

TOKEN = 'Njc4MTg0NDM5MjQ3MDExODQw.Xkf9_w.FwZos7G2gdBkCaEwGk9XTgWcPis'
client = discord.Client()
prefix = '~'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'getpfp'):
        user = message.mentions[0]
        pfp = user.avatar_url
        embed=discord.Embed(title="Profile picture", description="This is {}'s profile picture".format(user.mention) , color=0xecce8b)
        embed.set_image(url=(pfp))
        await message.channel.send(embed=embed)

client.run(TOKEN)
