Airflow:

Apache Airflow is a way to programmatically author, schedule, and monitor (batch) data pipelines.


Airflow commands:


## once a dag is triggered it gets executed after scheduling interval for that dag is over, eg: a Dag which is supposed run in 15 min interval if started at 5:05 pm then it will actually gets executed at 5:20 pm. NOT at 5:05 pm


airflow cli:
airflow initdb .
sqlite airflow.db

airflow resetdb 
airflow webserver
airflow scheduler

airflow list_dags
airflow list_tasks "dagName" --tree
airflow --h

airflow test dag_name task_name execution_date - useful for unit testing


# Important properties of Dag:

1. dag_id
2. start_date - if set today will run at starte_date + schedule_interval
3. schedule_interval
4. depends_on_past - 
5. default_args - dict of variables


catchup=False usually set to false , else it will backfill for all previous un-triggered schedule intervals


FileSensor operator = waits for a file to appear at a location, can be hdfs
FileSensor(task_id="waiting_for_file", fs_conn_id="fs_connection", filepath="data.csv", poke_interval='5')
# We need to create connection, for fs_connection
fs_connection = go to url->Admin->Connection

Python_operator = allows to execute arbitary python code



from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operator.python_operator import PythonOperator
from airflow.operator.bash_operator import BashOperator
from airflow.operator.hive_operator import HiveOperator
from datetime import datetime


import fetching_tweet # it is a python file containing python code to clean data
import cleaning_tweet

# list of args to applied to all operators.
default_args = {
	"start_date" = datetime(2020,1,1),
	"owner" = "user_1"

}


with DAG(dag_id='twitter_dag', schedule_interval='@daily', default_args = default_args, catchup=False) as dag:
	waiting_for_file = FileSensor(task_id="waiting_for_file", fs_conn_id="fs_connection", filepath="data.csv", poke_interval='5')

	fetching_tweet = PythonOperator(task_id="fetching_tweet", python_callable=fetching_tweet.main)

	cleaning_tweet = PythonOperator(task_id="cleaning_tweet", python_callable=fetching_tweet.main)

	move_file_to_hdfs = BashOperator(task_id="move_file_to_hdfs", bash_command="hdfs dfs -put -f /tmp/file_name /tmp/")

	loading_tweet = HiveOprator(task_id="loading_tweet", hql="load data inpath '/tmp/data_cleaned.csv' into TABLE table_name")

	# hql - accepts hql file as well

	waiting_for_file >> fetching_tweet >> cleaning_tweet >> move_file_to_hdfs >> loading_tweet










