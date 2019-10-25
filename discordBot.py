import discord
import youtube
import setting
import connect_pg
import os

DISCORD_TOKEN =os.environ.get('DISCORD_TOKEN') 
DISCORD_CHANNEL_ID = os.environ.get('DISCORD_CHANNEL_ID') 
DATABASE_URL = os.environ.get('DATABASE_URL')
YT_CHANNEL_ID = os.environ.get('YT_CHANNEL_ID')

client = discord.Client()

@client.event
async def on_ready():
    # print('Logged in as')
    # print(client.user.name)
    # print(client.user.id)
    # print('------')
    channel = client.get_channel(int(DISCORD_CHANNEL_ID))
    try:
        # await channel.send("起動しました")
        clip_id = youtube.get_clip_id(YT_CHANNEL_ID)
        if not connect_pg.select(clip_id): # clip_idがdbに登録されていなかったら
            connect_pg.insert(clip_id) #dbに書き込み

            await channel.send("Marimo NIghtcoreより\n" + youtube.search_pic_url(clip_id))
        else:
            print("Picture already posted.")
    except:
        await channel.send("画像の取得に失敗しました")

    await client.logout()
    await sys.exit()


@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

#ループ処理実行
# loop.start()
# client.loop.create_task(my_background_task())


# Botの起動とDiscordサーバーへの接続
client.run(DISCORD_TOKEN)


   