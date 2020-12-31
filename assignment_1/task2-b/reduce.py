#!/usr/bin/env python

import sys

current_key = None
count = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
	
    if key == current_key:
        count += int(value)
	  
    else:
        if current_key:
            print "{0:d}".format(count)
        count = int(value)
        current_key = key

if count:
    print "{0:d}".format(count)
