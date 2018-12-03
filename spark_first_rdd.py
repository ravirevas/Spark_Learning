from pyspark import SparkContext,SparkConf

logFile = "C:\\Users\\Ravi\\PycharmProjects\\Spark_Learning\\sampledata\\AAA1_ChoiceAccounting201701010000.txt"

sc = SparkContext("local", "first app")
#sc.setLogLevel("ERROR")
logData = sc.textFile(logFile)
#print(logData.take(1))
line=logData.map(lambda l : l.split(","))
total_count_before=line.count()
new_line=line.map(lambda p : (p[1],p[2]))

print("1st row is")
print(new_line.take(3))









