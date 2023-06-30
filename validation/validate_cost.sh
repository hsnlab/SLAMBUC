#!/usr/bin/env bash

trap exit SIGINT SIGTERM

# Execute sensitivity tests
for n in {10..100..10}; do
  #  python3.11 cli.py cost --attr "faas" --size "${n}"
  python3.11 cli.py cost --size "${n}"
  pkill "python3.11 cli.py cost"
done
