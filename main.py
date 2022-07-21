import os
import discord
from discord.ext import tasks, commands
import datetime
import asyncio
from dotenv import load_dotenv

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='a!')
bot.remove_command('help')
suimin = 949560203886604293
load_dotenv()
token = os.environ['token']
@bot.event
async def on_ready():
    print('ready')
    channel = bot.get_channel(949560203886604293)
    channel2 = bot.get_channel(984807772950519890)
    print(channel)
    print(channel2)
    ziholoop.start()
    await bot.change_presence(activity=discord.Game(name=f"0時まで待機中"))

@tasks.loop(seconds=1)
async def ziholoop():
   dt_now = datetime.datetime.now()
   if int(dt_now.hour) == 0 and int(dt_now.minute) == 00:
        channel = bot.get_channel(949560203886604293)
        channel2 = bot.get_channel(984807772950519890)
        print(channel)
        await channel.send(f'いちこめ {dt_now.month}/{dt_now.date}です')
        await channel2.send(f'いちこめ {dt_now.month}/{dt_now.date}です')
        await bot.change_presence(activity=discord.Game(name=f"0時過ぎたぞ"))
        await asyncio.sleep(60)
bot.run(token)
