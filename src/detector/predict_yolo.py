import argparse
import csv
import json
from pathlib import Path
import sys
from typing import Dict, List, Tuple

from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.stride.prioritization import prioritize_components


CATEGORY_COLORS: Dict[str, Tuple[int, int, int]] = {
    "compute": (52, 152, 219),
    "database": (46, 204, 113),
    "network": (155, 89, 182),
    "storage": (241, 196, 15),
    "security": (231, 76, 60),
}


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


def predict_one(
    model: YOLO,
    image_path: Path,
    conf: float,
    iou: float,
    device: str,
    max_components: int,
    min_confidence: float,
) -> dict:
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

    selected, dropped = prioritize_components(
        comps, max_components=max_components, min_confidence=min_confidence
    )
    return {
        "image": str(image_path),
        "components": selected,
        "excluded_components": dropped,
        "selection": {
            "strategy": "confidence_x_risk",
            "max_components": max_components,
            "min_confidence": min_confidence,
        },
    }


def _get_component_color(component_type: str) -> Tuple[int, int, int]:
    return CATEGORY_COLORS.get(component_type.lower(), (52, 73, 94))


def _rect_overlap_area(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> int:
    x1 = max(a[0], b[0])
    y1 = max(a[1], b[1])
    x2 = min(a[2], b[2])
    y2 = min(a[3], b[3])
    if x2 <= x1 or y2 <= y1:
        return 0
    return (x2 - x1) * (y2 - y1)


def _line_point_distance_sq(point: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> float:
    px, py = point
    ax, ay = a
    bx, by = b
    abx = bx - ax
    aby = by - ay
    apx = px - ax
    apy = py - ay
    ab_sq = abx * abx + aby * aby
    if ab_sq == 0:
        return float((px - ax) ** 2 + (py - ay) ** 2)
    t = max(0.0, min(1.0, (apx * abx + apy * aby) / ab_sq))
    qx = ax + t * abx
    qy = ay + t * aby
    return (px - qx) ** 2 + (py - qy) ** 2


def _choose_label_rect(
    box: Tuple[int, int, int, int],
    label_size: Tuple[int, int],
    image_size: Tuple[int, int],
    all_component_boxes: List[Tuple[int, int, int, int]],
    used_label_rects: List[Tuple[int, int, int, int]],
) -> Tuple[int, int, int, int]:
    x1, y1, x2, y2 = box
    lw, lh = label_size
    img_w, img_h = image_size
    pad = 8
    leader_gap = 10
    candidates = [
        (x1, y1 - lh - pad),
        (x2 - lw, y1 - lh - pad),
        (x1, y2 + pad),
        (x2 - lw, y2 + pad),
        (x1 - lw - pad, y1),
        (x2 + pad, y1),
        (x1 - lw - pad, y2 - lh),
        (x2 + pad, y2 - lh),
    ]

    best_rect = None
    best_score = float("inf")
    center = ((x1 + x2) // 2, (y1 + y2) // 2)

    for cx, cy in candidates:
        rx1 = max(0, min(cx, img_w - lw))
        ry1 = max(0, min(cy, img_h - lh))
        rect = (rx1, ry1, rx1 + lw, ry1 + lh)

        score = 0.0
        if _rect_overlap_area(rect, box) > 0:
            score += 5_000

        for other in all_component_boxes:
            overlap = _rect_overlap_area(rect, other)
            if overlap > 0:
                score += overlap

        for used in used_label_rects:
            overlap = _rect_overlap_area(rect, used)
            if overlap > 0:
                score += overlap * 2

        anchor = (rect[0] + lw // 2, rect[1] + lh // 2)
        min_line_dist_sq = min(
            _line_point_distance_sq(((ob[0] + ob[2]) // 2, (ob[1] + ob[3]) // 2), center, anchor)
            for ob in all_component_boxes
        )
        if min_line_dist_sq < leader_gap * leader_gap:
            score += 2_000

        score += (center[0] - anchor[0]) ** 2 * 0.01 + (center[1] - anchor[1]) ** 2 * 0.01

        if score < best_score:
            best_score = score
            best_rect = rect

    if best_rect:
        return best_rect
    return (x1, max(0, y1 - lh - pad), x1 + lw, max(0, y1 - pad))


def _line_width_for_image(image_size: Tuple[int, int]) -> int:
    w, h = image_size
    return max(1, int(min(w, h) * 0.0025))


def annotate_image(image_path: Path, components: List[Dict], output_path: Path) -> None:
    original = Image.open(image_path).convert("RGB")
    canvas = original.copy()
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    img_w, img_h = canvas.size
    component_boxes: List[Tuple[int, int, int, int]] = []

    for comp in components:
        x1, y1, x2, y2 = [int(round(v)) for v in comp["bbox"]]
        x1 = max(0, min(x1, img_w - 1))
        y1 = max(0, min(y1, img_h - 1))
        x2 = max(0, min(x2, img_w - 1))
        y2 = max(0, min(y2, img_h - 1))
        component_boxes.append((x1, y1, x2, y2))

    used_label_rects: List[Tuple[int, int, int, int]] = []
    line_w = _line_width_for_image((img_w, img_h))

    for comp, box in zip(components, component_boxes):
        color = _get_component_color(comp.get("type", ""))
        x1, y1, x2, y2 = box

        draw.rectangle([x1, y1, x2, y2], outline=color, width=line_w)

        text = comp["id"]
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        padding_x, padding_y = 10, 8
        label_w = text_w + (padding_x * 2)
        label_h = text_h + (padding_y * 2)

        label_rect = _choose_label_rect(
            box=box,
            label_size=(label_w, label_h),
            image_size=(img_w, img_h),
            all_component_boxes=component_boxes,
            used_label_rects=used_label_rects,
        )
        used_label_rects.append(label_rect)

        lx1, ly1, lx2, ly2 = label_rect
        draw.rectangle([lx1, ly1, lx2, ly2], fill=color, outline=(255, 255, 255), width=1)

        text_x = lx1 + padding_x
        text_y = ly1 + padding_y
        draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

        source_center = ((x1 + x2) // 2, (y1 + y2) // 2)
        label_center = ((lx1 + lx2) // 2, (ly1 + ly2) // 2)
        if _rect_overlap_area(label_rect, box) == 0:
            draw.line([source_center, label_center], fill=color, width=1)

    canvas.save(output_path)


def main():
    parser = argparse.ArgumentParser(description="Predição de componentes com YOLO")
    parser.add_argument("--weights", type=str, default=None, help="Caminho opcional para weights .pt")
    parser.add_argument("--image", type=str, default=None, help="Imagem única para predizer")
    parser.add_argument("--conf", type=float, default=0.001, help="Threshold de confiança")
    parser.add_argument("--iou", type=float, default=0.5, help="Threshold de IoU")
    parser.add_argument("--device", type=str, default="cpu", help="Dispositivo (cpu, 0, etc)")
    parser.add_argument("--max-components", type=int, default=15, help="Máximo de componentes priorizados")
    parser.add_argument("--min-priority-confidence", type=float, default=0.0, help="Confiança mínima para priorização")
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
        result = predict_one(
            model,
            image_path,
            conf=args.conf,
            iou=args.iou,
            device=args.device,
            max_components=args.max_components,
            min_confidence=args.min_priority_confidence,
        )
        annotated_out = out_dir / f"{image_path.stem}_annotated.png"
        annotate_image(image_path, result["components"], annotated_out)
        result["annotated_image"] = str(annotated_out)
        out_file = out_dir / f"{image_path.stem}_components.json"
        out_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            f"{image_path.name}: {len(result['components'])} componentes priorizados "
            f"(descartados: {len(result.get('excluded_components', []))})"
        )
        print(f"OK: {annotated_out}")
        print(f"OK: {out_file}")
        return

    aws_img = project_root / "data" / "images" / "train" / "aws.png"
    azure_img = project_root / "data" / "images" / "val" / "azure.png"

    aws_json = predict_one(
        model,
        aws_img,
        conf=args.conf,
        iou=args.iou,
        device=args.device,
        max_components=args.max_components,
        min_confidence=args.min_priority_confidence,
    )
    aws_annotated = out_dir / f"{aws_img.stem}_annotated.png"
    annotate_image(aws_img, aws_json["components"], aws_annotated)
    aws_json["annotated_image"] = str(aws_annotated)
    (out_dir / "aws_components.json").write_text(json.dumps(aws_json, ensure_ascii=False, indent=2), encoding="utf-8")

    azure_json = predict_one(
        model,
        azure_img,
        conf=args.conf,
        iou=args.iou,
        device=args.device,
        max_components=args.max_components,
        min_confidence=args.min_priority_confidence,
    )
    azure_annotated = out_dir / f"{azure_img.stem}_annotated.png"
    annotate_image(azure_img, azure_json["components"], azure_annotated)
    azure_json["annotated_image"] = str(azure_annotated)
    (out_dir / "azure_components.json").write_text(json.dumps(azure_json, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        f"aws.png: {len(aws_json['components'])} componentes priorizados "
        f"(descartados: {len(aws_json.get('excluded_components', []))})"
    )
    print(
        f"azure.png: {len(azure_json['components'])} componentes priorizados "
        f"(descartados: {len(azure_json.get('excluded_components', []))})"
    )
    print("OK: output/aws_components.json e output/azure_components.json gerados")
    print("OK: output/aws_annotated.png e output/azure_annotated.png gerados")
    print(f"weights usado: {weights}")


if __name__ == "__main__":
    main()
