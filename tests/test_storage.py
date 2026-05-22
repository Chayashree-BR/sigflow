from sigflow.storage.filestore import FileStore


def test_filestore_roundtrip(tmp_path):
    store = FileStore(tmp_path)
    store.write("a/b.bin", b"x")
    assert store.read("a/b.bin") == b"x"
