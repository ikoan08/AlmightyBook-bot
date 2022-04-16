# インストールした discord.py を読み込む
import discord
import wanakana
from discord import channel
from janome.tokenizer import Tokenizer
import random


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODg4NzcwMjAwOTY1NjIzODk4.YUXhwA.fej9-qgAEj9tGfTL_vQnYM5jxgg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 分かち書きに必要な解析器
t = Tokenizer()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# ------- 以下個別処理を行う関数 ----------
async def storiuse(message):
    escape_char = ['.', ',', '!', '?', '|', '。', '、', '…', '・', '？', '！', '「', '」', '『', '』', ' ', '　']
    res = "ストリウス「"
    for c in list(message.content)[6:]:
        res += c
        if not c in escape_char:
            res += "゛"
    res += "」"
    await message.channel.send(file=discord.File('pictures/Sutoriusu.jpg'))
    await message.channel.send(res)

async def aruto(message):
    res = "飛電或人「" + message.content[5:] + "は人類の夢だ！！」"
    await message.channel.send(file=discord.File('pictures/HidenAruto.jpg'))
    await message.channel.send(res)

async def ntr(message):
    file_name = f'NTRs/NTR{random.randint(1, 3)}.gif'
    await message.channel.send(file=discord.File(file_name))

async def shion(message):
    user_name = message.author.display_name
    await message.channel.send(file=discord.File('pictures/Shion.jpg'))
    await message.channel.send(f'{user_name}！今、幸せ？')

async def makoto(message):
    file_name = f'makotoes/makoto{random.randint(1, 11)}.gif'
    await message.channel.send(file=discord.File(file_name))

async def demon(message):
    s = message.content[7:]
    res = "デモンズドライバー「"
    for text in list(t.tokenize(s, wakati=True)):
        res += wanakana.to_katakana(f'{text}    ')
    res = res[0:-4]
    res += "」"

    await message.channel.send(file=discord.File('pictures/DemonsDriver.jpg'))
    await message.channel.send(res)

async def help(message):
    res = "**List of commands:**\n"
    res += "`:dktn_***`：ストリウスが濁点を付けて返してくれます。\n"
    res += "`:drm_***`：飛電或人が激推ししてくれます。\n"
    res += "`:ntr-gif`：「NTRは人類の夢だ！」のシーンか「NTRは人類の敵だ！」のシーンのGIFを送信します。\n"
    res += "`:shion`：シオンが今幸せかどうかを聞いてくれます。\n"
    res += "`:makoto`：マコト兄ちゃんが乱入してきます。（複数種類あります）\n"
    res += "`:demon_***`：デモンズドライバーが悪魔の喋り方で返してくれます。\n"
    res += "ビルディバイドのボイスチャンネルに誰かが参加するとリビルドバトルの開始を教えてくれます。\n"
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

    # シオンが幸せかどうか聞いてくれる処理
    if message.content == ':shion':
        await shion(message)

    # マコト兄ちゃんが乱入してくる処理
    if message.content == ':makoto':
        await makoto(message)

    # デモンズドライバーが喋ってくれる処理
    if message.content.startswith(':demon_'):
        await demon(message)

    if message.content == ':dice' and message.channel.id == 962019622075396216:
        res = random.randint(1, 6)
        await message.channel.send(res)

    if message.content == ':help':
        await help(message)



# ボイスチャンネルのイベント関連処理
@client.event
async def on_voice_state_update(member, before, after):
    if(before.channel == None and after.channel.id == 962018177951350875):
        channel = client.get_channel(962019622075396216)
        res = f'{member.name} さんがリビルドバトルに参加しました'
        await channel.send(res)
        await channel.send(file=discord.File("pictures/makoto_fu_ha.jpg"))
        res = f'フッ！ハッ！{member.name}！どうしてリビルドしない！？'
        await channel.send(res)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)