class Dispatcher:
    def __init__(self):
        self.handlers = []

    def add(self, handler):
        self.handlers.append(handler)

    def dispatch(self, frame, context):
        current = frame
        for handler in self.handlers:
            current = handler.handle(current, context)
        return current
