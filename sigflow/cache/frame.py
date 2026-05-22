from sigflow.cache.lru import LRUCache


class FrameCache:
    def __init__(self, capacity: int = 4096):
        self.cache = LRUCache(capacity)

    def key(self, frame) -> tuple[int, int]:
        return frame.stream_id, frame.sequence

    def put(self, frame) -> None:
        self.cache.set(self.key(frame), frame)

    def get(self, stream_id: int, sequence: int):
        return self.cache.get((stream_id, sequence))
