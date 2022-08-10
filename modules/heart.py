import discord
import random
import re


is_accept = True

# 画像を追加する場合はGIMPで縦を150にそろえる
async def func(message):
    global is_accept
    if str.isdecimal(message.content[7:]):
        num = int(message.content[7:])
        if num < 0 or num > 3:
            await message.channel.send("不正な数です")
            return

        if not is_accept:
            await message.channel.send("他の人が心臓抽選中です")
            return

        is_accept = False
        for i in random.sample(range(1, 19), k=num):
                file_name = f'hearts/heart{i}.jpg'
                await message.channel.send(file=discord.File(file_name))
        is_accept = True