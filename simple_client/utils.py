import requests
import numpy as np
import time


def get_websocket_data(times):
    prices = []
    for _ in range(times):
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bitcoin", "vs_currencies": "usd"},
        )
        if response.status_code == 429:
            print("Rate limit exceeded. Pausing for 60 seconds.")
            time.sleep(60)
            continue
        prices.append(response.json()["bitcoin"]["usd"])
    average_price = np.mean(prices)
    return prices, average_price
