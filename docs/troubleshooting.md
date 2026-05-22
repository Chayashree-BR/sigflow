# Troubleshooting

Use `sigflow inspect <path>` to examine stream prefixes and sizes. For checksum
warnings, verify the producer uses the same wire version. For truncated streams,
prefer replaying from the last complete frame boundary.

## Common Diagnostics

- `truncated-header`: the stream ended before a complete frame header was read.
- `truncated-payload`: the declared payload length extends beyond available
  bytes.
- `checksum`: the frame checksum did not match the encoded payload.
- `resync`: bytes were skipped before the parser found the next frame marker.
- `frame-limit`: parsing stopped at the configured frame cap.

## Debugging Workflow

Start with `inspect` to confirm the file prefix and total size, then use
`validate` to collect diagnostics without replaying payloads. When a producer
change is suspected, compare the captured header fields against
`docs/protocol.md` before changing parser behavior.
