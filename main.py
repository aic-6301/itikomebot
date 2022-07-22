import discord
from discord.ext import tasks, commands
import datetime
import asyncio

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='a!')
bot.remove_command('help')
suimin = 949560203886604293

@bot.event
async def on_ready():
    # datetimeの略
    dt_now = datetime.datetime.now()
    print('ready')
    print(f'いちこめ {dt_now.month}/{dt_now.day}です')
    print(f'いちこめ {dt_now.month}/{dt_now.day}です')
    channel = bot.get_channel(949560203886604293)
    channel2 = bot.get_channel(984807772950519890)
    print(channel)
    print(channel2)
    # 時報開始
    ziholoop.start()
    await bot.change_presence(activity=discord.Game(name=f"0時まで待機中"))

@tasks.loop(seconds=1)
async def ziholoop():
    # datetimeの略
   dt_now = datetime.datetime.now()
    # もし0時だったら
   if int(dt_now.hour) == 0 and int(dt_now.minute) == 00:
        # channelの取得
        channel = bot.get_channel(949560203886604293)
        channel2 = bot.get_channel(984807772950519890)
        print(channel)
        # 送信
        await channel.send(f'いちこめ {dt_now.month}/{dt_now.day}です')
        await channel2.send(f'いちこめ {dt_now.month}/{dt_now.day}です')
        await bot.change_presence(activity=discord.Game(name=f"0時過ぎたぞ")) # ステーサス変更
        await asyncio.sleep(60) # 待つ
        print('0:00だぁ')
       


bot.run('your token is here')
