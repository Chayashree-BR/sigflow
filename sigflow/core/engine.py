import logging
from sigflow.core.context import ExecutionContext
from sigflow.core.types import ProcessingResult
from sigflow.parsers.protocol import ProtocolParser
from sigflow.validators.frame import validate_frame


class Engine:
    def __init__(self, config: dict | None = None, parser=None):
        self.config = config or {}
        self.parser = parser or ProtocolParser()
        self.logger = logging.getLogger("sigflow.engine")

    def process(self, data: bytes) -> ProcessingResult:
        context = ExecutionContext(self.config, logger=self.logger)
        frames = self.parser.parse(data, context)
        valid = []
        for frame in frames:
            try:
                validate_frame(frame, max_payload=self.config.get("max_payload", 8 * 1024 * 1024))
                valid.append(frame)
            except Exception as exc:
                context.warn("validation", str(exc), frame.offset)
        return ProcessingResult(valid, context.diagnostics, context.elapsed_ms())
