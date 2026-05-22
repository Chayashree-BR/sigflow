import signal


class SignalController:
    def __init__(self, context):
        self.context = context

    def install(self):
        signal.signal(signal.SIGINT, self._cancel)
        signal.signal(signal.SIGTERM, self._cancel)

    def _cancel(self, signum, frame):
        self.context.cancelled = True
