import os
from pyspark import SparkContext,SparkConf
os.environ['PYSPARK_PYTHON']="C:\\Users\\Ravi\\AppData\\Local\\Programs\\Python\\Python36-32\\python"
#os.environ['SPARK_HOME'] ="C:\\Users\\Ravi\\Downloads\\spark-2.3.2-bin-hadoop2.7\\spark-2.3.2-bin-hadoop2.7\\spark-2.3.2-bin-hadoop2.7"
os.environ['SPARK_HOME'] ="C:\\Users\\Ravi\\Downloads\\spark-2.4.0-bin-hadoop2.7\\spark-2.4.0-bin-hadoop2.7"
conf= SparkConf().setMaster("local").setAppName("MYapp")
sc = SparkContext(conf = conf)
a = ["foo", "bar", "baz"]
save=((list, a))
print (save)



