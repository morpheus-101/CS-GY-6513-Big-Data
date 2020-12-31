#!/usr/bin/env python

import sys

def join_list(same_keys,key):
    l1 = []
    l2 = []
    for value in same_keys:
        if value[-1] == '1':
            l1.append(value[:-2])
        else:
            l2.append(value[:-2])
    for v1 in l1:
        for v2 in l2:
            print '%s\t%s,%s' % (key,v1,v2)

current_key = None
key = None
same_key = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    if current_key == key:
        same_key.append(value)
    else:
        join_list(same_key,current_key)
        same_key = [value]
        current_key = key

if current_key == key:
    join_list(same_key, key)

