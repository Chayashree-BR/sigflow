from concurrent.futures import ThreadPoolExecutor


class WorkerPool:
    def __init__(self, workers: int = 4):
        self.workers = workers

    def map(self, fn, items):
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            return list(pool.map(fn, items))