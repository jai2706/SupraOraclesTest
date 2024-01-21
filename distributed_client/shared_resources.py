from multiprocessing import Queue


def create_queues(num_clients):
    queues = []
    for _ in range(num_clients):
        q = Queue()
        queues.append(q)
    return queues
