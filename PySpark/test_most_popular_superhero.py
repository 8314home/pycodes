from pyspark import SparkConf,SparkContext

conf = SparkConf().setAppName("test_most_popular_superhero").setMaster("local")
sc = SparkContext(conf=conf)


def parsenames(line):
    fields = line.split("\"")
    number = int(fields[0])
    name = fields[1]
    return number, name


def parselines(line):
    fields = line.split(" ")
    hero = int(fields[0])
    no_of_occurance = len(fields) - 1
    return hero, no_of_occurance


marvel_graph_rdd = sc.textFile("file:///Users/smukherjee/Marvel-Graph.txt")
mg_rdd = marvel_graph_rdd.map(lambda x: parselines(x)).reduceByKey(lambda x, y: x+y)
mg_rdd_popular = mg_rdd.map(lambda x:(x[1], x[0])).max()

print("Most popular superhero : {}".format(mg_rdd_popular[1]))

marvel_names_rdd = sc.textFile("file:///Users/smukherjee/Marvel-Names.txt").map(lambda x: parsenames(x))
most_popular_hero_name = marvel_names_rdd.lookup(int(mg_rdd_popular[1]))

if most_popular_hero_name is None:
    print("Name not found for id {}".format(mg_rdd_popular[1]))
else:
    print("Most popular superhero : {}".format(most_popular_hero_name[0]))
