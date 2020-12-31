from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pyspark.sql.functions as F
import sys


spark = SparkSession.builder.appName("my_pp").getOrCreate()


print(sys.argv[1])
data_dir = 's3://big-data-class1/batch-job/{}'.format(sys.argv[1])
data = spark.read.csv(data_dir,
                          header = True, inferSchema = True)
                          
                          
#data = data.filter(F.col('Ticker') == 'AAPL')
data = data.select('Date', 'Timestamp', 'Ticker', 'ClosePrice')
data.show(2, False) # should show in console

data = data.withColumn('time', concat(col('Date').cast("string"), lit(" "), col('Timestamp')))\
.withColumn('Timestamp', to_timestamp(substring('time', 0, 13), "yyyyMMdd HH")).drop('Date', 'time')

data.show(2, False)

### add some other statistic you want here
min_max_avg = data.groupBy('Ticker').agg(F.min('ClosePrice').alias('MinClosePrice'), F.max('ClosePrice').alias('MaxClosePrice'), F.avg('ClosePrice').alias('AvgClosePrice'), (F.sum('ClosePrice') / F.count('*')).alias('MovingAvgClosePrice'))

print('min_max_avg')
min_max_avg.show(5, False)

###


#data_trasposed = data.groupBy('Ticker').pivot('ClosePrice').agg(count('ClosePrice')).na.fill(0).orderBy('Ticker')








# output final Spark DataFrame
output_folder = 'processed-batch-job'
output_dir = 's3://big-data-class1/{}/{}_processed_tr.csv'.format(output_folder, sys.argv[1].split('.')[0])
#data_trasposed.coalesce(1).write.csv(output_dir, mode="overwrite", header=True)

output_dir = 's3://big-data-class1/{}/{}_processed_stats.csv'.format(output_folder, sys.argv[1].split('.')[0])
min_max_avg.coalesce(1).write.csv(output_dir, mode="overwrite", header=True)
