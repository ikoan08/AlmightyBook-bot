import discord

async def func(message):
    user_name = message.author.display_name
    await message.channel.send(f'{user_name}君、良い目をしているね。')
    for i in range(1, 4):
        await message.channel.send(file=discord.File(f'pictures/kingkazus/kingkazu{i}.jpg'))