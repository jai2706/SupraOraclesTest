from signatures import verify_signature


def aggregator_task(queues, public_keys, num_clients):
    prices = []
    for i in range(num_clients):
        price, signature = queues[i].get()
        if verify_signature(public_keys[i], str(price), signature):
            prices.append(price)
        else:
            print("Invalid signature from client", i)
    average_price = sum(prices) / len(prices) if prices else None
    print(f"Aggregated average USD price of BTC is: {average_price}")
