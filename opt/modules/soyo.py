import discord

async def func(message):
    msg = message.content[6:]
    res = f"「なんで『{msg}』やったの！？」"

    await message.channel.send(file=discord.File('pictures/soyo.jpg'))
    await message.channel.send(res)