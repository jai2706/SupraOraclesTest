from multiprocessing import Process
from client_process import client
from aggregator import aggregator
from shared_resources import create_queues


def main():
    num_clients = 5
    queues = create_queues(num_clients)
    clients = []
    for i in range(num_clients):
        p = Process(target=client, args=(queues[i],))
        clients.append(p)
        p.start()

    agg = Process(target=aggregator, args=(queues, num_clients))
    agg.start()

    for p in clients:
        p.join()

    agg.terminate()
    agg.join()


if __name__ == "__main__":
    main()
