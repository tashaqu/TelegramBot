import requests
import json
from config import keys

class APIException(Exception):
    pass
class MoneyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):


        if quote == base:
            raise APIException(f'Не удалось перевести одинаковые валюты {base}.')
        if float(amount)<0:
            raise APIException(f'Количество меньше нуля {amount}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[base_ticker]) * float(amount)
        return total_base