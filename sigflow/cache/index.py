class IndexCache:
    def __init__(self):
        self._offsets: dict[int, list[int]] = {}

    def add(self, stream_id: int, offset: int) -> None:
        self._offsets.setdefault(stream_id, []).append(offset)

    def offsets(self, stream_id: int) -> list[int]:
        return list(self._offsets.get(stream_id, []))
