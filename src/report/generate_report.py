import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Dict, List

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.knowledge_base.catalog import lookup
from src.stride.rules import threats_for_component


def build_threat_report(components_payload: Dict) -> Dict:
    components = components_payload.get("components", [])
    report_components: List[Dict] = []

    for comp in components:
        comp_id = comp.get("id", "unknown")
        comp_type = comp.get("type", "unknown")
        comp_threats = []

        for t in threats_for_component(comp_type):
            kb = lookup(comp_type, t.category)
            comp_threats.append(
                {
                    "category": t.category,
                    "threat": t.title,
                    "description": t.description,
                    "vulnerability": kb.vulnerability,
                    "countermeasures": list(kb.countermeasures),
                    "references": list(kb.references),
                }
            )

        report_components.append(
            {
                "id": comp_id,
                "type": comp_type,
                "confidence": comp.get("confidence"),
                "bbox": comp.get("bbox"),
                "threats": comp_threats,
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_image": components_payload.get("image"),
        "components_analyzed": len(report_components),
        "components": report_components,
    }


def to_markdown(report: Dict) -> str:
    lines = [
        "# Relatório de Modelagem de Ameaças (STRIDE)",
        "",
        f"- Gerado em: `{report['generated_at']}`",
        f"- Imagem de origem: `{report.get('source_image')}`",
        f"- Componentes analisados: **{report['components_analyzed']}**",
        "",
    ]

    if not report["components"]:
        lines.extend([
            "> Nenhum componente detectado para análise.",
            "",
        ])
        return "\n".join(lines)

    for comp in report["components"]:
        lines.append(f"## Componente {comp['id']} ({comp['type']})")
        lines.append(f"- Confiança: `{comp.get('confidence')}`")
        lines.append("")

        if not comp["threats"]:
            lines.append("Sem mapeamento STRIDE para este tipo de componente no MVP.")
            lines.append("")
            continue

        for i, threat in enumerate(comp["threats"], 1):
            lines.append(f"### {i}. [{threat['category']}] {threat['threat']}")
            lines.append(f"- Descrição: {threat['description']}")
            lines.append(f"- Vulnerabilidade associada: {threat['vulnerability']}")
            lines.append("- Contramedidas:")
            for cm in threat["countermeasures"]:
                lines.append(f"  - {cm}")
            lines.append(f"- Referências: {', '.join(threat['references'])}")
            lines.append("")

    return "\n".join(lines)


def process_file(in_file: Path, out_dir: Path) -> None:
    payload = json.loads(in_file.read_text(encoding="utf-8"))
    report = build_threat_report(payload)

    json_out = out_dir / f"{in_file.stem}_threat_report.json"
    md_out = out_dir / f"{in_file.stem}_threat_report.md"

    json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_out.write_text(to_markdown(report), encoding="utf-8")

    print(f"OK: {json_out}")
    print(f"OK: {md_out}")


def main():
    parser = argparse.ArgumentParser(description="Gera relatório STRIDE a partir do JSON de componentes detectados")
    parser.add_argument("--input", type=str, default=None, help="JSON único de componentes")
    parser.add_argument("--input-dir", type=str, default="output", help="Diretório com *_components.json")
    parser.add_argument("--out-dir", type=str, default="output", help="Diretório de saída dos relatórios")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.input:
        process_file(Path(args.input), out_dir)
        return

    input_dir = Path(args.input_dir)
    files = sorted(input_dir.glob("*_components.json"))
    if not files:
        raise FileNotFoundError(f"Nenhum arquivo *_components.json em {input_dir}")

    for file in files:
        process_file(file, out_dir)


if __name__ == "__main__":
    main()
