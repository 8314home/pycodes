from pyspark.sql import SparkSession, Row


spark = SparkSession.builder.appName("DF_most_popular_movie").master("local[*]").getOrCreate()


def parse_line(line):
    fields = line.split("\t")
    user_id = int(fields[0])
    movie_id = int(fields[1])
    rating = int(fields[2])
    timeinfo = fields[3]
    return Row(user_id=user_id, movie_id=movie_id, rating=rating, timeinfo=timeinfo)


movie_ratings_rdd = spark.sparkContext.textFile("file:///Users/smukherjee/u.data").map(lambda l: parse_line(l))
movie_ratings_df = movie_ratings_rdd.toDF()

# movie_names_rdd = spark.sparkContext.textFile("file:///Users/smukherjee/u.item").map(lambda l: parse_name(l))
movie_names_df = spark.read.csv("file:///Users/smukherjee/u.item", sep="|",
                                encoding="ISO-8859-1").select("_c0", "_c1")\
                                .withColumnRenamed("_c0", "movie_no")\
                                .withColumnRenamed("_c1", "movie_name")


print("movie_names_df")
movie_names_df.printSchema()

most_popular_movie_df = movie_ratings_df.groupBy("movie_id").count().orderBy("count", ascending=False)

top5_most_popular_movies = most_popular_movie_df.join(movie_names_df,
                                                 most_popular_movie_df.movie_id == movie_names_df.movie_no, "inner")\
    .select("movie_name", "count").coalesce(1)
print("\n --------- top5_most_popular_movies Ready: Data sets joined ----------------\n")

for movie_id, count in top5_most_popular_movies.take(5):
    print(movie_id, " -> ", count)

top5_most_popular_movies.write.format("parquet").mode("overwrite").option("header", True)\
    .save("top5_most_popular_movies")

print("\n --------- END oF PROGRAM ----------------\n")
spark.stop()
