import discord
import random

async def func(message):
    msg = message.content[7:]
    res = ""
    if random.randint(1, 2) == 1:
        res = f"{msg}に償わせる!!!!!!!!!!!!!!!!!"
    else:
        res = "創世の女神に償わせる!!!!!!!!!!!!!!!!!!!!!!"

    await message.channel.send(file=discord.File('pictures/keiwa.jpg'))
    await message.channel.send(res)