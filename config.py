import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN","")
CHAT_ID = os.environ.get("CHAT_ID","")

if not TELEGRAM_TOKEN and CHAT_ID:
    raise Exception("TELEGRAM_TOKEN, CHAT_ID 확인필요")