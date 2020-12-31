#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.strip()
    features = value.split(',')
	
    total_amount = float(features[16])
    if total_amount <= 15:
        print "{0:s}\t{1:d}".format('0-15', 1)
