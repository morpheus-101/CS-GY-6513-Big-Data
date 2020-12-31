#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task2b").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

def func(x):
    if float(x[7]) >= 0:
        return (x[7], 1)
    else:
        return ('Invalid', 1)

out = all_trips.map(lambda x: func(x))
out = out.reduceByKey(lambda x,y: x+y)
out = out.sortBy(lambda a: a[0])

out = out.map(lambda x: (x[0], str(x[1])))
out = out.map(lambda r: ','.join([kvpair for kvpair in r]))
out.saveAsTextFile("task2b.out")




