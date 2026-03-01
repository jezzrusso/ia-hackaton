from pathlib import Path
import sys

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.detector.classes import CLASSES


def main():
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    yaml_path = data_dir / "data.yaml"

    # Use absolute dataset root to avoid Ultralytics resolving relative paths
    # against its internal default datasets directory on some environments.
    dataset_root = (project_root / "data").resolve().as_posix()

    yaml = [
        f"path: {dataset_root}",
        "train: images/train",
        "val: images/val",
        "",
        "names:",
    ]

    for i, name in enumerate(CLASSES):
        yaml.append(f"  {i}: {name}")

    yaml_path.write_text("\n".join(yaml) + "\n", encoding="utf-8")

    print(f"OK: {yaml_path} atualizado")


if __name__ == "__main__":
    main()
