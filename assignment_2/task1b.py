#!/usr/bin/env python
import sys
from pyspark.sql import *
from pyspark.sql.functions import *
from csv import reader
from pyspark import SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("task1b").config("spark.some.config.option", "some-value").getOrCreate()

fares = sc.textFile(sys.argv[1],1)
fares = fares.mapPartitions(lambda x:reader(x))

licenses = sc.textFile(sys.argv[2],1)
licenses = licenses.mapPartitions(lambda x:reader(x))


fares = fares.filter(lambda x: x[0]!='medallion')
licenses = licenses.filter(lambda x: x[0]!='medallion')



fares = fares.map(lambda x: (str(x[0]) , str(x[1]) +'*'+ str(x[2]) +'*'+ str(x[3]) +'*'+ str(x[4]) +'*'+ str(x[5]) +'*'+ str(x[6]) +'*'+ str(x[7]) +'*'+ str(x[8]) +'*'+ str(x[9]) +'*'+ str(x[10])))

licenses = licenses.map(lambda x: (str(x[0]) , str(x[1]) +'*'+ str(x[2]) +'*'+ str(x[3]) +'*'+ str(x[4]) +'*'+ str(x[5]) +'*'+ str(x[6]) +'*'+ str(x[7]) +'*'+ str(x[8]) +'*'+ str(x[9]) +'*'+ str(x[10]) +'*'+ str(x[11]) +'*'+ str(x[12]) +'*'+ str(x[13]) +'*'+ str(x[14]) +'*'+ str(x[15])))

fares_licenses_join = fares.join(licenses)

fares_licenses_join = fares_licenses_join.map(lambda x: (x[0], (x[1][0], x[1][1].replace(',',''))))

fares_licenses_join = fares_licenses_join.map(lambda x: (x[0], (x[1][0].replace('*',','), x[1][1].replace('*',','))))

fares_licenses_join = fares_licenses_join.map(lambda x: (x[0], (str(x[1][0]) + ',', x[1][1])))

fares_licenses_join = fares_licenses_join.map(lambda x: (x[0],''.join(x[1])))
fares_licenses_join = fares_licenses_join.map(lambda r: ','.join([kvpair for kvpair in r]))
fares_licenses_join.saveAsTextFile("task1b.out")
