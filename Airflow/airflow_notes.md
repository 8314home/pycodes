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



difference between parallelism & concurrency.

parallelism = 3 means at max 3 tasks run across all currently running dag_runs
max_active_runs_per_dag = 10 means - we can have 10 active dag_runs of same dag.
dag_concurrency = 2 means at max 2 tasks can run with a single dag_run

sequential executor - uses sqlite - one task can run at a time (above properties do not apply)
local executor - done via mysql/postgres tasks are executed in workers (sub processes) usually 1 task for 1 local processor core
celery executor



from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.hive_operator import HiveOperator
from datetime import datetime, timedelta

import fetching_tweet
import cleaning_tweet

default_args = {
	"start_date": datetime(2020, 1, 1),
	"owner": "airflow",
	"depends_on_past": False,
	"wait_for_downstream": True,
	"retries": 2,
	"retry_delay": timedelta(minutes=1)
}

with DAG(dag_id="twitter_dag", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
	task_start_task = DummyOperator(task_id="start_task")
	task_waiting_for_tweets = FileSensor(task_id="waiting_for_tweets",fs_conn_id="fs_tweet", filepath="data.csv", poke_interval=5)
	task_fetching_tweets = PythonOperator(task_id="fetch_tweets", python_callable=fetching_tweet.main)
	task_cleaning_tweets = PythonOperator(task_id="clean_tweets", python_callable=cleaning_tweet.main)
	task_storing_tweets = BashOperator(task_id="storing_tweets", bash_command="hdfs dfs -copyFromLocal -f /tmp/data_cleaned.csv /tmp/")
	task_load_tweets = HiveOperator(task_id="load_tweets_to_hive", hql="load data local inpath '/tmp/data_cleaned.csv' overwrite into table tweets")
	task_end_task = DummyOperator(task_id="end_task")

	task_start_task >> task_waiting_for_tweets >> task_fetching_tweets >> task_cleaning_tweets >> task_storing_tweets >> task_load_tweets >> task_end_task
	task_start_task >> task_end_task


-----------------parent_dag.py----------------------

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator

from subdag_factory import subdag_factory
from datetime import datetime, timedelta

PARENT_DAG_ID = "subdag_test_parent_dag"
SUBDAG_DAG_ID = "subdag_test_subdag_dag"

default_args = {
	"owner": "airflow",
	"depends_on_past": False,
	"retries": 2,
	"retry_delay": timedelta(minutes=1)
}

with DAG(dag_id=PARENT_DAG_ID,
	start_date=datetime(2020, 9, 1),
	schedule_interval="@daily",
	default_args=default_args,
	catchup=False) as dag:
	task_start_task = DummyOperator(task_id="start_task", wait_for_downstream=True)
	task_subdag_task = SubDagOperator(task_id=SUBDAG_DAG_ID, subdag=subdag_factory(PARENT_DAG_ID, SUBDAG_DAG_ID, dag.start_date, dag.schedule_interval))
	task_end_task = DummyOperator(task_id="end_task")
	task_start_task >> task_subdag_task >> task_end_task
	task_start_task >> task_end_task

-----subdag_factory.py------just a python file containing a function taht returns a DAG object---

from airflow.models import DAG
from airflow.operators import DummyOperator


def subdag_factory(PARENT_DAG_ID, SUBDAG_DAG_ID, PARENT_DAG_ID_START_DATE, PARENT_DAG_ID_SCHEDULE_INTERVAL):
	subdag = DAG(dag_id="{0}.{1}".format(PARENT_DAG_ID, SUBDAG_DAG_ID), start_date=PARENT_DAG_ID_START_DATE, schedule_interval=PARENT_DAG_ID_SCHEDULE_INTERVAL, catchup=False)
	with subdag:
		tmp_task_list = [DummyOperator(task_id=f"subdag_task_{i}", dag=subdag) for i in range(5)]
		for j, task_nm in enumerate(tmp_task_list):
			if j > 0:
				tmp_task_list[j - 1] >> task_nm
	return subdag


------using Hooks in Dag--------------------
# Just using a Postgres /Mysql operator will not give back the result, it will just execute the query


from datetime import datetime,timedelta
from airflow.models import DAG
from airflow.hooks import MySqlHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
	"start_date": datetime(2020, 9, 1),
	"owner": "airflow",
	"depends_on_past": False,
	"retries": 2,
	"retry_interval": timedelta(minutes=2)
}

def get_active_sources():
	request = "SELECT * FROM sources"
	mysql_hook = MySqlHook(mysql_conn_id="local_mysql", schema="airflow_mdb")
	conn = mysql_hook.get_conn()
	cursor = conn.cursor()
	cursor.execute(request)
	sources = cursor.fetchall()
	for source in sources:
		print(f"source - {source[0]} activated - {source[1]}")
	return sources


with DAG(dag_id="Hook_Dag", schedule_interval="@once", default_args=default_args, catchup=False) as dag:
	start_task = DummyOperator(task_id="start_task")
	mysql_get_activated_list = PythonOperator(task_id="mysql_get_activated_list", python_callable=get_active_sources)
	start_task >> mysql_get_activated_list


-----------------------------------------------------------------

from datetime import datetime,timedelta
from airflow.models import DAG
from airflow.hooks import MySqlHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    "start_date": datetime(2020, 9, 1),
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 2,
    "retry_interval": timedelta(minutes=2)
}

def get_active_sources(**kwargs):
	ti = kwargs['ti']
	request = "SELECT * FROM sources;"
	mysql_hook = MySqlHook(mysql_conn_id="local_mysql", schema="airflow_mdb")
	conn = mysql_hook.get_conn()
	cursor = conn.cursor()
	cursor.execute(request)
	sources = cursor.fetchall()
	for source in sources:
		if sources[1]:
			ti.xcom_push(key='activated',value=sources[0])
	return sources

def xcom_pull_function(**kwargs):
	ti = kwargs['ti']
	source = ti.xcom_pull(task_ids='mysql_get_activated_list', key='activated')
	print(f"sources pulled via xcom - {source}")


with DAG(dag_id="xcom_hook_dag", schedule_interval="@once", default_args=default_args, catchup=False) as dag:
	start_task = DummyOperator(task_id="start_task")
	mysql_get_activated_list = PythonOperator(task_id="mysql_get_activated_list", python_callable=get_active_sources, provide_context=True)
	xcom_pull_task = PythonOperator(task_id="xcom_pull_task", python_callable=xcom_pull_function, provide_context=True)
	start_task >> mysql_get_activated_list >> xcom_pull_task


----------

/etc/init.d/bootstrap.sh

BranchPythonOperator - supports kwargs to be passed with function



