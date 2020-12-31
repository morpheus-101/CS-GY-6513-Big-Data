#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader

spark = SparkSession.builder.appName("task1a-sql").config("spark.some.config.option", "some-value").getOrCreate()

trips = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
fares = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[2])
trip_fare_join = trips.join(fares, on = ['medallion', 'hack_license', 'vendor_id', 'pickup_datetime'], how = 'inner')

trip_fare_join = trip_fare_join.orderBy('medallion', 'hack_license', 'pickup_datetime', ascending=True)


trip_fare_join.select(format_string('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s',\
                                    trip_fare_join.medallion, trip_fare_join.hack_license, trip_fare_join.vendor_id, trip_fare_join.pickup_datetime\
                                    , trip_fare_join.rate_code, trip_fare_join.store_and_fwd_flag, trip_fare_join.dropoff_datetime, trip_fare_join.passenger_count\
                                    , trip_fare_join.trip_time_in_secs, trip_fare_join.trip_distance, trip_fare_join.pickup_longitude, trip_fare_join.pickup_latitude\
                                    , trip_fare_join.dropoff_longitude, trip_fare_join.dropoff_latitude, trip_fare_join.payment_type, trip_fare_join.fare_amount\
                                    , trip_fare_join.surcharge, trip_fare_join.mta_tax, trip_fare_join.tip_amount, trip_fare_join.tolls_amount\
                                    , trip_fare_join.total_amount)).write.save('task1a-sql.out',format="text")

