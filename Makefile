.PHONY: test lint bench
test:
	python -m pytest
lint:
	python -m ruff check sigflow tests
bench:
	python benchmarks/bench_parser.py samples/valid_telemetry.sgf
