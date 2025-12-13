# Databricks notebook source
dbutils.fs.ls('/Workspace/Users/anshulkhandelwal2904@gmail.com/data-practice-datasets/CSV/')

# COMMAND ----------

df = spark.read.format('csv').option('inferschema', True).option('header', True).load('/Workspace/Users/anshulkhandelwal2904@gmail.com/data-practice-datasets/CSV/banking.csv')
df.display()

# COMMAND ----------

df = spark.read.csv('/Workspace/Users/anshulkhandelwal2904@gmail.com/data-practice-datasets/CSV/banking.csv', header=True, inferSchema=True)


# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.filter((col('marital') == 'married') & (col('age') >= 40) & (col('age') <= 43) & (col('job') == 'blue-collar') & (col('education') == 'high.school'))\
 .select(col('age'), col('job'), col('marital'), col('education')).display()


# COMMAND ----------

from pyspark.sql.functions import *
df.select(col('age'), col('job'), col('marital'), col('education')).display()
df.filter(col('age') > 50).select(col('age'), col('job'), col('marital'), col('education')).display()

# COMMAND ----------


