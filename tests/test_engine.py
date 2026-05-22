from sigflow.core.engine import Engine


def test_engine_processes_stream(sample_stream):
    result = Engine().process(sample_stream)
    assert len(result.frames) == 2
    assert result.elapsed_ms >= 0
