def decode_text(data: bytes, *, errors: str = "strict") -> str:
    return data.decode("utf-8", errors=errors)


def safe_preview(data: bytes, limit: int = 80) -> str:
    return data[:limit].decode("utf-8", errors="replace")
