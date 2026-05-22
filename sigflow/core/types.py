from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Frame:
    stream_id: int
    sequence: int
    payload: bytes
    version: int = 1
    flags: int = 0
    checksum: int = 0
    offset: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def size(self) -> int:
        return len(self.payload)


@dataclass(slots=True)
class Diagnostic:
    code: str
    message: str
    offset: int = 0
    severity: str = "warning"


@dataclass(slots=True)
class ProcessingResult:
    frames: list[Frame]
    diagnostics: list[Diagnostic]
    elapsed_ms: float = 0.0
