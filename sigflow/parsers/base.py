from abc import ABC, abstractmethod
from sigflow.core.context import ExecutionContext
from sigflow.core.types import Frame


class BaseParser(ABC):
    name = "base"

    def __init__(self, *, max_payload: int = 8 * 1024 * 1024, max_frames: int = 100000):
        self.max_payload = max_payload
        self.max_frames = max_frames

    @abstractmethod
    def parse(self, data: bytes, context: ExecutionContext) -> list[Frame]:
        raise NotImplementedError

    def require(self, data: bytes, offset: int, size: int) -> bytes:
        if size < 0 or offset < 0 or offset + size > len(data):
            from sigflow.core.exceptions import ParseError
            raise ParseError("truncated input", offset=offset)
        return data[offset:offset + size]
