from pathlib import Path
from src.detector.classes import CLASSES

def main():
    # raiz do projeto = 2 níveis acima deste arquivo
    project_root = Path(__file__).resolve().parents[2]

    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    yaml_path = data_dir / "data.yaml"

    yaml = [
        "path: data",
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