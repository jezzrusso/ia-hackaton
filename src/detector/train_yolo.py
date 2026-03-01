from pathlib import Path
import argparse
import sys
import warnings

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

import yaml

from src.detector.write_data_yaml import main as write_data_yaml


def _ensure_absolute_dataset_path(data_yaml: Path, project_root: Path) -> None:
    """Guarantee data.yaml path is absolute and points to existing train/val dirs."""
    payload = yaml.safe_load(data_yaml.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Formato inválido em {data_yaml}")

    dataset_root = payload.get("path")
    if not dataset_root:
        dataset_root = str((project_root / "data").resolve())

    dataset_root_path = Path(dataset_root)
    if not dataset_root_path.is_absolute():
        dataset_root_path = (project_root / dataset_root_path).resolve()

    payload["path"] = dataset_root_path.as_posix()

    train_rel = payload.get("train", "images/train")
    val_rel = payload.get("val", "images/val")
    train_dir = dataset_root_path / train_rel
    val_dir = dataset_root_path / val_rel

    if not train_dir.exists() or not val_dir.exists():
        raise FileNotFoundError(
            "Dataset inválido para treino. "
            f"train existe={train_dir.exists()} ({train_dir}), "
            f"val existe={val_dir.exists()} ({val_dir})"
        )

    data_yaml.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Treino YOLO para o MVP STRIDE")
    parser.add_argument("--device", type=str, default="0", help="Dispositivo de treino (ex.: 0, cpu)")
    parser.add_argument("--epochs", type=int, default=80, help="Número de épocas")
    parser.add_argument("--batch", type=int, default=8, help="Batch size")
    parser.add_argument("--name", type=str, default="stride_mvp_gpu", help="Nome da run")
    args = parser.parse_args()

    data_yaml = project_root / "data" / "data.yaml"

    # Always regenerate and normalize YAML before training to avoid path issues.
    write_data_yaml()
    _ensure_absolute_dataset_path(data_yaml, project_root)

    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Mean of empty slice", category=RuntimeWarning)
        warnings.filterwarnings(
            "ignore",
            message="invalid value encountered in divide",
            category=RuntimeWarning,
        )
        model.train(
            data=str(data_yaml.resolve()),
            epochs=args.epochs,
            imgsz=640,
            batch=args.batch,
            device=args.device,
            project=str(project_root / "runs"),
            name=args.name,
            augment=True,
        )


if __name__ == "__main__":
    main()
