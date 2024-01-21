import json
import numpy as np
import requests
from utils import get_websocket_data


def run_cache_mode(times):
    # Fetch data from websocket and calculate average price
    price_data, average_price = get_websocket_data(times)
    print(f"Cache complete. The average USD price of BTC is: {average_price}")

    # Save the result to the data directory
    with open("data/price_data.json", "w") as file:
        json.dump(price_data, file)
    with open("data/average_price.txt", "w") as file:
        file.write(f"Average Price: {average_price}\n")
