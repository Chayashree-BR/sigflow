import struct
from sigflow.core.context import ExecutionContext
from sigflow.core.exceptions import ParseError
from sigflow.core.types import Frame
from sigflow.parsers.base import BaseParser
from sigflow.validators.checksum import verify_checksum

MAGIC = b"SGF1"
HEADER = struct.Struct(">4sBBIQII")


class BinaryFrameParser(BaseParser):
    name = "binary"

    def parse(self, data: bytes, context: ExecutionContext) -> list[Frame]:
        frames: list[Frame] = []
        offset = 0
        while offset < len(data):
            if len(frames) >= self.max_frames:
                context.warn("frame-limit", "frame limit reached", offset)
                break
            if len(data) - offset < HEADER.size:
                context.warn("truncated-header", "remaining bytes are smaller than header", offset)
                break
            magic, version, flags, stream_id, sequence, length, checksum = HEADER.unpack_from(data, offset)
            if magic != MAGIC:
                sync = data.find(MAGIC, offset + 1)
                if sync == -1:
                    raise ParseError("unable to resynchronize stream", offset=offset)
                context.warn("resync", "skipped bytes before next frame", offset)
                offset = sync
                continue
            if length > self.max_payload:
                raise ParseError("payload exceeds configured maximum", offset=offset, stream_id=stream_id)
            payload_start = offset + HEADER.size
            payload_end = payload_start + length
            if payload_end > len(data):
                context.warn("truncated-payload", "payload ended before declared length", payload_start)
                break
            payload = self.require(data, payload_start, length)
            check_data = data[offset:offset + HEADER.size - 4] + payload
            if not verify_checksum(check_data, checksum):
                context.warn("checksum", "checksum mismatch", offset)
            frames.append(Frame(stream_id, sequence, payload, version, flags, checksum, offset))
            offset = payload_end
        return frames
