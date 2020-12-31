#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    features = line.split(',')
    if features[0] == 'medallion':
        continue
 
    if len(features) == 11:
	# for fares data
        flag = str(2)
        print str(features[0]) + ',' + str(features[1]) + ',' + str(features[2]) + ',' + str(features[3]) + '\t' + str(features[4]) + ',' + str(features[5]) + ',' + str(features[6]) + ',' + str(features[7]) + ',' + str(features[8]) + ',' + str(features[9]) + ',' + str(features[10]) + ',' + flag
    
    if len(features) == 14:
	# for trips data
        flag = str(1)
	print str(features[0]) + ',' + str(features[1]) + ',' + str(features[2]) + ',' + str(features[5]) + '\t' + str(features[3]) + ',' + str(features[4]) + ',' + str(features[6]) + ',' + str(features[7]) + ',' + str(features[8]) + ',' + str(features[9]) + ',' + str(features[10]) + ',' + str(features[11]) + ',' + str(features[12]) + ',' + str(features[13]) + ',' + flag

