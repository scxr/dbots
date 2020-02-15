import discord
from discord.utils import get
from discord.ext import commands

TOKEN = 'TOKEN'
BOT_PREFIX = '~'
client = discord.Client()

bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))


@bot.command()
async def kick(ctx, member: discord.Member = None):
    if not member:
        await ctx.send('Please select a member to kick')
        return
    
    await member.kick()
    await ctx.send('{} was kicked'.format(member.mention))


@bot.command()
async def ban(ctx, member: discord.Member = None):
    if not member:
        await ctx.send('Please specify a member to ban')
        return
    await member.ban()
    await ctx.send('{} was banned'.format(member.mention))


@bot.command()
async def mute(ctx, member: discord.Member = None):

    role = get(ctx.guild.roles, name='Muted')
    if role is None:
        await ctx.send('Please create a Muted role')
        return 
    if not member:
        await ctx.send('PLease specify a member to mute')
        return  
    await member.add_roles(role)
    await ctx.send('{} has been muted'.format(member.mention))


@bot.command
async def unmute(ctx, member: discord.Member = None):
    role = get(ctx.guild.roles, name='Muted')
    if role is None:
        await ctx.send('Please create a Muted role')
        return 
    if not member:
        await ctx.send('PLease specify a member to mute')
        return
    await member.remove_roles(role)
    await ctx.send('{} has been unmuted'.format(member.mention))
bot.run(TOKEN)
