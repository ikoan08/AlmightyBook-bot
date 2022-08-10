import discord
import random
import re

# 画像を追加する場合はGIMPで縦を150にそろえる
async def func(message):
    if str.isdecimal(message.content[7:]):
        num = int(message.content[7:])
        if num < 0 or num > 10:
            await message.channel.send("不正な数です")
            return

        for i in random.sample(range(1, 19), k=num):
                file_name = f'hearts/heart{i}.jpg'
                await message.channel.send(file=discord.File(file_name))