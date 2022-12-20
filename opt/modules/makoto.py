import discord
import random

async def func(message):
    file_name = f'gifs/makotoes/makoto{random.randint(1, 11)}.gif'
    await message.channel.send(file=discord.File(file_name))