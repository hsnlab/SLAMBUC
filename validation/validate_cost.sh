#!/usr/bin/env bash

trap exit SIGINT SIGTERM

# Execute cost tests
for n in {10..100..10}; do
  python3.13 cli.py cost --alg "ser" --size "${n}"
  pkill "python3.13 cli.py cost"
done

for n in {10..100..10}; do
  python3.13 cli.py cost --alg "par" --size "${n}"
  pkill "python3.13 cli.py cost"
done