from dataclasses import dataclass, field
import logging
from time import monotonic
from .types import Diagnostic


@dataclass
class ExecutionContext:
    config: dict
    logger: logging.Logger = field(default_factory=lambda: logging.getLogger("sigflow"))
    diagnostics: list[Diagnostic] = field(default_factory=list)
    started_at: float = field(default_factory=monotonic)
    cancelled: bool = False

    def warn(self, code: str, message: str, offset: int = 0) -> None:
        self.diagnostics.append(Diagnostic(code=code, message=message, offset=offset))
        self.logger.debug("%s at %s: %s", code, offset, message)

    def elapsed_ms(self) -> float:
        return (monotonic() - self.started_at) * 1000
