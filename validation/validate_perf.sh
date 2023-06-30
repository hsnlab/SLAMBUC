#!/usr/bin/env bash

trap exit SIGINT SIGTERM

# Execute performance tests
for n in {10..100..10}; do
  python3.11 cli.py perf --alg "ser" --size "${n}"
  pkill "python3.11 cli.py perf"
done

for n in {10..100..10}; do
  python3.11 cli.py perf --alg "par" --size "${n}"
  pkill "python3.11 cli.py perf"
done
