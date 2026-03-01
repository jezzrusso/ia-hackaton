import argparse
import csv
import json
from pathlib import Path

from ultralytics import YOLO


def _read_best_map50(run_dir: Path) -> float:
    """Lê o melhor mAP50 de runs/<nome>/results.csv (se existir)."""
    results_csv = run_dir / "results.csv"
    if not results_csv.exists():
        return float("-inf")

    with results_csv.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        return float("-inf")

    map50_key = next((k for k in rows[0].keys() if "metrics/mAP50(B)" in k), None)
    if not map50_key:
        return float("-inf")

    return max(float(row.get(map50_key, 0) or 0) for row in rows)


def find_best_weights(project_root: Path) -> Path:
    """Escolhe automaticamente o melhor best.pt disponível em /runs."""
    runs_dir = project_root / "runs"
    candidates = []

    for run_dir in runs_dir.glob("*"):
        weight_path = run_dir / "weights" / "best.pt"
        if weight_path.exists():
            candidates.append((weight_path, _read_best_map50(run_dir)))

    if not candidates:
        raise FileNotFoundError("Não achei best.pt dentro de runs/*/weights/best.pt")

    best_weight, best_map50 = max(candidates, key=lambda item: item[1])
    print(f"weights selecionado automaticamente: {best_weight} (melhor mAP50={best_map50:.5f})")
    return best_weight


def predict_one(model: YOLO, image_path: Path, conf: float, iou: float, device: str) -> dict:
    results = model.predict(source=str(image_path), conf=conf, iou=iou, device=device, verbose=False)
    r0 = results[0]

    comps = []
    names = model.names if isinstance(model.names, dict) else {}

    for i, box in enumerate(r0.boxes):
        cls_id = int(box.cls[0].item())
        score = float(box.conf[0].item())
        x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
        comps.append(
            {
                "id": f"c{i + 1}",
                "type": names.get(cls_id, f"class_{cls_id}"),
                "bbox": [x1, y1, x2, y2],
                "confidence": round(score, 4),
            }
        )

    return {"image": str(image_path), "components": comps}


def main():
    parser = argparse.ArgumentParser(description="Predição de componentes com YOLO")
    parser.add_argument("--weights", type=str, default=None, help="Caminho opcional para weights .pt")
    parser.add_argument("--image", type=str, default=None, help="Imagem única para predizer")
    parser.add_argument("--conf", type=float, default=0.001, help="Threshold de confiança")
    parser.add_argument("--iou", type=float, default=0.5, help="Threshold de IoU")
    parser.add_argument("--device", type=str, default="cpu", help="Dispositivo (cpu, 0, etc)")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[2]
    weights = Path(args.weights) if args.weights else find_best_weights(project_root)

    if not weights.exists():
        raise FileNotFoundError(f"Arquivo de peso não encontrado: {weights}")

    model = YOLO(str(weights))

    out_dir = project_root / "output"
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.image:
        image_path = Path(args.image)
        result = predict_one(model, image_path, conf=args.conf, iou=args.iou, device=args.device)
        out_file = out_dir / f"{image_path.stem}_components.json"
        out_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{image_path.name}: {len(result['components'])} componentes detectados")
        print(f"OK: {out_file}")
        return

    aws_img = project_root / "data" / "images" / "train" / "aws.png"
    azure_img = project_root / "data" / "images" / "val" / "azure.png"

    aws_json = predict_one(model, aws_img, conf=args.conf, iou=args.iou, device=args.device)
    (out_dir / "aws_components.json").write_text(json.dumps(aws_json, ensure_ascii=False, indent=2), encoding="utf-8")

    azure_json = predict_one(model, azure_img, conf=args.conf, iou=args.iou, device=args.device)
    (out_dir / "azure_components.json").write_text(json.dumps(azure_json, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"aws.png: {len(aws_json['components'])} componentes detectados")
    print(f"azure.png: {len(azure_json['components'])} componentes detectados")
    print("OK: output/aws_components.json e output/azure_components.json gerados")
    print(f"weights usado: {weights}")


if __name__ == "__main__":
    main()
