from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("test_degree_of_separation").setMaster("local[*]")
sc = SparkContext(conf=conf)


# The characters we wish to find the degree of separation between:
startCharacterID = 5306  # SpiderMan - 5306
targetCharacterID = 14  # ADAM 3,031 (who?)

# Our accumulator, used to signal when we find the target character during
# our BFS traversal.
hitCounter = sc.accumulator(0)

# Step -1 Import Marvel graph data


def line_to_node(line):
    fields = line.split()
    heroid = int(fields[0])
    connections = []  # empty list where association with other heros will be added
    color = "WHITE"
    distance = 9999

    for field in fields[1:]:
        connections.append(int(field))

    if heroid == startCharacterID:
        color = "GRAY"
        distance = 0
        #print("MARKED GRAY FOR starting HERO ID {}".format(heroid))
    #print("fields: {0} {1} {2} {3}".format(heroid, connections, distance, color))
    return heroid, (connections, distance, color)


input_rdd = sc.textFile("file:///Users/smukherjee/Marvel-Graph.txt")
node_rdd = input_rdd.map(lambda l: line_to_node(l))
node_rdd.count()


def bfsMapNode(node):
    heroid = node[0]
    connections = node[1][0]
    distance = node[1][1]
    color = node[1][2]
    result = []

    if color == "GRAY":
        for c in connections:
            new_charid = c
            new_distance = distance + 1
            new_color = "GRAY"
            new_entry = (new_charid, ([], new_distance, new_color))
            if new_charid == targetCharacterID:
                hitCounter.add(1)
            result.append(new_entry)
        color = "BLACK"
    result.append((heroid,(connections, distance, color)))
    return result


# BFS reduce will take all node type values for a char id & merge them to preserve darkest color & shortest path
def bfsreduce(node1, node2):
    no_off_conn1 = node1[0]
    no_off_conn2 = node2[0]
    distance1 = node1[1]
    distance2 = node2[1]
    color1 = node1[2]
    color2 = node2[2]

    no_of_conn = []
    distance = 9999
    color = color1

    if len(no_off_conn1) > 0:
        no_of_conn.extend(no_off_conn1)
    if len(no_off_conn2) > 0:
        no_of_conn.extend(no_off_conn2)

    # Preserve minimum distance
    if distance1 < distance:
        distance = distance1

    if distance2 < distance:
        distance = distance2

    if color1 == "WHITE" and (color2 == "GRAY" or color2 == "BLACK"):
        color = color2
    if color1 == "GRAY" and color2 == "BLACK":
        color = color2
    if color2 == "WHITE" and (color1 == "GRAY" or color1 == "BLACK"):
        color = color1
    if color2 == "GRAY" and color1 == "BLACK":
        color = color1

    return no_of_conn, distance, color


def parsenames(line):
    fields = line.split("\"")
    number = int(fields[0])
    name = fields[1]
    return number, name

# Iteration over RDD

iteration_rdd = node_rdd
for i in range(0, 15):
    print("Iteration {} ".format(i+1))
    node_rdd_explode = iteration_rdd.flatMap(lambda node: bfsMapNode(node))
    print("Processing {} values".format(node_rdd_explode.count()))
    marvel_names_rdd = sc.textFile("file:///Users/smukherjee/Marvel-Names.txt").map(lambda x: parsenames(x))
    startCharacterID_name = marvel_names_rdd.lookup(startCharacterID)
    targetCharacterID_name = marvel_names_rdd.lookup(targetCharacterID)
    if hitCounter.value > 0:
        print("LINK BETWEEN HERO FOUND")
        print("{0} is {2} degree separated from {1}".format(targetCharacterID_name[0], startCharacterID_name[0], hitCounter.value))
        break
    iteration_rdd = node_rdd_explode.reduceByKey(bfsreduce)  # key here is hero id
