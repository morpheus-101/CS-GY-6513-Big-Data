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

from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import StringType

name = 'pickup_datetime'
udf = UserDefinedFunction(lambda x: x.split(' ')[0].strip(), StringType())
new_df = df_withcol.select(*[udf(column).alias(name) if column == name else column for column in df_withcol.columns])

from pyspark.sql import functions as func
tips_revenue = new_df.groupBy('pickup_datetime').agg(func.sum("tolls_amount"))

total_revenue = new_df.groupBy('pickup_datetime').agg(func.sum("fare_amount"), func.sum("surcharge"), func.sum("tip_amount"))

df1 = total_revenue.select(((col("sum(surcharge)") + col("sum(fare_amount)")+ col("sum(tip_amount)"))).alias("total_revenue"))

from pyspark.sql.types import StructType
schema = StructType(tips_revenue.schema.fields + df1.schema.fields)
df1df2 = tips_revenue.rdd.zip(df1.rdd).map(lambda x: x[0]+x[1])
all_revenues = spark.createDataFrame(df1df2, schema)

all_revenues_rdd = all_revenues.rdd.map(tuple)

all_revenues_rdd = all_revenues_rdd.sortBy(lambda x: x[0])

all_revenues_rdd = all_revenues_rdd.map(lambda x: (x[0], "{:.2f}".format(x[2]), "{:.2f}".format(x[1])))

all_revenues_rdd = all_revenues_rdd.map(lambda r: ','.join([kvpair for kvpair in r]))
all_revenues_rdd.saveAsTextFile("task2c-sql.out")
