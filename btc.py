import json
from datetime import date

import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

from os import path

def get_btc_price(url):
    session = HTMLSession()
    r = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find('div', class_="cmc-details-panel-price")
    price = div.find('span').text.strip()
    change = div.find('span', class_="cmc-details-panel-price__price-change").text.strip()
    volume_parent = soup.find('ul', class_="cmc-details-panel-stats")
    volume_li = volume_parent.findAll('li')[1]
    volume = volume_li.find('span').text.strip()
    data = [price, change, volume]
    return data