#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task3a").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

def func(x):
    if float(x[15]) < 0:
        return ("yes", 1)
    else:
        return ('no', 1) 

out = all_trips.map(lambda x: func(x))
out = out.reduceByKey(lambda x,y: x+y)

def func2(x):
    if x[0] == 'yes':
        return x

out = out.filter(lambda x: func2(x))

out = out.map(lambda x: str(x[1]))

out.saveAsTextFile("task3a.out")
