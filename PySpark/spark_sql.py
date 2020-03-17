from pyspark.sql import SparkSession, Row, functions
import collections

input_file = "file:///Users/smukherjee/fakefriends.csv"
out_put_dir = "friend_df_cleaned_target_csv"
app_name = "SparkSQL fake friends"
master_value = "local[*]"

spark = SparkSession.builder.appName(app_name).master(master_value)\
    .config("spark.sql.shuffle.partitions","4")\
    .config("spark.sql.inMemoryColumnarStorage.batchSize","10000")\
    .config("spark.sql.autoBroadcastJoinThreshold","10485760")\
    .enableHiveSupport()\
    .getOrCreate()

friend_rdd = spark.sparkContext.textFile(input_file)


def line_to_row_object(line):
    fields = line.split(",")
    return Row(id=int(fields[0]), name=fields[1], age=int(fields[2]), num_of_friends=int(fields[3]))

# Creating DF from RDD (of Row object)
friend_df = friend_rdd.map(lambda l: line_to_row_object(l)).toDF().cache()


# SPARK SQL
friend_df.createOrReplaceTempView("friend_df_table")
teenagers = spark.sql("select * from friend_df_table where 13 <= age and age <= 20")

for i in teenagers.collect():
    print(i)

# Spark DF operation
friend_df.printSchema()
friend_df_filter = friend_df.filter("age >= 13").filter("age <= 20")
friend_df_target = friend_df_filter.groupBy("age").avg("num_of_friends").withColumnRenamed("avg(num_of_friends)",
                                                                                           "avg_num_of_friends")
friend_df_target.printSchema()
friend_df_cleaned_target = friend_df_target.selectExpr("age", "round(avg_num_of_friends,0)")\
    .withColumnRenamed("round(avg_num_of_friends, 0)", "avg_num_of_friends")


print("****** DF operation ********")
friend_df_cleaned_target.write.format("csv").mode("overwrite").option("header", True).save(out_put_dir)


spark.stop()
