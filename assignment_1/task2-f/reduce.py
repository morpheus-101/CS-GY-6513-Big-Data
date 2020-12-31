#!/usr/bin/env python

import sys

current_key = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
	
    if current_key == key:
        if value not in medallions:
	    medallions.append(value)
    else:
        if current_key:
            print "{0:s}\t{1:d}".format(current_key, len(medallions))
        medallions = [value]
        current_key = key

print "{0:s}\t{1:d}".format(current_key, len(medallions))
