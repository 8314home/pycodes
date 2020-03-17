from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("test_most_popular_movie").setMaster("local")
sc = SparkContext(conf=conf)


def parseLine(line):
    fields = line.split("\t")
    user_id = fields[0]
    movie_id = fields[1]
    rating = int(fields[2])
    timestamp = fields[3]
    return movie_id, rating


rdd = sc.textFile("file:///Users/smukherjee/u.data")
ratings = rdd.map(lambda x: parseLine(x)).map(lambda x: (x[0], 1))
ratings_sum = ratings.reduceByKey(lambda x, y: x+y)
sorted_ratings = ratings_sum.map(lambda x: (x[1], x[0])).sortByKey(ascending=False)

sorted_ratings_list = sorted_ratings.top(5)

for k, v in sorted_ratings_list:
    print(k, v)
