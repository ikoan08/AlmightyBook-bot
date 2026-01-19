import discord


async def func(message):
    escape_char = [".", ",", "!", "?", "|", "。", "、", "…", "・", "？", "！", "「", "」", "『", "』", " ", "　"]
    res = "ストリウス「"
    for c in list(message.content)[6:]:
        res += c
        if c not in escape_char:
            res += "゛"
    res += "」"
    await message.channel.send(file=discord.File("pictures/Sutoriusu.jpg"))
    await message.channel.send(res)
