import discord
import random

async def dice(message):
    res = random.randint(1, 6)
    await message.channel.send(res)

async def entry():
    channel = client.get_channel(962019622075396216)
    text = f'{member.name} さんがリビルドバトルに参加しました'
    await channel.send(text)