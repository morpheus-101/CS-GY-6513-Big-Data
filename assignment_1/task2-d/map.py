#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.strip()
    features = value.split(',')
    key = key.strip()
    key_features = key.split(',')
	
    date = key_features[3].split(' ')[0]
    total_revenue = float(features[11]) + float(features[12]) + float(features[14])
    tips_amount = float(features[14])
	
    print "{0:s}\t{1:.2f},{2:.2f}".format(date, total_revenue, tips_amount)
