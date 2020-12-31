#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task2d").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

out = all_trips.map(lambda x: (x[0], (1, x[3][:10].strip())))

out = out.reduceByKey(lambda x,y: (x[0] + y[0], x[1] +","+ y[1]))

out = out.map(lambda x: (x[0], x[1][0], len(set(x[1][1].split(','))),  "{:.2f}".format(x[1][0]/len(set(x[1][1].split(','))))))

out = out.sortBy(lambda a: a[0])

out = out.map(lambda x: (x[0], str(x[1]) + "," + str(x[2]) +","+ str(x[3])))

out = out.map(lambda r: ','.join([kvpair for kvpair in r]))
out.saveAsTextFile("task2d.out")

