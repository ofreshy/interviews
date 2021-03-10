import Queue


def get_slowest_and_50_percentile(num_of_slowest):
    """

    :param num_of_slowest:
    :return:
    """

    # We use a priority Queue for its ability to efficiently evict items with low values
    # We do not expose this queue and run in a single threaded environment,
    # so we safely call full() and len() methods
    pq = Queue.PriorityQueue(maxsize=num_of_slowest)

    def process_times(times):
        running_total = 0
        for n, t in enumerate(times):
            if pq.full():
                pq.get_nowait()
            pq.put(t)
            running_total += t

        mean = 0
        if running_total:
            mean = running_total / (n + 1)
        # Again, running in single thread this is a safe operation
        slowest = [pq.get_nowait() for _ in xrange(pq.qsize())]

        return mean, slowest

    return process_times
