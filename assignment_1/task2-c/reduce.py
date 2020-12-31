#!/usr/bin/env python

import sys

current_key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
	
    if key == current_key:
        count += int(value)
	  
    else:
        if current_key:
            print "{0:s}\t{1:d}".format(current_key, count)
        count = int(value)
        current_key = key

if count > 0:
    print "{0:s}\t{1:d}".format(current_key, count)

