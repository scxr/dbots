import discord, youtube_dl, os
from discord.ext import commands
from discord.utils import get

TOKEN = 'TOKEN'
BOT_PREFIX = '~'


bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))


@bot.command(pass_context=True, aliases=['J', 'joi'])
async def join(ctx):
    global voice 
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print("The bot has joined {} ".format(channel))

    await ctx.send("Joined {}".format(channel))


@bot.command(pass_context=True, aliases=['L', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        print("The bot has left {}".format(channel))
        await ctx.send("Left {}".format(channel))
    else:
        await ctx.send('Bot not in a channel')


@bot.command(pass_context=True, aliases=['p','pla'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:        
            os.remove("song.mp3")
            print("Removed all song")
    except PermissionError:
        print('Trying to delete song file however currently in use')
        await ctx.send("Error: Song already playing")
        return

    await ctx.send("Getting everything ready")

    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        print('Downloading audio now')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print('renamed file {}'.format(file))
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("{} has finished playing".format(name)))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.2

    newname = name.rsplit("-",2)
    await ctx.send("Playing: {}".format(newname))
    print("Playing")
bot.run(TOKEN) 
