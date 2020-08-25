from config import TELEGRAM_TOKEN,CHAT_ID
import telegram

print(TELEGRAM_TOKEN)
bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(text):
    bot.sendMessage(CHAT_ID,text,parse_mode=telegram.ParseMode.HTML)

