import discord
import random

async def func(message):
    res = random.randint(1, 6)
    await message.channel.send(res)