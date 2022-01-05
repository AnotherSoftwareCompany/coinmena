"""
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)
"""
import requests
from django.conf import settings


class Fetcher:
    def __init__(self):
        self.session = requests.Session()
        self.token = settings.ALPHAVANTAGE_API_KEY
        self.host = 'https://www.alphavantage.co'


    def get_exchange(self, from_symbol: str, to_symbol: str):
        response = self.session.get(f'{self.host}/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_symbol}&'
                                    f'to_currency={to_symbol}&apikey={self.token}')
        response.raise_for_status()
        data = response.json()
        return data['Realtime Currency Exchange Rate']['5. Exchange Rate']

