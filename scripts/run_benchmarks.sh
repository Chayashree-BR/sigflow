#!/usr/bin/env sh
python benchmarks/bench_parser.py samples/valid_telemetry.sgf
python benchmarks/bench_cache.py
