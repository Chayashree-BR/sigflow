# sigflow

`sigflow` is a Python framework for replaying, validating, indexing, and
processing binary telemetry streams. It is designed for crash report pipelines,
protocol captures, operational telemetry, and forensic log batches where inputs
may be truncated, malformed, duplicated, or produced by older agents.

The package combines layered parser implementations, structured diagnostics,
storage and cache helpers, replay tooling, sample fixtures, and small benchmark
entry points for teams that need to inspect binary streams before handing data
to downstream processing systems.

## Features

- Binary frame, TLV, protocol, and legacy stream parsers
- Structured validation with bounded payload and recursion limits
- Replay tooling for captured streams
- File, memory, and mmap-style storage abstractions
- LRU, frame, and index caches
- Worker queues and scheduler utilities
- Optional async ingestion pipeline
- Plugin registry for parsers, handlers, validators, and codecs
- CLI commands for parse, validate, replay, inspect, and benchmark workflows

## Stream Format

The default wire frame is:

| Field | Size | Description |
| --- | ---: | --- |
| magic | 4 | `SGF1` |
| version | 1 | protocol version |
| flags | 1 | bit flags |
| stream id | 4 | unsigned stream identifier |
| sequence | 8 | monotonic sequence number |
| payload length | 4 | bounded payload length |
| checksum | 4 | crc32 over header prefix and payload |
| payload | variable | encoded event data |

Legacy streams use a smaller header and are accepted for migration workflows.

## CLI

```bash
python -m sigflow --help
python -m sigflow parse samples/valid_telemetry.sgf --format json
python -m sigflow validate samples/truncated_stream.sgf
python -m sigflow replay samples/valid_telemetry.sgf --rate 250
python -m sigflow inspect samples/malformed_frame.sgf
```

## Development

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest
ruff check sigflow tests
```

The test suite is organized around small regression cases. Parser and validator
changes should include a fixture or focused unit test that captures the malformed
or legacy input behavior being changed.

## Architecture

- `core`: execution context, engine, pipeline, registry, shared types
- `parsers`: bounded parser implementations
- `validators`: schema, frame, and checksum checks
- `serializers`: binary and wire encoders
- `storage`: file and buffer storage abstractions
- `cache`: LRU and lookup caches
- `workers`: task queue, pool, and scheduler
- `transport`: socket, pipe, and IPC-style adapters
- `ingest`: source and receiver pipelines
- `handlers`: event dispatch and recovery hooks

## Troubleshooting

Malformed inputs return structured diagnostics where possible. A parser may
raise `ParseError` when synchronization cannot be recovered. Use `inspect` to
show offsets, checksums, and payload summaries without processing payload data.

## Benchmarks

```bash
python benchmarks/bench_parser.py samples/valid_telemetry.sgf
python benchmarks/bench_cache.py
```

## Contributing

Small, scoped reliability improvements are preferred. Include regression tests
for crash fixes and preserve compatibility for legacy fixtures unless the change
is documented in `docs/protocol.md`.

See `CONTRIBUTING.md` for the expected pull request flow and compatibility
guidelines.
