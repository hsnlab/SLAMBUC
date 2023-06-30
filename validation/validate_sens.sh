#!/usr/bin/env bash

trap exit SIGINT SIGTERM

ATTR_CASES=("mem" "lat" "cpu" "eps" "lambda" "bicrit")

# Execute sensitivity tests
for n in {10..100..10}; do
  for attr in "${ATTR_CASES[@]}"; do
    python3.11 cli.py sens --attr "${attr}" --size "${n}"
    pkill "python3.11 cli.py sens"
  done
done
