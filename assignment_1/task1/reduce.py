#!/usr/bin/env python

import sys

def join_and_print(same_keys,key):
    part1 = []
    part2 = []
    for s in same_keys:
        if s[-1] == '1':
            part1.append(s[:-2])
        else:
            part2.append(s[:-2])
    for i in part1:
        for j in part2:
            print '%s\t%s,%s' % (key,i,j)

current_key = None
key = None
same_key = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    if current_key == key:
        same_key.append(value)
    else:
        join_and_print(same_key,current_key)
        same_key = [value]
        current_key = key

if current_key == key:
    join_and_print(same_key, key)
