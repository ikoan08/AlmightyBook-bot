import discord

async def func(message):
    res = "「やっぱり..." + message.content[8:] + "は極悪人だーーーーーっ！！」"
    await message.channel.send(file=discord.File('pictures/goroge.jpg'))
    await message.channel.send(res)