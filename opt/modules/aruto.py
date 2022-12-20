import discord

async def func(message):
    res = "飛電或人「" + message.content[5:] + "は人類の夢だ！！」"
    await message.channel.send(file=discord.File('pictures/HidenAruto.jpg'))
    await message.channel.send(res)