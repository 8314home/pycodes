from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("test_wordcount").setMaster("local")
sc = SparkContext(conf=conf)

rdd = sc.textFile("file:///Users/smukherjee/Book.txt")
lines = rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x,1))
final_words = lines.reduceByKey(lambda x, y: x + y)
flipped_rdd = final_words.map(lambda x: (x[1], x[0])).sortByKey(ascending=False)
for cnt, word in flipped_rdd.top(5):
    word2 = word.encode('ascii', 'ignore')
    if word2:
        print(str(cnt), word2)
