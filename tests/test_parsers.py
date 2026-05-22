import pytest
from sigflow.core.context import ExecutionContext
from sigflow.core.exceptions import ParseError
from sigflow.parsers.binary import BinaryFrameParser


def test_binary_parser_reads_frames(sample_stream):
    frames = BinaryFrameParser().parse(sample_stream, ExecutionContext({}))
    assert [f.payload for f in frames] == [b"alpha", b"beta"]


def test_binary_parser_reports_truncation(sample_stream):
    ctx = ExecutionContext({})
    frames = BinaryFrameParser().parse(sample_stream[:-2], ctx)
    assert frames
    assert any(d.code in {"truncated-header", "truncated-payload", "checksum"} for d in ctx.diagnostics)


def test_invalid_magic_raises():
    with pytest.raises(ParseError):
        BinaryFrameParser().parse(b"NOPE" + b"0" * 32, ExecutionContext({}))
