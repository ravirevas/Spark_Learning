#how to install pyspark on windows10

1. Download python 3.6
2. Download spark 2.4
3. From pycharm (project interpreter) install pyspark package
4. Install py4j in the same way if its not added.
5.  Add below commands in your code or set these values in pycharm env variables
import os
#os.environ['PYSPARK_PYTHON']="C:\\Users\\Ravi\\AppData\\Local\\Programs\\Python\\Python36-32\\python"
#os.environ['SPARK_HOME'] ="C:\\Users\\Ravi\\Downloads\\spark-2.3.2-bin-hadoop2.7\\spark-2.3.2-bin-hadoop2.7\\spark-2.3.2-bin-hadoop2.7"