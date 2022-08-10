# インストールした discord.py を読み込む
import discord
from discord import channel

# 分割したモジュール
from modules import sutoriuse
from modules import aruto
from modules import ntr
from modules import shion
from modules import makoto
from modules import demon
from modules import furinkazan
from modules import heart

# アクセストークン
TOKEN = 'ODg4NzcwMjAwOTY1NjIzODk4.YUXhwA.fej9-qgAEj9tGfTL_vQnYM5jxgg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


async def help(message):
    res = "**List of commands:**\n"
    res += "・`:dktn_***`：ストリウスが濁点を付けて返してくれます。\n"
    res += "・`:drm_***`：飛電或人が激推ししてくれます。\n"
    res += "・`:ntr-gif`：「NTRは人類の夢だ！」のシーンか「NTRは人類の敵だ！」のシーンのGIFを送信します。\n"
    res += "・`:shion`：シオンが今幸せかどうかを聞いてくれます。\n"
    res += "・`:makoto`：マコト兄ちゃんが乱入してきます。（複数種類あります）\n"
    res += "・`:demon_***`：デモンズドライバーが悪魔の喋り方で返してくれます。\n"
    res += "・ノーザンベースで`「風」「林」「火」「山」のサーバー絵文字`を順番に送信すると風林火山を撃ってくれます。\n"
    res += "・`:heart_[任意の数]`：心臓キャプのガチャを実行します（10連まで）。\n"
    res += "・ビルディバイドのボイスチャンネルに誰かが参加するとリビルドバトルの開始を教えてくれます。\n"
    await message.channel.send(res)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content.startswith(':dktn_'):
        await sutoriuse.func(message)

    if message.content.startswith(':drm_'):
        await aruto.func(message)

    if message.content == ':ntr-gif':
        await ntr.func(message)

    if message.content == ':shion':
        await shion.func(message)

    if message.content == ':makoto':
        await makoto.func(message)

    if message.content.startswith(':demon_'):
        await demon.func(message)

    if message.content.startswith(':heart_'):
        await heart.func(message)

    if message.channel.id == 845573797279957006:
        await furinkazan.func(message)

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