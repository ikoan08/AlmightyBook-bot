import discord
import random

async def func(message):
    file_name = f'NTRs/NTR{random.randint(1, 3)}.gif'
    await message.channel.send(file=discord.File(file_name))