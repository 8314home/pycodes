from pyspark.sql import SparkSession,Row,functions
import os

input_file = "file:///Users/smukherjee/crime_data_sample.csv"
output_dir = "file:///Users/smukherjee/monthly_crime/"

spark = SparkSession.builder.appName("monthly_crime_count_by_type").master("local[*]") \
    .config("spark.sql.shuffle.partitions", "10") \
    .config("spark.sql.inMemoryColumnarStorage.batchSize", "10000") \
    .config("spark.sql.autoBroadcastJoinThreshold", "10485760") \
    .enableHiveSupport() \
    .getOrCreate()

input_rdd = spark.sparkContext.textFile(input_file)


def parseline(line):
    fields = line.split(",")
    crime_date = fields[2]
    crime_type = fields[5]
    crime_date_part = crime_date.split(" ")[0]
    # print(crime_date_part)
    month = crime_date_part.split("/")[0]
    year = crime_date_part.split("/")[2]
    # print(year+month, crime_type)
    return Row(crime_date=year+month, crime_type=crime_type, values=1)


header_data = input_rdd.first()
mapped_rdd = input_rdd.filter(lambda x: x != header_data).map(lambda l: parseline(l))

input_df = mapped_rdd.toDF()

grouped_df = input_df.groupBy("crime_date", "crime_type").sum("values").withColumnRenamed("sum(values)", "count")
grouped_df.printSchema()

sort_df = grouped_df.orderBy(functions.asc("crime_date"), functions.desc("count")).select("crime_date","count","crime_type")
sort_df.printSchema()


sort_rdd = sort_df.rdd
sort_rdd.saveAsTextFile(output_dir, compressionCodecClass="org.apache.hadoop.io.compress.GzipCodec")

# spark-submit --master yarn --deploy-mode cluster --num-executors 3 --executor-cores 2
# --executor-memory 3G /home/8314home/jan20spark/monthly_crime_count.py
# remove master("local[*]" when being run in cluster mode