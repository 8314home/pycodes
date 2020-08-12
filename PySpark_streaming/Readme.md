

**Streaming tutorial followed:
https://www.adaltas.com/en/2019/04/18/spark-streaming-data-pipelines-with-structured-streaming/
https://kafka.apache.org/documentation.html**


curl -OL https://archive.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
tar -xzvf spark-2.4.0-bin-hadoop2.7.tgz
ln -sf spark-2.4.0-bin-hadoop2.7 spark_2_4


https://downloads.apache.org/kafka/2.2.2/
curl -OL  https://www-us.apache.org/dist/kafka/2.2.2/kafka_2.11-2.2.2.tgz  
tar -xvzf kafka_2.11-2.2.2.tgz


#### Always start zookeper & kafka server else topiucs already in kafka won't be read
kafka/bin/zookeeper-server-start.sh -daemon kafka/config/zookeeper.properties
kafka/bin/kafka-server-start.sh -daemon kafka/config/server.properties


* Creating kakfa topics
kafka/bin/kafka-topics.sh \
  --create --zookeeper localhost:2181 --replication-factor 1 \
  --partitions 1 --topic taxirides
  
kafka/bin/kafka-topics.sh \
  --create --zookeeper localhost:2181 --replication-factor 1 \
  --partitions 1 --topic taxifares
  
    
in mac coreutils needs to be installed , option is gsplit instead of split 
 
* kakfa producer , producing messages from as file in a stream 
( curl -s https://training.ververica.com/trainingData/nycTaxiRides.gz | zcat | gsplit -l 10000 --filter="kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic taxirides; sleep 0.2" > /dev/null ) &
( curl -s https://training.ververica.com/trainingData/nycTaxiFares.gz | zcat | gsplit -l 10000 --filter="kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic taxifares; sleep 0.2" > /dev/null ) &

* kafka consumer showing data
See data:
kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic taxirides --from-beginning
kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic taxifares --from-beginning  
  
* how to submit spark app for a streaming job with kafka, package is mandatory **org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0**
spark_2_4/bin/spark-submit \
  --master local --driver-memory 1g \
  --num-executors 2 --executor-memory 1g \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 sstream_pyspark_kafka.py
  
#### Watermarking - means max amount of lag we are allowing
For example, the latest event was at 14h05 and watermark is set to 1 hour. A new event with a timestamp at 13h00 would 
be dropped while the one at 13h10 would be marked as valid and kept in the Streaming State (buffer)
 
Unfortunately, the sdfFares DataFrame created from Flink data lacks the “endTime” column and only has the “startTime” column.
 The ride is payed off at the “endTime” and it would make more sense to have this column available in sdfFares.
  The join can be done anyways but in a slightly misleading way. The “startTime” has to be used for watermarking of the 
  sdfFares and “endTime” for watermarking of the sdfRides.
 Consequently, time-constraint relating the beginning and the end of the ride has to be defined for a join.
 
#### code: 
sdfFaresWithWatermark = sdfFares \
  .selectExpr("rideId AS rideId_fares", "startTime", "totalFare", "tip") \
  .withWatermark("startTime", "30 minutes")  # maximal delay

sdfRidesWithWatermark = sdfRides \
  .selectExpr("rideId", "endTime", "driverId", "taxiId", \
    "startLon", "startLat", "endLon", "endLat") \
  .withWatermark("endTime", "30 minutes") # maximal delay

# Join with event-time constraints
sdf = sdfFaresWithWatermark \
  .join(sdfRidesWithWatermark, \
    expr(""" 
     rideId_fares = rideId AND 
      endTime > startTime AND
      endTime <= startTime + interval 2 hours
      """))

#### defining udf:
find_nbhd_udf = udf(find_nbhd, StringType())

What Manhattan neighborhoods should Taxi driver choose to get a high tip?
Adding aggregation

The final operation is averaging over the “tip” column, grouped by ending neighborhoods 
and 30 minutes windowing (updated in 10-minute intervals).
It would be preferable to run 2 hours windows with triggers every minute, but that would demand high computing resources.

tips = sdf \
  .groupBy(
    window("endTime", "30 minutes", "10 minutes"),
    "stopNbhd") \
  .agg(avg("tip"))