import requests
from celery import shared_task
from django.core.cache import cache

from trade.currencies import SOURCE_CURRENCIES, DEST_CURRENCIES
from user.models import Nobitex


@shared_task
def cache_orderbook_task():
    url = 'https://api.nobitex.ir/v2/orderbook/all'
    value = requests.get(url).json()
    cache_key = 'nobitex_orderbook'
    cache.set(cache_key, value)


@shared_task
def _cache_trades_task(market_symbol):
    url = 'https://api.nobitex.ir/v2/trades/' + market_symbol
    value = requests.get(url).json()['trades']
    cache_key = 'nobitex_trades_' + market_symbol
    cache.set(cache_key, value)


@shared_task
def cache_trades_task():
    for source_currency in SOURCE_CURRENCIES:
        source = source_currency[0]
        for dest_currency in DEST_CURRENCIES:
            dest = dest_currency[0]
            market_symbol = Nobitex.get_market_symbol(source, dest)
            _cache_trades_task.delay(market_symbol)
