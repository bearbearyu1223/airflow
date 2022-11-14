from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG(dag_id='first_sample_dag', start_date=datetime.today(), schedule_interval=None) as dag:
    start_task = EmptyOperator(task_id='start')

    print_hello_world = BashOperator(task_id='print_helo_world', bash_command='echo "Hello World!"')

    end_task = EmptyOperator(task_id="end")

start_task >> print_hello_world
print_hello_world >> end_task

