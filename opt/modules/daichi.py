import discord
import random

async def func(message):
    num = random.randint(1, 500)
    if num == 100:
        await message.channel.send(file=discord.File('pictures/daichi.jpg'))