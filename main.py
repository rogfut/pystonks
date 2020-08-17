from telegram.ext import Updater, CommandHandler
import requests
import re
from dotenv import load_dotenv
import os

from ipo_scrape import get_ipo
from crypto_price_scrape import crypto_price

load_dotenv()

# emojis
backhand_index_pointing_right = u'\U0001F449'

def ipo(bot, update):
    chat_id = update.message.chat_id
    ipo = get_ipo()
    text = "<pre>Upcoming IPOs\n\n"
    for row in ipo:
        for i in row:
            text += str(i) + ": " + str(row[i]) + "\n"
    text += "</pre>"
    print(text)
    bot.send_message(chat_id=chat_id, text=text, parse_mode='html')

def btc(bot, update):
    chat_id = update.message.chat_id
    btc_data = crypto_price(os.environ['BTC_PRICE_URL'])
    text = "BTC:  " + btc_data[0] + "\nChange:  " + btc_data[1] + "\nVol(24h):  " + btc_data[2] + "\n\nFollow" + backhand_index_pointing_right + "[@rogut](https://github.com/rogfut)"
    bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview='true', parse_mode='markdown')

def eth(bot, update):
    chat_id = update.message.chat_id
    btc_data = crypto_price(os.environ['ETH_PRICE_URL'])
    text = "ETH:  " + btc_data[0] + "\nChange:  " + btc_data[1] + "\nVol(24h):  " + btc_data[2] + "\n\nFollow" + backhand_index_pointing_right + "[@rogut](https://github.com/rogfut)"
    bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview='true', parse_mode='markdown')

def link(bot, update):
    chat_id = update.message.chat_id
    btc_data = crypto_price(os.environ['LINK_PRICE_URL'])
    text = "LINK:  " + btc_data[0] + "\nChange:  " + btc_data[1] + "\nVol(24h):  " + btc_data[2] + "\n\nFollow" + backhand_index_pointing_right + "[@rogut](https://github.com/rogfut)"
    bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview='true', parse_mode='markdown')

def rvn(bot, update):
    chat_id = update.message.chat_id
    btc_data = crypto_price(os.environ['RVN_PRICE_URL'])
    text = "RVN:  " + btc_data[0] + "\nChange:  " + btc_data[1] + "\nVol(24h):  " + btc_data[2] + "\n\nFollow" + backhand_index_pointing_right + "[@rogut](https://github.com/rogfut)"
    bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview='true', parse_mode='markdown')

def xmr(bot, update):
    chat_id = update.message.chat_id
    btc_data = crypto_price(os.environ['XMR_PRICE_URL'])
    text = "XMR:  " + btc_data[0] + "\nChange:  " + btc_data[1] + "\nVol(24h):  " + btc_data[2] + "\n\nFollow" + backhand_index_pointing_right + "[@rogut](https://github.com/rogfut)"
    bot.send_message(chat_id=chat_id, text=text, disable_web_page_preview='true', parse_mode='markdown')

def main():
    updater = Updater(os.environ['TELEGRAM_API_KEY'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('ipo', ipo))
    dp.add_handler(CommandHandler('btc', btc))
    dp.add_handler(CommandHandler('eth', eth))
    dp.add_handler(CommandHandler('link', link))
    dp.add_handler(CommandHandler('rvn', rvn))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()