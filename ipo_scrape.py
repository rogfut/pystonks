# inspired by https://github.com/MNafekh/IPOList/blob/master/IPOScraper.py with permission of owner

import json
from datetime import date

import requests
from prettytable import PrettyTable
from requests_html import HTMLSession
from bs4 import BeautifulSoup

from os import path

# helper functions
def save_file(file, path):
    with open(path, 'wb') as f:
        f.write(file)

def open_file(path):
    with open(path, 'rb') as f:
        return f.read()

def get_ipo():
    title = "Upcoming IPOs"

    # parse html content
    def parse(content, title):
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', id="ipoCalendarData")
        table_body = table.find('tbody')
        rows = table_body.findAll('tr')

        # data = [['Date', 'Company', 'Exchange', 'IPO Value', 'IPO Price', 'Last']]
        data = []

        for row in rows:
            cells = row.findAll('td')
            d = dict()
            d['Date']       = cells[0].text.strip()
            d['Company']    = cells[1].text.strip().replace("\n", " ")
            d['Exchange']   = cells[2].text.strip()
            d['IPO Value']  = cells[3].text.strip()
            d['IPO Price']  = cells[4].text.strip()
            d['Last']       = cells[5].text.strip()

            data.append(d)

        return data

    # check for cached data
    if path.exists('./cache/ipo_table'):
        return parse(open_file('/.cache/ipo_table'), title)
    else:
        # scrape
        session = HTMLSession()
        r = session.get('https://www.investing.com/ipo-calendar/', headers={'User-Agent': 'Mozilla/5.0'})

        # cache page
        save_file(r.content, './cache/ipo_table')

        return parse(r.content, title)