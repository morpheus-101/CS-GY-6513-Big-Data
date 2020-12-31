#!/usr/bin/env python

import sys

ranges = ["0,20", "20.01,40", "40.01,60", "60.01,80", "80.01,infinite"]
range_indicators = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6']
current_key = None
count = None
range_dict = {}

for i, r in enumerate(ranges):
    range_dict[range_indicators[i]] = r

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')

    if key == current_key:
        count += int(value)

    else:
        if current_key:
            print "{0:s}\t{1:d}".format(range_dict[current_key], count)
        count = int(value)
        current_key = key

if count:
    print "{0:s}\t{1:d}".format(range_dict[current_key], count)
