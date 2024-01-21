import requests
import json
from signatures import sign_data


def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
    }
    response = requests.get(url, params=params)
    data = response.json()
    btc_price = data["bitcoin"]["usd"]
    return btc_price


def client_task(private_key, queue):
    price = fetch_btc_price()
    signature = sign_data(private_key, str(price))
    queue.put((price, signature))
