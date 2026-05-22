from sigflow.core.registry import codecs


class RawCodec:
    name = "raw"

    def encode(self, data: bytes) -> bytes:
        return bytes(data)

    def decode(self, data: bytes) -> bytes:
        return bytes(data)


codecs.register("raw", RawCodec, replace=True)
