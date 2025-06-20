import os
import discord
from discord.ext import commands
import fitz  # PyMuPDF
from analisador import analisar_pdf

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "cenário institucional")
BOT_NAME = os.getenv("BOT_NAME", "Viés EURUSD Bot")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{BOT_NAME} conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.name != CHANNEL_NAME or message.author == bot.user:
        return

    for attachment in message.attachments:
        if attachment.filename.endswith(".pdf"):
            filepath = f"/tmp/{attachment.filename}"
            await attachment.save(filepath)

            texto_extraido = analisar_pdf(filepath)
            await message.channel.send(f"📊 Análise Institucional:\n\n{texto_extraido}")

bot.run(DISCORD_TOKEN)
