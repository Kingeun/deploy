FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

# Install necessary Airflow dependencies
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install apache-airflow==2.5.1  # Airflow 버전을 지정

# Install NVIDIA CLI tools
RUN apt-get install -y nvidia-cuda-toolkit

# Add your Airflow installation and other configurations
# Copy Airflow scripts and other required files here

# ----------------------------------------------------------
# FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

# # 필수 패키지 설치
# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     libglib2.0-0 \
#     libsm6 \
#     libxrender1 \
#     libxext6 \
#     && apt-get clean

# # Python 패키지 설치
# RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# RUN pip3 install torch-tensorrt tensorrt

# # Airflow 설치
# RUN pip3 install apache-airflow

# ----------------------------------------------------------

