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