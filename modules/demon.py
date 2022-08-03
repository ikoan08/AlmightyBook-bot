import discord
from janome.tokenizer import Tokenizer

# 分かち書きに必要な解析器
t = Tokenizer()

async def func(message):
    s = message.content[7:]
    res = "デモンズドライバー「"
    for text in list(t.tokenize(s, wakati=True)):
        res += f'{text}  '
    res = res[0:-2]
    res += "」"

    await message.channel.send(file=discord.File('pictures/DemonsDriver.jpg'))
    await message.channel.send(res)
