class SigflowError(Exception):
    """Base exception for sigflow."""


class ParseError(SigflowError):
    def __init__(self, message, offset=0, stream_id=None):
        super().__init__(message)
        self.offset = offset
        self.stream_id = stream_id


class ValidationError(SigflowError):
    pass


class StorageError(SigflowError):
    pass


class TransportError(SigflowError):
    pass
