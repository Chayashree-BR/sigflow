import sys
from pathlib import Path

data = Path(sys.argv[1]).read_bytes()
for offset in range(0, len(data), 16):
    chunk = data[offset:offset + 16]
    print(f"{offset:08x}  {chunk.hex(' ', 1):47}  {chunk.decode('utf-8', 'replace')}")
