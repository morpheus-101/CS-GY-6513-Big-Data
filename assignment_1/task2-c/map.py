#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.strip()
    features = value.split(',')

    num_passengers = int(features[3])
    print "{0:d}\t{1:d}".format(num_passengers, 1)

	
