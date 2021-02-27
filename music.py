import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('봇이 정상적으로 실행되었습니다')
    print(bot.user.name)
    print('connection was succesful')
    game = discord.Game('접두사 /')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def 따라하기(ctx, *, number):
    await ctx.send(embed = discord.Embed(title = '따라하기', description = number, color = 0x00ff00))

@bot.command()
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("음성채널에 유저가 접속해있지 않습니다")

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 음성채널에 접속해있지 않아요")

@bot.command()
async def URL재생(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

bot.run('ODE1MDg3MDY0OTI3ODMwMDQ3.YDnS-w.gZLgSQnxod-qwu9W8NFB2YiLmh4')