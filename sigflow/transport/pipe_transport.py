from pathlib import Path


class PipeTransport:
    def __init__(self, path):
        self.path = Path(path)

    def write(self, data: bytes) -> None:
        with self.path.open("ab") as fh:
            fh.write(data)
