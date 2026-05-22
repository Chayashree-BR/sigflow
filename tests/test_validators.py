import pytest
from sigflow.core.exceptions import ValidationError
from sigflow.core.types import Frame
from sigflow.validators.frame import validate_frame


def test_validator_rejects_negative_stream():
    with pytest.raises(ValidationError):
        validate_frame(Frame(-1, 0, b""))
