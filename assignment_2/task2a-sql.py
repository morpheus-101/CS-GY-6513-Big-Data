#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()
spark = SparkSession.builder.appName("task2a-sql").config("spark.some.config.option", "some-value").getOrCreate()

f = sc.textFile(sys.argv[1])
data_rdd = f.map(lambda line: [x for x in line.split(',')])

df_withcol = data_rdd.toDF(['medallion','hack_license','vendor_id','pickup_datetime','rate_code','store_and_fwd_flag','dropoff_datetime','passenger_count','trip_time_in_secs','trip_distance','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','payment_type','fare_amount','surcharge','mta_tax','tip_amount','tolls_amount','total_amount'])

output_df = df_withcol.withColumn("fare_amount",df_withcol["fare_amount"].cast('float'))

range1 = output_df.filter((output_df.fare_amount >= 0) & (output_df.fare_amount <= 5)).count()
range2 = output_df.filter((output_df.fare_amount > 5) & (output_df.fare_amount <= 15)).count()
range3 = output_df.filter((output_df.fare_amount > 15) & (output_df.fare_amount <= 30)).count()
range4 = output_df.filter((output_df.fare_amount > 30) & (output_df.fare_amount <= 50)).count()
range5 = output_df.filter((output_df.fare_amount > 50) & (output_df.fare_amount <= 100)).count()
range6 = output_df.filter((output_df.fare_amount > 100)).count()

fare_amount_counts = sc.parallelize([['[0,5]',range1], ['(5,15]',range2], ['(15,30]',range3], ['(30,50]',range4], ['(50,100]',range5], ['[>100)',range6]]).toDF(("amount_range", "num_trips"))

fare_amount_counts.select(format_string('%s, %s', fare_amount_counts.amount_range, fare_amount_counts.num_trips)).write.save('task2a-sql.out', format='text')


