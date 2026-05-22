# Protocol

The default sigflow wire format uses a fixed-size big-endian header followed by
a bounded payload. Parsers treat all lengths and offsets as untrusted input.

| Field | Size | Notes |
| --- | ---: | --- |
| magic | 4 | `SGF1` |
| version | 1 | wire format version |
| flags | 1 | bit flags reserved for producers |
| stream id | 4 | unsigned stream identifier |
| sequence | 8 | monotonic sequence number |
| payload length | 4 | payload size in bytes |
| checksum | 4 | CRC32 over header prefix and payload |
| payload | variable | encoded event data |

## Parser Rules

- Payload lengths are capped by parser configuration.
- Frame counts are capped to avoid unbounded replay work.
- Truncated headers and payloads should produce diagnostics when the parser can
  stop at a clean boundary.
- Unrecoverable synchronization failures should raise a structured parse error
  with the byte offset.
- Checksum mismatches should be reported without discarding the frame unless a
  caller explicitly requires strict validation.

## Legacy Streams

The legacy parser accepts the older compact header used by archived exports.
Trailing bytes are reported as diagnostics so migration tools can inspect
partially recovered captures.
