#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    key = key.strip()
    key_features = key.split(',')
	
    medallion = key_features[0]
    license = key_features[1]
    print "{0:s}\t{1:s}".format(license, medallion)
	
