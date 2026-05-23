from sigflow.workers.pool import WorkerPool


def test_worker_pool_maps_items():
    assert WorkerPool(2).map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]


def test_worker_pool_preserves_order_with_varying_times():
    import time

    def slow_if_first(x):
        if x == 0:
            time.sleep(0.1)
        return x

    results = WorkerPool(workers=2).map(slow_if_first, [0, 1, 2])
    assert results == [0, 1, 2]