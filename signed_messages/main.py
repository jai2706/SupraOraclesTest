import sys
from multiprocessing import Process, Queue
from client_signed import client_task
from aggregator_signed import aggregator_task
from signatures import generate_keys


def main():
    num_clients = 5
    queues = [Queue() for _ in range(num_clients)]
    keys = [generate_keys() for _ in range(num_clients)]
    public_keys = [key[1] for key in keys]

    clients = [
        Process(target=client_task, args=(keys[i][0], queues[i]))
        for i in range(num_clients)
    ]
    for client in clients:
        client.start()

    aggregator = Process(
        target=aggregator_task, args=(queues, public_keys, num_clients)
    )
    aggregator.start()

    for client in clients:
        client.join()

    aggregator.join()


if __name__ == "__main__":
    main()
