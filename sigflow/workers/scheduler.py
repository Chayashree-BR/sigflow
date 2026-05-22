import time
from dataclasses import dataclass


@dataclass(order=True)
class ScheduledJob:
    run_at: float
    name: str
    payload: object


class Scheduler:
    def __init__(self):
        self.jobs: list[ScheduledJob] = []

    def every(self, delay: float, name: str, payload=None) -> None:
        self.jobs.append(ScheduledJob(time.monotonic() + delay, name, payload))

    def due(self) -> list[ScheduledJob]:
        now = time.monotonic()
        ready = [job for job in self.jobs if job.run_at <= now]
        self.jobs = [job for job in self.jobs if job.run_at > now]
        return ready
