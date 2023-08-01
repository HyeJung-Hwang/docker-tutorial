from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# DAG 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_boaz_dag',
    default_args=default_args,
    description='간단한 Hello Boaz DAG',
    schedule_interval=timedelta(days=1),  # 매일 실행
)

# 작업 정의
task_hello_world = BashOperator(
    task_id='hello_world_task',
    bash_command='echo "Hello, Boaz!"',
    dag=dag,
)

# 작업 간의 실행 순서 정의
task_hello_world

