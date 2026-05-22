import json
from sigflow.core.types import Frame


def frame_to_json(frame: Frame) -> dict:
    return {
        "stream_id": frame.stream_id,
        "sequence": frame.sequence,
        "version": frame.version,
        "flags": frame.flags,
        "size": frame.size,
        "payload_hex": frame.payload.hex(),
    }


def dumps(frames: list[Frame]) -> str:
    return json.dumps([frame_to_json(frame) for frame in frames], indent=2)
