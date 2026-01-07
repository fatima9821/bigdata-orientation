#!/usr/bin/python3
import sys

rang = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue

    cin, fg = parts
    try:
        fg = int(fg)
    except ValueError:
        continue

    rang += 1
    print("{}\t{}\t{}".format(cin, fg, rang))