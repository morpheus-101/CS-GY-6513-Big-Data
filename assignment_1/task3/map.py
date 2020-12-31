#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.replace('\t', ',')
    features = line.split(',')
    if features[0] == 'medallion':
        continue
 
    if len(features) == 21:
        flag = str(1)
        print str(features[0]) + '\t' + str(features[1]) + ',' + str(features[2]) + ',' + str(features[3]) + ',' + str(features[4]) + ',' + str(features[5]) + ',' + str(features[6]) + ',' + str(features[7]) + ',' + str(features[8]) + ',' + str(features[9]) + ',' + str(features[10]) + ',' + str(features[11]) + ',' + str(features[12]) + ',' + str(features[13]) + ',' + str(features[14]) + ',' + str(features[15]) + ',' + str(features[16]) + ',' + str(features[17]) + ',' + str(features[18]) + ',' + str(features[19]) + ',' + str(features[20]) + ',' + flag
    
    if len(features) == 16:
        flag = str(2)
	print str(features[0]) + '\t' + str(features[1]) + ',' + str(features[2]) + ',' + str(features[3]) + ',' + str(features[4]) + ',' + str(features[5]) + ',' + str(features[6]) + ',' + str(features[7]) + ',' + str(features[8]) + ',' + str(features[9]) + ',' + str(features[10]) + ',' + str(features[11]) + ',' + str(features[12]) + ',' + str(features[13]) + ',' + str(features[14]) + ',' + str(features[15]) + ',' + flag
			
			


