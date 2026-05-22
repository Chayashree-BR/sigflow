import sys
import time
from pathlib import Path
from sigflow.core.engine import Engine

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("samples/valid_telemetry.sgf")
data = path.read_bytes()
engine = Engine()
start = time.perf_counter()
for _ in range(100):
    engine.process(data)
elapsed = time.perf_counter() - start
print(f"parser: {elapsed:.4f}s for 100 iterations")
