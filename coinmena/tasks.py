import django

from coinmena.alphav import Fetcher
from coinmena.models import CoinPair, Coin, Price
from coinmena.worker import celery_app

django.setup()



@celery_app.task(name="fetch_and_store_alphavantage_data")
def fetch_and_store_alphavantage_data(base, pair):
    base = Coin.objects.get(symbol=base)
    pair = Coin.objects.get(symbol=pair)

    coin_pair = CoinPair.objects.get(base=base, pair=pair)
    data = Fetcher().get_exchange(base.symbol, pair.symbol)
    Price.objects.create(pair=coin_pair, price=data)


@celery_app.task(name="fetch_all_coin_pairs")
def fetch_all_coin_pairs():
    for cp in CoinPair.objects.all():
        fetch_and_store_alphavantage_data.apply_async(args=(cp.base.symbol, cp.pair.symbol))
