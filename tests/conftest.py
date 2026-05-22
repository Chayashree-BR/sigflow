import pytest
from sigflow.core.types import Frame
from sigflow.serializers.binary import encode_stream


@pytest.fixture
def sample_frames():
    return [Frame(7, 1, b"alpha"), Frame(7, 2, b"beta")]


@pytest.fixture
def sample_stream(sample_frames):
    return encode_stream(sample_frames)
