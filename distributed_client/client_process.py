import requests
import time
import numpy as np
from multiprocessing import Process, Queue


def client(queue):
    time.sleep(10)  # Wait for 10 second before making the request
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_exchange_logo": False,
        "include_24hr_vol": True,
        "include_24hr_change": True,
        "include_last_updated_at": True,
    }
    response = requests.get(url, params=params)
    data = response.json()
    btc_price = data["bitcoin"]["usd"]
    queue.put(btc_price)
