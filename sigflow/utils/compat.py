from pathlib import Path


def read_binary(path) -> bytes:
    return Path(path).read_bytes()


def ensure_bytes(value) -> bytes:
    if isinstance(value, bytes):
        return value
    if isinstance(value, str):
        return value.encode("utf-8")
    return bytes(value)
