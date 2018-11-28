from pyspark import SparkContext,SparkConf
logFile = "C:\\Users\\Ravi\\Desktop\\forspark.txt"
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile)
logdata2=(logData.collect())
print(logdata2)






