import discord
import random

async def func(message, guild):
    num = random.randint(1, 500)
    dev_channel = guild.get_channel(875755647063449710)
    await dev_channel.send(num)
    if num == 100 or num == 101 or num == 102 or num == 103 or num == 104:
        await message.channel.send(file=discord.File('pictures/daichi.jpg'))

    if num == 50 or num == 150:
        await message.channel.send(file=discord.File('pictures/oioioioi.jpg'))