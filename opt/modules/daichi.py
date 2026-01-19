import random

import discord


async def func(message, guild):
    num = random.randint(1, 500)
    dev_channel = guild.get_channel(875755647063449710)
    await dev_channel.send(num)
    if num in {100, 101}:
        await message.channel.send(file=discord.File("pictures/daichi.jpg"))

    if num in {50, 150}:
        await message.channel.send(file=discord.File("pictures/oioioioi.jpg"))
