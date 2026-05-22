from sigflow.core.exceptions import ValidationError
from sigflow.core.types import Frame


def validate_frame(frame: Frame, *, max_payload: int = 8 * 1024 * 1024) -> None:
    if frame.stream_id < 0:
        raise ValidationError("stream_id must be non-negative")
    if frame.sequence < 0:
        raise ValidationError("sequence must be non-negative")
    if frame.size > max_payload:
        raise ValidationError("payload exceeds maximum")
