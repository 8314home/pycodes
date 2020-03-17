from pyspark import SparkConf,SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingCounter8314Home")
sc = SparkContext(conf=conf)

lines = sc.textFile("file:///Users/smukherjee/u.data")
ratings = lines.map(lambda x: x.split()[2])
result = ratings.countByValue()

print(type(result.items()))

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))