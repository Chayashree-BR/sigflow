from collections.abc import Callable
from sigflow.core.context import ExecutionContext


class Pipeline:
    def __init__(self, stages: list[Callable] | None = None):
        self.stages = list(stages or [])

    def add(self, stage: Callable) -> "Pipeline":
        self.stages.append(stage)
        return self

    def run(self, value, context: ExecutionContext):
        current = value
        for stage in self.stages:
            if context.cancelled:
                context.warn("cancelled", "pipeline cancelled")
                break
            current = stage(current, context)
        return current
