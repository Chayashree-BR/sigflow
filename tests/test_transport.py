from sigflow.transport.ipc import IPCChannel


def test_ipc_channel_sanitizes_name():
    channel = IPCChannel("../demo")
    assert "sigflow-" in channel.path.name
