import discord
import datetime

# 風が送信された時刻
start = datetime.datetime.now()

# ノーザンベースに入れておくメッセージ履歴
message_content_history = []

#風が最後に送信されてから風林火山が成立したか
is_complete_furinkazan = True

async def func(message):
    message_content_history.append(message.content)
    if len(message_content_history) > 4:
        message_content_history.pop(0)

    global is_complete_furinkazan
    global start
    if is_complete_furinkazan and message.content == "<:like_window:970702189506998302>":
        start = datetime.datetime.now()
        is_complete_furinkazan = False

    if message_content_history == [
        "<:like_window:970702189506998302>",
        "<:like_forest:970702266313101362>",
        "<:like_fire:970702341185609798>",
        "<:like_mountain:970702424060870736>"
    ]:
        is_complete_furinkazan = True
        time = datetime.datetime.now() - start
        await message.channel.send(file=discord.File('pictures/furinkazan.jpg'))
        await message.channel.send(f'タイム {time.seconds}.{time.microseconds} 秒')