from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import *

# Approx manhattan bbox
manhattan_bbox = [[-74.0489866963,40.681530375],[-73.8265135518,40.681530375],
                  [-73.8265135518,40.9548628598],[-74.0489866963,40.9548628598],[-74.0489866963,40.681530375]]

def parse_data_from_kafka_message(sdf, schema):
    from pyspark.sql.functions import split
    assert sdf.isStreaming == True, "DataFrame doesn't receive streaming data"
    col = split(sdf['value'], ',')
    # split attributes to nested array in one Column
    # now expand col to multiple top-level columns
    for idx, field in enumerate(schema):
        sdf = sdf.withColumn(field.name, col.getItem(idx).cast(field.dataType))
    return sdf.select([field.name for field in schema])


def clean_sdf_return(sdf_rides: DataFrame) -> DataFrame:
    LON_EAST, LON_WEST, LAT_NORTH, LAT_SOUTH = -73.7, -74.05, 41.0, 40.5
    sdf_rides = sdf_rides.filter(sdf_rides["startLon"].between(LON_WEST, LON_EAST) &
                                 sdf_rides["startLat"].between(LAT_SOUTH, LAT_NORTH) &
                                 sdf_rides["endLon"].between(LON_WEST, LON_EAST) &
                                 sdf_rides["endLat"].between(LAT_SOUTH, LAT_NORTH))
    # Notice that rides with faulty geospatial data as e.g. (0, 0) are filtered out also
    sdf_rides = sdf_rides.filter(sdf_rides["isStart"] == "END") # Keep only finished!
    return sdf_rides


def joined_ride_and_fare(sdfFares: DataFrame, sdfRides:DataFrame ) -> DataFrame:
    # Apply watermarks on event-time columns
    sdfFaresWithWatermark = sdfFares \
        .selectExpr("rideId AS rideId_fares", "startTime", "totalFare", "tip") \
        .withWatermark("startTime", "30 minutes")  # maximal delay

    sdfRidesWithWatermark = sdfRides \
        .selectExpr("rideId", "endTime", "driverId", "taxiId", \
                    "startLon", "startLat", "endLon", "endLat") \
        .withWatermark("endTime", "30 minutes") # maximal delay

    # Join with event-time constraints
    sdf = sdfFaresWithWatermark.join(sdfRidesWithWatermark,
                                     F.expr("""rideId_fares = rideId 
                                     AND startTime < endTime  
                                     AND endTime <= startTime + interval 2 hours"""))
    return sdf


taxiFaresSchema = StructType([ \
    StructField("rideId", LongType()), StructField("taxiId", LongType()), \
    StructField("driverId", LongType()), StructField("startTime", TimestampType()), \
    StructField("paymentType", StringType()), StructField("tip", FloatType()), \
    StructField("tolls", FloatType()), StructField("totalFare", FloatType())])

taxiRidesSchema = StructType([ \
    StructField("rideId", LongType()), StructField("isStart", StringType()), \
    StructField("endTime", TimestampType()), StructField("startTime", TimestampType()), \
    StructField("startLon", FloatType()), StructField("startLat", FloatType()), \
    StructField("endLon", FloatType()), StructField("endLat", FloatType()), \
    StructField("passengerCnt", ShortType()), StructField("taxiId", LongType()), \
    StructField("driverId", LongType())])


def isPointInPath(x, y, poly):
    """check if point x, y is in poly
    poly -- a list of tuples [(x, y), (x, y), ...]"""
    num = len(poly)
    i = 0
    j = num - 1
    c = False
    for i in range(num):
        if ((poly[i][1] > y) != (poly[j][1] > y)) and \
                (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                 (poly[j][1] - poly[i][1])):
            c = not c
        j = i
    return c


def find_nbhd(lon, lat):
    '''takes geo point as lon, lat floats and returns name of neighborhood it belongs to
    needs broadcastVar available'''
    if not isPointInPath(lon, lat, manhattan_bbox):
        return "Other"
    for name, coord in broadcastVar.value.items():
        if isPointInPath(lon, lat, coord):
            return str(name) #cast unicode->str
    return "Other" #geo-point not in neighborhoods


if __name__ == "__main__":
    spark = SparkSession.builder.appName("test kafka").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    print(f"Spark session is : {spark.sparkContext.applicationId}")

    sdfRides = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "taxirides") \
        .option("startingOffsets", "latest") \
        .load() \
        .selectExpr("CAST(value AS STRING)")

    sdfFares = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "taxifares") \
        .option("startingOffsets", "latest") \
        .load() \
        .selectExpr("CAST(value AS STRING)")

    sdfRides = parse_data_from_kafka_message(sdfRides, taxiRidesSchema)
    sdfFares = parse_data_from_kafka_message(sdfFares, taxiFaresSchema)

    sdfRides = clean_sdf_return(sdfRides)

    sdf = joined_ride_and_fare(sdfFares, sdfRides)

    # Broadcast operation & define UDF to get neighbourhood

    nbhds_df = spark.read.json("nbhd.jsonl")# easy loading data
    lookupdict = nbhds_df.select("name", "coord").rdd.collectAsMap() # cast the DataFrame
    broadcastVar = spark.sparkContext.broadcast(lookupdict) # use broadcastVar.value from now on
    find_nbhd_udf = F.udf(find_nbhd, StringType())
    sdf = sdf.withColumn("stopNbhd", find_nbhd_udf("endLon", "endLat"))
    sdf = sdf.withColumn("startNbhd", find_nbhd_udf("startLon", "startLat"))

    sdf = sdf\
        .groupBy(F.window("endTime","30 minutes", "10 minutes"), "stopNbhd")\
        .agg(F.avg(sdf.tip).alias("tips"), F.count(sdf.tip).alias("no_of_tips"))

    query = sdf.selectExpr("*")

    # query = sdfRides.groupBy("driverId").count()

    # to enable below query use append mode as outputMode
    # query = sdfRides.selectExpr("*")

    query.writeStream \
        .outputMode("append")\
        .format("console")\
        .option("truncate", False)\
        .start()\
        .awaitTermination()
