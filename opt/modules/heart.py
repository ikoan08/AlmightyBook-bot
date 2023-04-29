import discord
import random
import re


is_accept = True

# 画像を追加する場合はGIMPで縦を150にそろえる
async def func(message):
    global is_accept
    if str.isdecimal(message.content[7:]) and int(message.content[7:]) > 0 and int(message.content[7:]) < 4:
        num = int(message.content[7:])
        if not is_accept:
            await message.channel.send("他の人が心臓抽選中です")
            return

        is_accept = False
        for i in random.sample(range(1, 28), k=num):
                file_name = f'pictures/hearts/heart{i}.jpg'
                await message.channel.send(file=discord.File(file_name))
        is_accept = True
    else:
        await message.channel.send(file=discord.File("pictures/hearts/not_heart.jpg"))