from sigflow.core.engine import Engine
from sigflow.ingest.receiver import Receiver
from sigflow.ingest.source import FileSource


def ingest_file(path, config=None):
    source = FileSource(path)
    receiver = Receiver(Engine(config))
    return receiver.receive(source.chunks())
