Read CSV file into dataframe:
-----------------------------------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Read CSV File into DataFrame').getOrCreate()

authors = spark.read.csv('D:\python\Scala\Fortune5002017.csv', sep=',',inferSchema=True, header=True)

df = authors.toPandas()
df.head()
print(df1.head()) #display(df.head())

Reading Multiple Files:
----------------------------------
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Read Multiple CSV Files').getOrCreate()

path = ['D:\python\Scala\Fortune5002017.csv','D:\python\Scala\Fortune5002017.csv']

files = spark.read.csv(path, sep=',',inferSchema=True, header=True)

df1 = files.toPandas()
display(df1.head())
display(df1.tail())

---------------------------------------------------
import pyspark # importing the module
from pyspark.sql import SparkSession # importing the SparkSession module
session = SparkSession.builder.appName('First App').getOrCreate() # creating a session
session # calling the session variable
data = session.read.csv('D:\python\Scala\Fortune5002017.csv') # reading the dataset through the given path
data # calling the variable for column created
data.show()

data.printSchema()
data.select('_c0').show()
data.select('_c0','_c1').show()


-------------------------------------------------------
#1. Creating a session
#Let’s get started with the most basic part of working with PySpark – creating a session. The below code can be used to setup your first session.

import pyspark # importing the module
from pyspark.sql import SparkSession # importing the SparkSession module
session = SparkSession.builder.appName('First App').getOrCreate() # creating a session
session # calling the session variable
#Reading a dataset in Spark
#When we talk about a dataset, it is a collection of a huge amount of data and records in a row-column format. They can be in thousands or many more.
data = session.read.option('header', 'true').csv('D:\python\Scala\Sample.csv') 
data
#data.show()
data.printSchema()
data.select('Name').show()
data.select('Name','Age').show()

-----------------------------------------------
# adding columns in dataframe
data = data.withColumn('Age_after_3_y', data['Age']+3)
data.show()
--------------------------------------------------------
#Changing Schema data types:

import pyspark # importing the module
from pyspark.sql import SparkSession # importing the SparkSession module
session = SparkSession.builder.appName('First App').getOrCreate() # creating a session
session # calling the session variable
data = session.read.option('header', 'true').csv('D:\python\Scala\Sample.csv') 
data
data.printSchema() #Everuthing is in string format
data = session.read.option('header', 'true').csv('D:\python\Scala\Sample.csv', inferSchema = True)
data.printSchema() 
#data.show()
data.select('Name').show()
data.select('Name','Age').show()
# adding columns in dataframe
data = data.withColumn('Age_after_3_y', data['Age']+3)
data.show()

--------------------------------------------------------
#Deleting columns and dropping the null values from the dataset

# dropping the columns
data = data.drop('Age_after_3_y')
data.show()

# renaming the columns
data = data.withColumnRenamed('Fare', 'Price')
data.show()

#Filtering the data
data = data.filter(data['PassengerId'] >=16)
data.show()



RDD:
---------------------------------
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate() 

#Create RDD from parallelize    
data = [1,2,3,4,5,6,7,8,9,10,11,12]
rdd=spark.sparkContext.parallelize(data)

#Create RDD from external Data source
rdd2 = spark.sparkContext.textFile("D:\python\Scala\Fortune5002017.csv")

#Reads entire file into a RDD as single record.
rdd3 = spark.sparkContext.wholeTextFiles("D:\python\Scala\Fortune5002017.csv")



#Create empty RDD with partition
rdd2 = spark.sparkContext.parallelize([],10) #This creates 10 partitions

print("initial partition count:"+str(rdd2.getNumPartitions()))
#Outputs: initial partition count:2

#To see the data from RDD
print(rdd3.collect())

#Repartitioning
reparRdd = rdd.repartition(4)
print("re-partition count:"+str(reparRdd.getNumPartitions()))
#Outputs: "re-partition count:4

rdd5 = spark.sparkContext.textFile("D:\python\Scala\test.txt")

print(rdd5.collect())

print(rdd5.getNumPartitions())

rdd6 = rdd5.repartition(4)

print(rdd6.getNumPartitions())

------------Converting RDD into dataframe----------------
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
rdd = spark.sparkContext.parallelize(dept)

df = rdd.toDF()
df.printSchema()
df.show(truncate=False)


-------------Actions by Examples------------------------
# Action - count
print("Count : "+str(rdd5.count()))

# Action - first
firstRec = rdd5.first()
print("First Record : "+str(firstRec[0]) + ","+ firstRec[1])

# Action - max
datMax = rdd5.max()
print("Max Record : "+str(datMax[0]) + ","+ datMax[1])

# Action - reduce
totalWordCount = rdd5.reduce(lambda a,b: (a[0]+b[0],a[1]))
print("dataReduce Record : "+str(totalWordCount[0]))

# Action - take
data3 = rdd5.take(3)
for f in data3:
    print("data3 Key:"+ str(f[0]) +", Value:"+f[1])
    
# Action - collect
data = rdd5.collect()
for f in data:
    print("Key:"+ str(f[0]) +", Value:"+f[1])
    
------------------Convert DF to pandas----------------------
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [("James","","Smith","36636","M",60000),
        ("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),
        ("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
pysparkDF = spark.createDataFrame(data = data, schema = columns)
pysparkDF.printSchema()
pysparkDF.show(truncate=False)

pandasDF = pysparkDF.toPandas()
print(pandasDF)

------------------Pyspark Select--------------------
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(truncate=False)



df.select("firstname","lastname").show()
df.select(df.firstname,df.lastname).show()
df.select(df["firstname"],df["lastname"]).show()

#By using col() function
from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()

#Select columns by regular expression
df.select(df.colRegex("`^.*name*`")).show()

------------------Filter------------------------
from pyspark.sql.types import StructType,StructField 
from pyspark.sql.types import StringType, IntegerType, ArrayType
data = [
    (("James","","Smith"),["Java","Scala","C++"],"OH","M"),
    (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
    (("Julia","","Williams"),["CSharp","VB"],"OH","F"),
    (("Maria","Anne","Jones"),["CSharp","VB"],"NY","M"),
    (("Jen","Mary","Brown"),["CSharp","VB"],"NY","M"),
    (("Mike","Mary","Williams"),["Python","VB"],"OH","M")
 ]
        
schema = StructType([
     StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
         StructField('lastname', StringType(), True)
     ])),
     StructField('languages', ArrayType(StringType()), True),
     StructField('state', StringType(), True),
     StructField('gender', StringType(), True)
 ])

df = spark.createDataFrame(data = data, schema = schema)
df.printSchema()
df.show(truncate=False)


df.filter(df.state == "OH").show(truncate=False)

#Using SQL Expression
df.filter("gender == 'M'").show()
#For not equal
df.filter("gender != 'M'").show()
df.filter("gender <> 'M'").show()

df.filter( (df.state  == "OH") & (df.gender  == "M") ).show(truncate=False)  


-------------Missing values----------------------
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

filePath="D:\python\Scala\small_zipcode.csv"
df = spark.read.options(header='true', inferSchema='true').csv(filePath)

df.printSchema()
df.show(truncate=False)


#Replace 0 for null for all integer columns
df.na.fill(value=0).show()
#Replace 0 for null on only population column 
df.na.fill(value=0,subset=["population"]).show()



df.na.fill("unknown",["city"]).na.fill("",["type"]).show()

------------------------Database Operations----------------------
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
spark = SparkSession.builder.config("spark.jars", "postgresql-42.2.4.jar").master("local[1]").appName("PySpark_Postgres_test").getOrCreate()

df = spark.read.format("jdbc").option("url", "jdbc:postgresql://localhost:5432/dvdrental").option("driver", "org.postgresql.Driver").option("dbtable", "actor").option("user", "postgres").option("password", "postgres").load()

df.show()

df.printSchema()

df.select('*').collect()


df = spark.read.jdbc(url = "jdbc:postgresql://localhost:5432/dvdrental", 
                     table = "(SELECT emp.empno, emp.ename AS employee_name FROM emp  INNER JOIN dept ON emp.deptno = dept.deptno) AS my_table",
                     properties={"user": "postgres", "password": "postgres", "driver": 'org.postgresql.Driver'}).createTempView('tbl')


spark.sql('select * from tbl').show() #or use .collect() to get Rows

-----------Writing back to table---------------
studentDf = spark.createDataFrame([
Row(id=1,name='vijay',marks=67),
Row(id=2,name='Ajay',marks=88),
Row(id=3,name='jay',marks=79),
Row(id=4,name='vinay',marks=67),
])


studentDf.select("id","name","marks").write.format("jdbc")\
    .option("url", "jdbc:postgresql://localhost:5432/dvdrental") \
    .option("driver", "org.postgresql.Driver").option("dbtable", "student") \
    .option("user", "postgres").option("password", "postgres").save()
    
    