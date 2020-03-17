from pyspark.sql import SparkSession, Row, functions
from pyspark import SparkFiles
import os, time

input_file_1 = "/Users/smukherjee/PycharmProjects/untitled/PySpark/orders.csv"
input_file_2 = "/Users/smukherjee/PycharmProjects/untitled/PySpark/customers.csv"
output_dir = "/Users/smukherjee/PycharmProjects/untitled/PySpark/customer_orders/"

if os.path.exists(output_dir):
    for i in os.listdir(output_dir):
        os.remove(os.path.join(output_dir,i))
    os.rmdir(output_dir)
    print("output path deleted")

spark = SparkSession.builder.appName("Customer_order")\
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions","10") \
    .config("spark.sql.inMemoryColumnarStorage.batchsize","10000") \
    .enableHiveSupport() \
    .getOrCreate()

print("SPARK_APPLICATION_ID = {}".format(spark.sparkContext.applicationId))
print("PWD: " + os.getcwd())
print("SparkFiles: " + SparkFiles.getRootDirectory())

for i in os.listdir(SparkFiles.getRootDirectory()):
    print("found {}".format(i))


def parseline(line):
    fields = line.split(",")
    order_id, order_date, order_customer_id, order_status = fields
    return Row(order_customer_id=order_customer_id, order_id=order_id)


def parselineCustomer(line):
    fields = line.split(",")
    customer_id, customer_fname, customer_lname = fields[0], fields[1], fields[2]
    return Row(customer_id=customer_id,customer_lname= customer_lname, customer_fname=customer_fname)


with open(os.path.abspath(input_file_1),'r') as orders_file:
    order_list = orders_file.readlines()
order_rdd = spark.sparkContext.parallelize(order_list).map(lambda l: parseline(l))
order_df = order_rdd.toDF()


with open(os.path.abspath(input_file_2)) as customer_file:
    customer_list = customer_file.readlines()
customer_rdd = spark.sparkContext.parallelize(customer_list).map(lambda l: parselineCustomer(l))
customer_df = customer_rdd.toDF()


joined_df = customer_df.join(order_df,customer_df.customer_id == order_df.order_customer_id,"left_outer")
filter_df = joined_df.where(functions.col("order_id").isNull()).select("customer_lname", "customer_fname")

orderby_df = filter_df.orderBy("customer_lname","customer_fname")

orderby_rdd = orderby_df.rdd.map(lambda l: "{0}, {1}".format(l[0], l[1]))
print(orderby_rdd.take(3))

orderby_rdd.coalesce(1).saveAsTextFile(output_dir)
print("------END OF PROGRAM -------")

spark.stop()


# [8314home@gw03 jan20spark]$ spark-submit --master yarn --deploy-mode client --num-executors 3 --executor-cores 2 --executor-memory 3G customers_without_order.py -files /data/retail_db/orders/part-00000
# SPARK_MAJOR_VERSION is set to 2, using Spark2
# File read completed
# Join and filter completed
# ordering completed
# ['Bolton, Mary', 'Ellison, Albert', 'Green, Carolyn']
# ------END OF PROGRAM -------
# [8314home@gw03 jan20spark]$