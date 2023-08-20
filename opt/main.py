from dotenv import load_dotenv
import os

load_dotenv()

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
from modules import builddivide
from modules import kingkazu
from modules import goroge
from modules import daichi
from modules import keiwa
from modules import soyo
from modules import happiness

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)
guild = None

SERVER_ID = 845573797279957003
NOZAN_BASE_ID = 845573797279957006
FURINKAZAN_ID = 1006761298077417533
BOT_DEV_ID = 875755647063449710

# 起動時に動作する処理
@client.event
async def on_ready():
    print(f'{client.user} ログインしました')
    global guild
    guild = client.get_guild(SERVER_ID)

async def help(message):
    res = "**List of commands:**\n"
    res += "・`:dktn_***`：ストリウスが濁点を付けて返してくれます。\n"
    res += "・`:drm_***`：飛電或人が激推ししてくれます。\n"
    res += "・`:ntr-gif`：「NTRは人類の夢だ！」のシーンか「NTRは人類の敵だ！」のシーンのGIFを送信します。\n"
    res += "・`:shion`：シオンが今幸せかどうかを聞いてくれます。\n"
    res += "・`:makoto`：マコト兄ちゃんが乱入してきます。（複数種類あります）\n"
    res += "・`:kingkazu`：キングカズが激励してくれます。\n"
    res += "・`:demon_***`：デモンズドライバーが悪魔の喋り方で返してくれます。\n"
    res += "・風林火山チャンネルで`「風」「林」「火」「山」のサーバー絵文字`を順番に送信すると風林火山を撃ってくれます。\n"
    res += "・`:heart_[任意の数]`：心臓キャプのガチャを実行します（3連まで）。\n"
    res += "・`:goroge_***`：ゴローゲが糾弾します。\n"
    res += "・`:keiwa_***`：景和が償わせます。50％の確率で創世の女神に償わせます。\n"
    res += "・`:soyo_***`：そよ彦が問い詰めます。\n"
    res += "・`:happiness`：貴方の幸せの数値を可視化します。\n"
    res += "・ビルディバイドのボイスチャンネルに誰かが参加するとリビルドバトルの開始を教えてくれます。\n"

    await message.channel.send(res)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message: discord.Message):
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

    if message.content == ':kingkazu':
        await kingkazu.func(message)

    if message.content.startswith(':demon_'):
        await demon.func(message)

    if message.content.startswith(':heart_'):
        await heart.func(message)

    if message.channel.id == FURINKAZAN_ID or message.channel.id == BOT_DEV_ID:
        await furinkazan.func(message)

    if message.content == ':dice' and message.channel.id == 962019622075396216:
        await builddivide.dice(message)

    if message.content.startswith(':goroge_'):
        await goroge.func(message)

    if message.content.startswith(':keiwa_'):
        await keiwa.func(message)

    if message.content.startswith(':soyo_'):
        await soyo.func(message)

    if message.content == ':happiness':
        await happiness.func(message)

    if message.channel.id == NOZAN_BASE_ID or message.channel.id == BOT_DEV_ID:
        await daichi.func(message, guild)

    if message.content == ':help_bot':
        await help(message)



# ボイスチャンネルのイベント関連処理
@client.event
async def on_voice_state_update(member, before, after):
    if(before.channel == None and after.channel.id == 962018177951350875):
        builddivide.entry()

# Botの起動とDiscordサーバーへの接続
client.run(os.environ.get("DISCORD_TOKEN_TEST"))