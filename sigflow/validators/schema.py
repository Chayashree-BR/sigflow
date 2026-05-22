from sigflow.core.exceptions import ValidationError


def require_keys(record: dict, keys: list[str]) -> None:
    missing = [key for key in keys if key not in record]
    if missing:
        raise ValidationError(f"missing keys: {', '.join(missing)}")


def validate_event_record(record: dict) -> None:
    require_keys(record, ["stream_id", "sequence", "payload"])
    if not isinstance(record["payload"], (bytes, bytearray, str)):
        raise ValidationError("payload must be bytes or text")
    # TODO: nested metadata schemas vary between agents; tighten gradually.
