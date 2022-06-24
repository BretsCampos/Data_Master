import pymongo_spark
from pyspark.sql import SparkSession
import os

pymongo_spark.activate()

spark = SparkSession.builder \
                    .appName("pyspark-mongo") \
                    .enableHiveSupport() \
                    .getOrCreate()

sql = """
SELECT * FROM enem.enem_tratado limit 1000
"""
df = spark.sql(sql)

rdd = df.rdd.map(tuple)

rdd.saveToMongoDB("mongodb://root:root@172.21.0.2:27017/admin.enem")

spark.stop()
