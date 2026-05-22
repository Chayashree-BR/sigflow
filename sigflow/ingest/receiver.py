class Receiver:
    def __init__(self, engine):
        self.engine = engine

    def receive(self, chunks) -> list:
        data = b"".join(chunks)
        return self.engine.process(data).frames
