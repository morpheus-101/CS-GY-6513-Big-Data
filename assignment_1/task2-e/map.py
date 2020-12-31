#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.strip()
    features = value.split(',')
    key = key.strip()
    key_features = key.split(',')
	
    medallion = key_features[0]
    date = key_features[3].split(' ')[0]
    print "{0:s}\t{1:s}".format(medallion, date)
