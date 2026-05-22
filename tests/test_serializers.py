from sigflow.parsers.binary import BinaryFrameParser
from sigflow.serializers.binary import encode_stream
from sigflow.core.context import ExecutionContext
from sigflow.core.types import Frame


def test_round_trip():
    frames = [Frame(1, 2, b"payload")]
    parsed = BinaryFrameParser().parse(encode_stream(frames), ExecutionContext({}))
    assert parsed[0].payload == b"payload"
