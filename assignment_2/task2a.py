#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task2a").config("spark.some.config.option", "some-value").getOrCreate()

all_trips = sc.textFile(sys.argv[1],1)
all_trips = all_trips.mapPartitions(lambda x:reader(x))

def func(x):
    if float(x[15])!=None:
        p = float(x[15])
        if p>=0 and p<=5:
            return ('[0,5]', 1)

        elif p>5 and p<=15:
            return ('(5,15]', 1)

        elif p>15 and p<=30:
            return ('(15,30]', 1)

        elif p>30 and p<=50:
            return ('(30,50]', 1)

        elif p>50 and p<=100:
            return ('(50,100]', 1)  
                
        elif p>100:
            return ('[>100)', 1)
        else:
            return ('Invalid number', 1)    
    else:
        return ('None type', 1)    

trip_prices = all_trips.map(lambda x: func(x))
trip_prices_reduced = trip_prices.reduceByKey(lambda x,y: x + y)
trip_prices_reduced = trip_prices_reduced.sortBy(lambda a: a[0])
trip_prices_reduced = trip_prices_reduced.map(lambda x: (x[0], str(x[1])))
trip_prices_reduced = trip_prices_reduced.map(lambda r: ','.join([kvpair for kvpair in r]))
trip_prices_reduced.saveAsTextFile("task2a.out")
