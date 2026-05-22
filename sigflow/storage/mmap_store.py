import mmap
from pathlib import Path


class MMapReader:
    def __init__(self, path):
        self.path = Path(path)
        self._fh = None
        self._map = None

    def __enter__(self):
        self._fh = self.path.open("rb")
        self._map = mmap.mmap(self._fh.fileno(), 0, access=mmap.ACCESS_READ)
        return self

    def read(self, start: int = 0, size: int | None = None) -> bytes:
        if self._map is None:
            raise RuntimeError("mmap reader is closed")
        end = len(self._map) if size is None else min(len(self._map), start + size)
        return self._map[start:end]

    def __exit__(self, exc_type, exc, tb):
        if self._map is not None:
            self._map.close()
        if self._fh is not None:
            self._fh.close()
