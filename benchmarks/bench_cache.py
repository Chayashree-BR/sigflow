import time
from sigflow.cache.lru import LRUCache

cache = LRUCache(4096)
start = time.perf_counter()
for i in range(100000):
    cache.set(i, i)
    cache.get(i // 2)
print(f"cache: {time.perf_counter() - start:.4f}s")
