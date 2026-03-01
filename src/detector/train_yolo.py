from ultralytics import YOLO
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_yaml = project_root / "data" / "data.yaml"

    model = YOLO("yolov8n.pt")

    model.train(
        data=str(data_yaml),
        epochs=80,          # suficiente pro MVP (e mais rápido)
        imgsz=640,
        batch=8,
        device=0,           # GPU
        project=str(project_root / "runs"),
        name="stride_mvp_gpu",
        augment=True
    )

if __name__ == "__main__":
    main()