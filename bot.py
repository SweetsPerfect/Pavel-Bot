import datetime
import discord
import os
import re
import typing

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot(
    intents=discord.Intents.all(),
    activity=discord.Game("Grand Theft Auto V"),
)

# コンソールメッセージ用
sysmessage = '["Pavel-Bot".sys]'

# パス
# ボットフォルダー
bot_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(bot_path, "token.txt"), mode="r", encoding="cp932") as bot_token:
    TOKEN = str(bot_token.read())


# 単語定義
# パベル
pavel = ["ぱべる", "パベル", "Pavel", "PAVEL", "pavel"]

# 美味しいヤミー
oisiiyummy = ["美味しいヤミー", "おいしいヤミー", "おいしいやみー", "oisiiyummy", "OISIIYUMMY"]

# メインターゲット
maintarget = {
    1: "ルビーのネックレス",
    2: "ピンク・ダイヤモンド",
    3: "無記名債権",
    4: "シンシミートテキーラ",
}

# メインターゲットの添付画像
mt_imgfolderpath = os.path.join(bot_path, "mt_img")
mt_imgfile = {
    1: "ruby_necklace.png",
    2: "pink_diamond.png",
    3: "bearer_bonds.png",
    4: "sinsimito_tequila.png",
}

# 美味しいヤミーの添付画像
oisiiyummy_file = "oisiiyummy.png"


@bot.event
async def on_ready():
    print(sysmessage, "----------Done dayo!----------")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    # endif

    if message.content in pavel:  # PAVEL呼び
        await message.channel.send("え、呼んだか？")
    # endif

    if message.content in oisiiyummy:  # 美味しいヤミー
        await message.channel.send(file=discord.File(os.path.join(bot_path, oisiiyummy_file)))
        return
    # endif


# /target コマンド
@bot.command(
    name="target",
    description="カヨ・ペリコ強盗のメインターゲット及びサブターゲットのお知らせを行います",
)
async def target(
    ctx: discord.ApplicationContext,
    main: int,
    gold: int,
    art: int,
    money: int,
):
    await ctx.response.send_message(
        content=f"おっ、{ctx.author.mention}がルビオのところに__偵察__しに行ったらしいな？\nそれで...**今回のターゲットはこれだ！**\n\n> メインターゲット\n> 　・__**{maintarget[main]}**__\n> サブターゲット\n> 　・金塊:coin: × **{gold}**\n> 　・絵画:art: × **{art}**\n> 　・現金:dollar: × **{money}**",
        file=discord.File(
            os.path.join(mt_imgfolderpath, mt_imgfile[main]),
            filename="SPOILER_" + mt_imgfile[main],
        ),
    )
    return


bot.run(TOKEN)
