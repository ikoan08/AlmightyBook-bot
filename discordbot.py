# インストールした discord.py を読み込む
import discord
from discord import channel

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODg4NzcwMjAwOTY1NjIzODk4.YUXhwA.fej9-qgAEj9tGfTL_vQnYM5jxgg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

async def storiuse(message):
    escape_char = ['.', ',', '!', '?', '|', '。', '、', '…', '・', '？', '！', '「', '」', '『', '』']
    res = "ストリウス「"
    for c in list(message.content)[6:]:
        res += c
        if not c in escape_char:
            res += "゛"
    res += "」"
    await message.channel.send(file=discord.File('Sutoriusu.jpg'))
    await message.channel.send(res)

async def aruto(message):
    res = "飛電或人「" + message.content[5:] + "は人類の夢だ！！」"
    await message.channel.send(file=discord.File('HidenAruto.jpg'))
    await message.channel.send(res)

async def ntr(message):
    await message.channel.send(file=discord.File('NTR.gif'))

async def help(message):
    res = "**List of commands:**\n `:dktn_***`：ストリウスが濁点を付けて返してくれます。\n `:drm_***`：飛電或人が激推ししてくれます。\n `:ntr-gif`：「NTRは人類の夢だ！」のシーンのGIFを送信します。\n"

    await message.channel.send(res)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # ストリウスが濁点をつける処理
    if message.content.startswith(':dktn_'):
            await storiuse(message)

    if message.content.startswith(':drm_'):
        await aruto(message)

    # NTRは人類の夢だ！のGIFを送信する処理
    if message.content == ':ntr-gif':
        await ntr(message)

    if message.content == ':help':
        await help(message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)