from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("test_minTemp").setMaster("local")
sc = SparkContext(conf=conf)


def parse_lines(line):
    fields = line.split(",")
    city = fields[0]
    temp_type = fields[2]
    temp_value = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return city, temp_type, temp_value


rdd = sc.textFile("file:///Users/smukherjee/1800.csv")
rdd_values = rdd.map(lambda x: parse_lines(x)).filter(lambda t: t[1] == "TMAX")
cleaned_rdd = rdd_values.map(lambda x: (x[0], x[2]))
final_rdd = cleaned_rdd.reduceByKey(lambda x, y: max(x, y))


for k, v in final_rdd.collect():
    print("{0} {1:.2f}".format(k, v))

