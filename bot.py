import os
import requests
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TEXT = (
    "‼️Напоминание‼️\n"
    "‼️Не забудь заполнить тайминги‼️\n\n"
    "📋 Форма для заполнения:\n"
    "💻 Web: <a href='https://docs.google.com/forms/d/e/1FAIpQLSd6_bfaZ796YTEjf8rwmseQ8QZe05ZDQxI4KFHgTsWqoKFcmg/viewform'>ссылка</a>\n"
    "📱 Mobile: <a href='https://docs.google.com/forms/d/e/1FAIpQLSd_4mgsQa3pQi2wzuuOhU7y7XbzL1ruGNnfna4tYWL3AVSEpQ/viewform'>ссылка</a>\n\n"
    "🔍 <a href='https://docs.google.com/spreadsheets/d/1VM8PoYVnGRnCutLV7nvMJ9U1qT8G5d4Y8M-sMjopmCA/edit?gid=1788470692#gid=1788470692'>Просмотр таймингов</a>"
)

if datetime.utcnow().weekday() != 6:
    r = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": TEXT,
            "parse_mode": "HTML",
        },
        timeout=10,
    )
    print(f"Telegram status: {r.status_code}")