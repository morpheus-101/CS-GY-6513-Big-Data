#!/usr/bin/env python

import sys

ranges = [(0, 20),(20.01, 40),(40.01, 60),(60.01, 80),(80.01, 'infinite')]
range_indicators = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6'] 

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.strip()
    features = value.split(',')

    fare_amount = round(float(features[11]), 2)
    for i, (left, right) in enumerate(ranges):
        if fare_amount >= left and (fare_amount <= right or fare_amount=='infinite'):
            print "{0:s}\t{1:d}".format(range_indicators[i], 1)
            break
	
