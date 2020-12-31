#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task1b-sql").config("spark.some.config.option", "some-value").getOrCreate()

f = sc.textFile(sys.argv[1])
data_rdd = f.map(lambda line: [x for x in line.split(',')])

df_withcol = data_rdd.toDF(['medallion','hack_license','vendor_id','pickup_datetime','rate_code','store_and_fwd_flag','dropoff_datetime','passenger_count','trip_time_in_secs','trip_distance','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','payment_type','fare_amount','surcharge','mta_tax','tip_amount','tolls_amount','total_amount'])
df_withcol = df_withcol.filter((df_withcol.passenger_count.cast('float') >= 0))

all_counts = df_withcol.select(df_withcol.columns[7]).groupBy('passenger_count').count()

all_counts = all_counts.sort("passenger_count")

all_counts.passenger_count.cast('string')

all_counts_rdd = all_counts.rdd.map(tuple)

all_counts_rdd = all_counts_rdd.map(lambda x: (x[0], str(x[1])))

all_counts_rdd = all_counts_rdd.map(lambda r: ','.join([kvpair for kvpair in r]))
all_counts_rdd.saveAsTextFile("task2b-sql.out")
