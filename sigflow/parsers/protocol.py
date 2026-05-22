from sigflow.core.context import ExecutionContext
from sigflow.core.types import Frame
from sigflow.parsers.binary import BinaryFrameParser
from sigflow.parsers.tlv import TLVParser


class ProtocolParser:
    name = "protocol"

    def __init__(self):
        self.parsers = [BinaryFrameParser(), TLVParser()]

    def parse(self, data: bytes, context: ExecutionContext) -> list[Frame]:
        last_error = None
        for parser in self.parsers:
            try:
                frames = parser.parse(data, context)
                if frames:
                    return frames
            except Exception as exc:  # fallback is intentionally broad for compatibility
                last_error = exc
                context.warn("parser-fallback", f"{parser.name} failed: {exc}")
        if last_error:
            raise last_error
        return []
