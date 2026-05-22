import struct
from sigflow.core.types import Frame
from sigflow.parsers.binary import MAGIC
from sigflow.validators.checksum import crc32


def encode_frame(frame: Frame) -> bytes:
    if frame.size > 0xFFFFFFFF:
        raise ValueError("payload too large")
    prefix = struct.pack(">4sBBIQI", MAGIC, frame.version, frame.flags, frame.stream_id, frame.sequence, frame.size)
    checksum = crc32(prefix + frame.payload)
    return prefix + struct.pack(">I", checksum) + frame.payload


def encode_stream(frames: list[Frame]) -> bytes:
    return b"".join(encode_frame(frame) for frame in frames)
