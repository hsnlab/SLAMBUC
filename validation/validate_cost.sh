#!/usr/bin/env bash

trap exit SIGINT SIGTERM

# Execute cost tests
for n in {10..100..10}; do
  python3.14 tester_cli cost --alg "ser" --size "${n}"
  pkill "python3.14 tester_cli cost"
done

for n in {10..100..10}; do
  python3.14 tester_cli cost --alg "par" --size "${n}"
  pkill "python3.14 tester_cli cost"
done