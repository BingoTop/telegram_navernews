from config import TELEGRAM_TOKEN,CHAT_ID
import requests as rq
import telegram


bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(text):
    bot.sendMessage(CHAT_ID,text,parse_mode=telegram.ParseMode.HTML)

# bot = telegram.Bot(token="1284773681:AAG6J9Ubxeyj9zx9whXky3T4_NWubbuwXAI")
# updates= bot.getUpdates()
#
# for msg in updates:
#     print(msg)
