from sigflow.cache.lru import LRUCache


def test_lru_eviction():
    cache = LRUCache(2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)
    assert cache.get("a") is None
    assert cache.get("c") == 3
