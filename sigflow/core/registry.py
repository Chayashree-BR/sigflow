from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Registry:
    name: str
    _items: dict[str, Any] = field(default_factory=dict)

    def register(self, key: str, value: Any, *, replace: bool = False) -> None:
        normalized = key.strip().lower()
        if not normalized:
            raise ValueError("registry key must not be empty")
        if normalized in self._items and not replace:
            raise KeyError(f"{self.name} already contains {normalized}")
        self._items[normalized] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._items.get(key.strip().lower(), default)

    def create(self, key: str, *args, **kwargs) -> Any:
        item = self.get(key)
        if item is None:
            raise KeyError(f"unknown {self.name}: {key}")
        return item(*args, **kwargs) if isinstance(item, type) or callable(item) else item

    def decorator(self, key: str) -> Callable[[Any], Any]:
        def wrap(value: Any) -> Any:
            self.register(key, value)
            return value
        return wrap


parsers = Registry("parser")
handlers = Registry("handler")
codecs = Registry("codec")
validators = Registry("validator")
