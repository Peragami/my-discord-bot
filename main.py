import discord
from discord import app_commands
import os

# 権限の設定
intents = discord.Intents.default()
client = discord.Client(intents=intents)
# スラッシュコマンド用のツリーを作成
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    # スラッシュコマンドをDiscordに登録（同期）する
    await tree.sync()
    print(f'ログイン成功！スラッシュコマンド同期完了: {client.user}')

# /hello コマンドの定義
@tree.command(name="hello", description="挨拶を返します")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! スラッシュコマンドが成功したよ！")

client.run(os.getenv('DISCORD_TOKEN'))
