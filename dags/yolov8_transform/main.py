from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os

def convert_model_to_tensorrt(**kwargs):
    model_path = kwargs['model_path']
    output_path = kwargs['output_path']
    
    os.system(f"python3 convert_to_tensorrt.py --model_path {model_path} --output_path {output_path}")

# DAG 정의
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 10),
    'retries': 1,
}

with DAG(
    'convert_to_tensorrt',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    # 모델 경로 설정
    model_path = "./dags/yolov8_transform/yolov8n.pt"
    output_path = "./dags/yolov8_transform/output/best.engine"

    # PythonOperator 사용하여 TensorRT 변환
    convert_to_tensorrt_task = PythonOperator(
        task_id='convert_model_to_tensorrt',
        python_callable=convert_model_to_tensorrt,
        op_kwargs={'model_path': model_path, 'output_path': output_path},
    )

    convert_to_tensorrt_task
