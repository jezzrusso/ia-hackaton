import json
from pathlib import Path
from ultralytics import YOLO
from src.detector.classes import ID_TO_CLASS

def find_best_weights(project_root: Path) -> Path:
    # seus possíveis caminhos (ultralytics varia)
    candidates = [
        project_root / "runs" / "stride_mvp_gpu" / "weights" / "best.pt",
        project_root / "runs" / "detect" / "stride_mvp_gpu" / "weights" / "best.pt",
        project_root / "runs" / "stride_mvp" / "weights" / "best.pt",
        project_root / "runs" / "detect" / "stride_mvp" / "weights" / "best.pt",
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError("Não achei best.pt. Procurei em:\n" + "\n".join(str(c) for c in candidates))

def predict_one(model: YOLO, image_path: Path) -> dict:
    results = model.predict(source=str(image_path), conf=0.01, iou=0.5, device=0)
    r0 = results[0]

    comps = []
    for i, box in enumerate(r0.boxes):
        cls_id = int(box.cls[0].item())
        conf = float(box.conf[0].item())
        x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
        comps.append({
            "id": f"c{i+1}",
            "type": ID_TO_CLASS.get(cls_id, f"class_{cls_id}"),
            "bbox": [x1, y1, x2, y2],
            "confidence": round(conf, 4),
        })

    return {"image": str(image_path), "components": comps}

def main():
    project_root = Path(__file__).resolve().parents[2]
    weights = find_best_weights(project_root)

    model = YOLO(str(weights))

    out_dir = project_root / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    aws_img = project_root / "data" / "images" / "train" / "aws.png"
    azure_img = project_root / "data" / "images" / "val" / "azure.png"

    aws_json = predict_one(model, aws_img)
    (out_dir / "aws_components.json").write_text(json.dumps(aws_json, ensure_ascii=False, indent=2), encoding="utf-8")

    azure_json = predict_one(model, azure_img)
    (out_dir / "azure_components.json").write_text(json.dumps(azure_json, ensure_ascii=False, indent=2), encoding="utf-8")

    print("OK: output/aws_components.json e output/azure_components.json gerados")
    print(f"weights usado: {weights}")

if __name__ == "__main__":
    main()