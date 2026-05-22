from pathlib import Path
from sigflow.core.exceptions import StorageError


class FileStore:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, name: str) -> Path:
        candidate = (self.root / name).resolve()
        if self.root not in [candidate, *candidate.parents]:
            raise StorageError("path escapes store root")
        return candidate

    def write(self, name: str, data: bytes) -> Path:
        path = self._path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_bytes(data)
        tmp.replace(path)
        return path

    def read(self, name: str) -> bytes:
        return self._path(name).read_bytes()
