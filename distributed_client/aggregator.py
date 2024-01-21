from multiprocessing import Queue
from typing import List
from multiprocessing import Queue
import numpy as np


def aggregator(queues, num_clients):
    prices = []
    for i in range(num_clients):
        prices.append(queues[i].get())
    average_price = np.mean(prices)
    print(f"Cache complete. The average USD price of BTC is: {average_price}")
