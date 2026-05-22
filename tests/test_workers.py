from sigflow.workers.pool import WorkerPool


def test_worker_pool_maps_items():
    assert sorted(WorkerPool(2).map(lambda x: x + 1, [1, 2, 3])) == [2, 3, 4]
