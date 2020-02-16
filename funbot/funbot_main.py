import discord, random
from discord.ext import commands
from discord.utils import get
from jokes import dad_joke, chuck_norris_joke

TOKEN = 'Njc4MTg0NDM5MjQ3MDExODQw.Xkf9_w.FwZos7G2gdBkCaEwGk9XTgWcPis'
BOT_PREFIX = '--'
client = discord.Client()

bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))


@bot.command(pass_context=True)
async def roll(ctx):
    todo = ctx.message.content.split()
    tosend = 0
    for i in range(1,int(todo[1][0])):
        tosend += random.randint(0,6)
    embed=discord.Embed(title="Rolling your dice", description="You roled {} d6's your output total is {}".format(todo[1],tosend) , color=0xecce8b)
    await ctx.message.channel.send(embed=embed)


@bot.command(pass_context=True)
async def choose(ctx):
    tochoose = ctx.message.content.split()

    choice1 = tochoose[1]
    choice2 = tochoose[2]
    choice = random.randint(1,2)
    if choice == 1:
        finalchoice=choice1
    else:
        finalchoice = choice2
    embed = discord.Embed(title="I have made my decision", description="I have chosen {}".format(finalchoice))
    await ctx.message.channel.send(embed=embed) 

@bot.command(pass_context=True)
async def spoiler(ctx):
    text = ctx.message.content.split()
    await ctx.message.delete()
    text = ' '.join(text[1::])
    await ctx.message.channel.send('||{}||'.format(text))


@bot.command(pass_context=True)
async def eightball(ctx):
    ballresponse = [
        'Yes', 'No', 'Take a wild guess...', 'Very doubtful',
        'Sure', 'Without a doubt', 'Most likely', 'Might be possible',
        "You'll be the judge", 'no... (╯°□°）╯︵ ┻━┻', 'no... baka',
        'senpai, pls no ;-;'
    ]
    answer = random.choice(ballresponse)
    question = ' '.join(ctx.message.content.split()[1::])
    await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")


@bot.command(pass_context=True)
async def dadjoke(ctx):
    joke = dad_joke()
    await ctx.message.channel.send('{}'.format(joke))


@bot.command(pass_context=True)
async def chuckjoke(ctx):
    joke = chuck_norris_joke()
    await ctx.message.channel.send('{}'.format(joke))

bot.run(TOKEN)
