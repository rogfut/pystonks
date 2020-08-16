from telegram.ext import Updater, CommandHandler
import requests
import re
from dotenv import load_dotenv
import os

from ipo_scrape import get_ipo

load_dotenv()

def ipo(bot, update):
    chat_id = update.message.chat_id
    ipo = get_ipo()
    # print(type(ipo))
    # print(ipo)
    text = "<pre>Upcoming IPOs\n\n"
    for row in ipo:
        for i in row:
            text += str(i) + ": " + str(row[i]) + "\n"
    text += "</pre>"
    print(text)
    bot.send_message(chat_id=chat_id, text=text, parse_mode='html')

def main():
    updater = Updater(os.getenv('TELEGRAM_API_KEY'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('ipo', ipo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()