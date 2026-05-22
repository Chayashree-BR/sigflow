import zlib


def crc32(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF


def verify_checksum(data: bytes, expected: int) -> bool:
    return crc32(data) == (expected & 0xFFFFFFFF)
