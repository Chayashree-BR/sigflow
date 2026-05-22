# Contributing

Thanks for improving sigflow. Please keep changes narrowly scoped, include
regression tests for parser or validation fixes, and avoid unrelated refactors.

## Workflow

1. Open an issue or describe the behavior in the pull request.
2. Add or update a fixture when fixing malformed input handling.
3. Run `pytest` and `ruff check sigflow tests`.
4. Keep public APIs and legacy stream behavior backward compatible.

## Repository Map

- `sigflow/parsers`: binary, TLV, protocol, and legacy stream readers
- `sigflow/validators`: frame, schema, and checksum validation helpers
- `sigflow/serializers`: wire-format and JSON serialization helpers
- `sigflow/storage`: file, buffer, and mmap-backed storage utilities
- `sigflow/cache`: lookup caches used by parser and replay workflows
- `sigflow/ingest`: file source and receiver pipeline helpers
- `sigflow/cli`: command-line entry points
- `tests`: focused regression tests and parser fixtures

## Parser and Fixture Changes

Parser fixes should be paired with the smallest input that reproduces the
behavior. Prefer extending an existing test when the behavior is already covered
by a nearby case. Add a new sample under `samples/` only when the byte stream is
useful for manual inspection, replay, or documentation.

When changing malformed input handling, document whether the parser should:

- return a diagnostic and continue,
- stop at the last complete frame, or
- raise a structured exception because synchronization is not recoverable.

## Review Preferences

- Prefer explicit bounds checks over clever offset arithmetic.
- Prefer structured exceptions with offsets and stream ids.
- Keep parser state reset paths easy to reason about.
- Document configuration changes in `README.md` or `docs/`.

## Pull Request Checklist

- Keep the change focused on one parser, validator, transport, or storage path.
- Include tests for new error handling or compatibility behavior.
- Preserve legacy fixtures unless the behavior change is intentional and
  documented.
- Avoid broad cleanup commits in the same pull request as behavioral fixes.
