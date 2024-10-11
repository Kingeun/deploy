import torch
import torch_tensorrt

def convert_to_tensorrt(model_path: str, output_path: str):
    # PyTorch 모델 로드
    model = torch.load(model_path)
    model.eval()

    # TensorRT 변환
    trt_model = torch_tensorrt.compile(model, inputs=[torch_tensorrt.Input((1, 3, 640, 640))])

    # TensorRT 모델 저장
    with open(output_path, "wb") as f:
        f.write(trt_model.serialize())

    print(f"TensorRT 모델이 {output_path}에 저장되었습니다.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert PyTorch model to TensorRT")
    parser.add_argument("--model_path", required=True, help="Path to the trained .pt model")
    parser.add_argument("--output_path", required=True, help="Output path for the .engine file")

    args = parser.parse_args()
    convert_to_tensorrt(args.model_path, args.output_path)
