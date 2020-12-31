#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task3c").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

def func(x):
    if float(x[10])==0 and float(x[11])==0 and float(x[12])==0 and float(x[13])==0:
        return (x[0], (0, 1))
    else:
        return (x[0], (1, 0))

out = all_trips.map(lambda x: func(x))

out = out.reduceByKey(lambda x,y: (x[0] + y[0], x[1] + y[1]))

out = out.map(lambda x: (x[0], "{:.2f}".format(100*(x[1][1]+0)/(x[1][0]+x[1][1]+0.000001))))

out = out.sortBy(lambda a: a[0])

out = out.map(lambda x: (x[0], str(x[1])))

out = out.map(lambda r: ','.join([kvpair for kvpair in r]))
out.saveAsTextFile("task3c.out")

