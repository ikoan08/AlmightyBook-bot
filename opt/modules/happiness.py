import discord
import random

async def func(message):
    user_name = message.author.display_name
    score = random.randint(0, 100)
    decimal = random.randint(0, 10)
 
    await message.channel.send(f"{user_name}：Happiness {score}.{decimal}")