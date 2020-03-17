from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("test_most_popular_movie").setMaster("local")
sc = SparkContext(conf=conf)

# Broadcast variable
# In below example encoding property was used as one character was not being decoded by default utf-8 setting


def movie_names():
    movies = dict()
    with open("/Users/smukherjee/u.item", mode='r', encoding="ISO-8859-1") as movie_name_file:
        lines = movie_name_file.readlines()
        for l in lines:
            fields = l.split("|")
            movies[int(fields[0])] = fields[1]
    print("movies loaded {}".format(type(movies)))
    return movies


def parseLine(line):
    fields = line.split("\t")
    user_id = fields[0]
    movie_id = fields[1]
    rating = int(fields[2])
    timestamp = fields[3]
    return movie_id, rating


# load broadcast variable
bcv_movies = sc.broadcast(movie_names())

rdd = sc.textFile("file:///Users/smukherjee/u.data")
ratings = rdd.map(lambda x: parseLine(x)).map(lambda x: (x[0], 1))
ratings_sum = ratings.reduceByKey(lambda x, y: x+y)
sorted_ratings = ratings_sum.map(lambda x: (x[1], x[0])).sortByKey(ascending=False)

# replacing movie ids with movie names: broadcast variable_name.value[]  is how value is obtained

sorted_ratings_with_movie_names = sorted_ratings.map(lambda x: (bcv_movies.value[int(x[1])], x[0]))

sorted_ratings_list = sorted_ratings_with_movie_names.collect()

for k, v in sorted_ratings_list:
    print(k, v)
