#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task4c").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

all_lic = all_trips.map(lambda x: (x[20], float(x[5])))
all_lic = all_lic.reduceByKey(lambda x,y: x + y)
all_lic = all_lic.sortBy(lambda a: a[0],ascending=False)
all_lic = all_lic.map(lambda x: (x[0], str("{:.2f}".format(x[1]))))
all_lic = all_lic.map(lambda r: ','.join([kvpair for kvpair in r]))
all_lic.saveAsTextFile("task4c.out")

