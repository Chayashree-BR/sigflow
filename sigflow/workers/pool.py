from concurrent.futures import ThreadPoolExecutor, as_completed


class WorkerPool:
    def __init__(self, workers: int = 4):
        self.workers = workers

    def map(self, fn, items):
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            futures = [pool.submit(fn, item) for item in items]
            return [future.result() for future in as_completed(futures)]
