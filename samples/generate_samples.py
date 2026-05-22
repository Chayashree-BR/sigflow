import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sigflow.core.types import Frame
from sigflow.serializers.binary import encode_stream

ROOT = Path(__file__).resolve().parent
ROOT.mkdir(exist_ok=True)
valid = encode_stream([Frame(42, 1, b"service=api status=ok"), Frame(42, 2, b"service=worker status=ok")])
(ROOT / "valid_telemetry.sgf").write_bytes(valid)
(ROOT / "truncated_stream.sgf").write_bytes(valid[:-7])
(ROOT / "malformed_frame.sgf").write_bytes(b"BAD!" + valid[4:28])
(ROOT / "oversized_payload.sgf").write_bytes(b"SGF1\x01\x00\x00\x00\x00\x01" + b"\x00" * 24)
