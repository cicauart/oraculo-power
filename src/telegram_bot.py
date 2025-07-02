"""Envío del audio procesado a Telegram."""

from pathlib import Path
from telegram import Bot

TOKEN = "YOUR_TELEGRAM_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


def send_audio(audio: Path) -> None:
    """Envía el archivo de audio final a Telegram."""
    print("[Telegram] Enviando audio...")
    bot = Bot(token=TOKEN)
    with open(audio, "rb") as f:
        bot.send_audio(chat_id=CHAT_ID, audio=f)
    print("[Telegram] Audio enviado")
