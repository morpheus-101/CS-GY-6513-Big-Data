#!/usr/bin/env python

import sys

current_key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    revenue, tips = value.split(',')
	
    if key == current_key:
        total_revenue += float(revenue)
        total_tips += float(tips)
    else:
        if current_key:
            print "{0:s}\t{1:.2f},{2:.2f}".format(current_key, total_revenue, total_tips)
        total_revenue = float(revenue)
        total_tips = float(tips)
        current_key = key

print "{0:s}\t{1:.2f},{2:.2f}".format(current_key, total_revenue, total_tips)

