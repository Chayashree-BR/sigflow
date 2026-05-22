import tempfile
from pathlib import Path


class IPCChannel:
    def __init__(self, name: str):
        safe = "".join(ch for ch in name if ch.isalnum() or ch in "._-") or "channel"
        self.path = Path(tempfile.gettempdir()) / f"sigflow-{safe}.ipc"

    def publish(self, data: bytes) -> None:
        with self.path.open("ab") as fh:
            fh.write(data)

    def read(self) -> bytes:
        return self.path.read_bytes() if self.path.exists() else b""
