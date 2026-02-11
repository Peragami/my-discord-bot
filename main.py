import discord
from discord import app_commands
from discord.ext import commands
import os
import random

class MyBot(commands.Bot):
    def __init__(self):
        # 標準的な権限（メッセージ読み取り権限なしで動くスラッシュコマンド用）
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        """
        Bot起動時に実行される準備処理
        グローバルコマンドとしてDiscord全体に同期します
        """
        await self.tree.sync()
        print("グローバルコマンドの同期が完了しました")

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# --- スラッシュコマンドの定義 ---

@bot.tree.command(name="hello", description="挨拶を返します")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! スラッシュコマンドが成功したよ！")

@bot.tree.command(name="ping", description="Botの応答速度を確認します")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! 遅延: {latency_ms}ms")

@bot.tree.command(name="echo", description="入力した文字をBotが復唱します")
@app_commands.describe(message="Botに喋らせたい文字")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(f"あなたが言ったこと: {message}")

@bot.tree.command(name="omikuji", description="今日の運勢を占います")
async def omikuji(interaction: discord.Interaction):
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(fortunes)
    await interaction.response.send_message(f"今日のあなたの運勢は… **{result}** です！")

# 実行
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("Error: 'DISCORD_TOKEN' environment variable is not set.")
