#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task3b").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

out = all_trips.map(lambda x: ((x[0], x[3].strip()), 1))
out = out.reduceByKey(lambda x,y: x+y)

out = out.filter(lambda x: x[1]>1)
out = out.map(lambda x: (x[0][0], x[0][1]))

out = out.sortBy(lambda a: (a[0], a[1]))

out = out.map(lambda r: ','.join([kvpair for kvpair in r]))
out.saveAsTextFile("task3b.out")

