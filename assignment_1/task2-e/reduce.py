#!/usr/bin/env python

import sys

current_key = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
	
    if key == current_key:
        total_trips += 1
	  
	if value not in trips_per_day_dict.keys():
	    trips_per_day_dict[value] = 0
	    trips_per_day_dict[value] += 1
	  
	  
    else:
        if current_key:
	    all_trip_days = float(len(trips_per_day_dict))
            avg_trips_per_day = total_trips / all_trip_days
			
            print "{0:s}\t{1:.2f},{2:.2f}".format(current_key, total_trips, avg_trips_per_day)
			
        total_trips = 1
        trips_per_day_dict = {}
        trips_per_day_dict[value] = 1
        current_key = key


all_trip_days = float(len(trips_per_day_dict))
avg_trips_per_day = total_trips / all_trip_days
print "{0:s}\t{1:.2f},{2:.2f}".format(current_key, total_trips, avg_trips_per_day)
