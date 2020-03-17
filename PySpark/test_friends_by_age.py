from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("test_friends_by_example")
sc = SparkContext(conf=conf)


def parse_lines(line):
    age = int(line.split(",")[2])
    no_of_friend = int(line.split(",")[3])
    return age, no_of_friend


lines = sc.textFile("file:///Users/smukherjee/fakefriends.csv")
age_no_of_friend = lines.map(lambda x: parse_lines(x))

age_based_agg = age_no_of_friend.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
averagesByAge = age_based_agg.mapValues(lambda x: x[0]//x[1])
averagesByAge_list = averagesByAge.collect()

for k, v in averagesByAge_list:
    print("{0} {1}".format(k, v))
