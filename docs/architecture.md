# Architecture

sigflow is organized as a layered stream-processing package. Sources produce
byte chunks, parsers turn bytes into frames, validators attach diagnostics, and
handlers or callers decide how to process accepted frames. Storage and cache
modules provide small reusable helpers for replay, inspection, and indexing
workflows.

## Flow

1. `ingest` reads bytes from a source.
2. `core.Engine` creates an execution context and invokes the configured parser.
3. `parsers` produce `Frame` objects or structured parse errors.
4. `validators` check frame-level invariants such as payload bounds.
5. `handlers`, `storage`, and `cache` modules can be composed by callers or CLI
   workflows.

## Extension Points

The registry module supports registering parsers, handlers, validators, and
codecs without hard-coding every implementation into the CLI. Built-in parsers
remain intentionally small so compatibility fixes can be reviewed in isolation.

## Compatibility Notes

Legacy stream support is kept separate from the default binary parser. Changes
to legacy behavior should be scoped and documented in `docs/protocol.md` because
older telemetry captures may depend on partial-frame and trailing-byte handling.
