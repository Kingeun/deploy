from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# 현재 파일의 디렉토리 경로를 가져옵니다.
source_dir = os.path.abspath(os.path.dirname(__file__))
# 모델 파일의 절대 경로를 설정합니다.
model_path = os.path.join(source_dir, 'model', 'yolov9-s-converted.pt')

# 기본 설정
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


def log_source_dir():
    print("-----------------------------------------------------------")
    print(f"source_dir: {source_dir}")

# DAG 생성
dag = DAG(
    'convert_yolov9_to_trt',
    default_args=default_args,
    description='Convert YOLOv9 model to TensorRT .engine',
    schedule_interval=None,  
)

# .pt 파일에서 .engine 파일로 변환하는 작업
convert_task = BashOperator(
    task_id='convert_to_trt',
    bash_command='python3 /opt/airflow/dags/transform/yolov9/export.py --weights /opt/airflow/dags/transform/model/model.pt --imgsz 1280 --device 0',
    dag=dag,
)

# 로그 기록 작업
log_task = PythonOperator(
    task_id='log_source_dir',
    python_callable=log_source_dir,
    dag=dag,
)


# GitHub 업로드 작업
# upload_github_task = BashOperator(
#     task_id='upload_to_github',
#     bash_command='sh /path/to/upload_to_github.sh',  # GitHub 업로드 스크립트를 포함한 셸 스크립트
#     dag=dag,
# )

# AWS 업로드 작업
# upload_aws_task = BashOperator(
#     task_id='upload_to_aws',
#     bash_command='aws s3 cp /path/to/model.engine s3://your-bucket-name/',
#     dag=dag,
# )

# 작업 순서 정의
log_task >> convert_task #>> upload_github_task
