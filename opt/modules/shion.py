import discord

async def func(message):
    user_name = message.author.display_name
    await message.channel.send(file=discord.File('pictures/Shion.jpg'))
    await message.channel.send(f'{user_name}！今、幸せ？')