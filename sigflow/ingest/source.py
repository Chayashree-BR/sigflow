from pathlib import Path


class FileSource:
    def __init__(self, path, chunk_size: int = 1024 * 1024):
        self.path = Path(path)
        self.chunk_size = chunk_size

    def chunks(self):
        with self.path.open("rb") as fh:
            while True:
                chunk = fh.read(self.chunk_size)
                if not chunk:
                    break
                yield chunk
