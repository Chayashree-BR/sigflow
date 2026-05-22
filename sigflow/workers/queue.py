import queue


class TaskQueue:
    def __init__(self, maxsize: int = 1000):
        self._queue = queue.Queue(maxsize=maxsize)

    def put(self, item, timeout: float | None = None) -> None:
        self._queue.put(item, timeout=timeout)

    def get(self, timeout: float | None = None):
        return self._queue.get(timeout=timeout)

    def task_done(self) -> None:
        self._queue.task_done()
