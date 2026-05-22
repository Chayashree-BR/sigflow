class BufferPool:
    def __init__(self, buffer_size: int = 65536, limit: int = 32):
        self.buffer_size = buffer_size
        self.limit = limit
        self._free: list[bytearray] = []

    def acquire(self) -> bytearray:
        return self._free.pop() if self._free else bytearray(self.buffer_size)

    def release(self, buffer: bytearray) -> None:
        buffer.clear()
        buffer.extend(b"\x00" * self.buffer_size)
        if len(self._free) < self.limit:
            self._free.append(buffer)
