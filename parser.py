import requests  # для URL запроса
from bs4 import BeautifulSoup
import pandas_datareader as pdr
import datetime
def get_price():
    ETH = 'https://www.gate.io/ru/trade/ETH_USDT'
    headers = {
    'user agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/110.0.0.0 Safari/537.36'}
    html = requests.get(ETH, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    convert = soup.findAll('span', {'class': 'tempCurrFiat'})
    price = (convert[0].text[1:])
    print(price)
get_price()
