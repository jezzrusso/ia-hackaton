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
from src.stride.interaction_rules import threats_for_interaction
from src.stride.rules import threats_for_component
from src.stride.prioritization import prioritize_components


def _bbox_center(bbox: List[float]) -> tuple[float, float]:
    return ((bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2)


def _squared_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def infer_associations(components: List[Dict], max_neighbors: int = 2) -> List[Dict]:
    """Infere associações entre componentes usando proximidade de bounding boxes.

    Quando o detector não fornece arestas/fluxos explícitos, usamos um fallback
    de vizinhança espacial para enriquecer a análise do relatório.
    """
    candidates = [c for c in components if isinstance(c.get("bbox"), list) and len(c["bbox"]) == 4]
    if len(candidates) < 2:
        return []

    centers = {c["id"]: _bbox_center(c["bbox"]) for c in candidates}
    by_id = {c["id"]: c for c in candidates}
    links = set()

    for src in candidates:
        src_id = src["id"]
        ordered_targets = sorted(
            [c for c in candidates if c["id"] != src_id],
            key=lambda dst: _squared_distance(centers[src_id], centers[dst["id"]]),
        )

        for dst in ordered_targets[:max_neighbors]:
            src_type = by_id[src_id].get("type", "unknown")
            dst_type = dst.get("type", "unknown")
            if not threats_for_interaction(src_type, dst_type):
                continue
            links.add(tuple(sorted((src_id, dst["id"]))))

    return [{"source": s, "target": t} for s, t in sorted(links)]


def build_threat_report(components_payload: Dict) -> Dict:
    components = components_payload.get("components", [])
    selection_info = components_payload.get("selection")
    excluded_components = components_payload.get("excluded_components", [])

    if not selection_info:
        components, excluded_components = prioritize_components(components)
        selection_info = {
            "strategy": "confidence_x_risk",
            "max_components": 15,
            "min_confidence": 0.0,
        }

    report_components: List[Dict] = []
    associations = components_payload.get("associations") or infer_associations(components)
    component_by_id = {c.get("id"): c for c in components}
    interaction_threats: List[Dict] = []

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
                "risk_score": comp.get("risk_score"),
                "priority_score": comp.get("priority_score"),
                "threats": comp_threats,
            }
        )

    for assoc in associations:
        source_id = assoc.get("source")
        target_id = assoc.get("target")
        source = component_by_id.get(source_id, {})
        target = component_by_id.get(target_id, {})
        source_type = source.get("type", "unknown")
        target_type = target.get("type", "unknown")

        threats = [
            {
                "category": t.category,
                "threat": t.title,
                "description": t.description,
            }
            for t in threats_for_interaction(source_type, target_type)
        ]

        if not threats:
            continue

        interaction_threats.append(
            {
                "source": source_id,
                "source_type": source_type,
                "target": target_id,
                "target_type": target_type,
                "threats": threats,
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_image": components_payload.get("image"),
        "components_analyzed": len(report_components),
        "components_excluded": len(excluded_components),
        "selection": selection_info,
        "components": report_components,
        "associations_analyzed": len(interaction_threats),
        "associations": interaction_threats,
    }


def to_markdown(report: Dict) -> str:
    lines = [
        "# Relatório de Modelagem de Ameaças (STRIDE)",
        "",
        f"- Gerado em: `{report['generated_at']}`",
        f"- Imagem de origem: `{report.get('source_image')}`",
        f"- Componentes analisados: **{report['components_analyzed']}**",
        f"- Componentes excluídos por priorização: **{report.get('components_excluded', 0)}**",
        f"- Estratégia de seleção: `{report.get('selection', {}).get('strategy', 'n/a')}`",
        f"- Associações analisadas: **{report.get('associations_analyzed', 0)}**",
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
        lines.append(f"- Risco estimado: `{comp.get('risk_score')}`")
        lines.append(f"- Prioridade (confiança x risco): `{comp.get('priority_score')}`")
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

    if report.get("associations"):
        lines.append("## Ameaças por associação entre componentes")
        lines.append("")
        for assoc in report["associations"]:
            lines.append(
                f"### {assoc['source']} ({assoc['source_type']}) ↔ {assoc['target']} ({assoc['target_type']})"
            )
            for i, threat in enumerate(assoc["threats"], 1):
                lines.append(f"- {i}. [{threat['category']}] {threat['threat']}: {threat['description']}")
            lines.append("")

    return "\n".join(lines)


def process_file(in_file: Path, out_dir: Path) -> None:
    payload = json.loads(in_file.read_text(encoding="utf-8"))
    report = build_threat_report(payload)

    source_image = payload.get("image") or payload.get("source_image")
    base_name = in_file.stem
    if source_image:
        source_name = str(source_image).replace("\\", "/").rsplit("/", maxsplit=1)[-1]
        source_stem = Path(source_name).stem
        if source_stem:
            base_name = f"{source_stem}_components"

    json_out = out_dir / f"{base_name}_threat_report.json"
    md_out = out_dir / f"{base_name}_threat_report.md"

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

    # Usa caminhos absolutos baseados no projeto
    out_dir = project_root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.input:
        process_file(project_root / Path(args.input), out_dir)
        return

    input_dir = project_root / args.input_dir
    files = sorted(input_dir.glob("*_components.json"))
    if not files:
        raise FileNotFoundError(f"Nenhum arquivo *_components.json em {input_dir}")

    for file in files:
        process_file(file, out_dir)


if __name__ == "__main__":
    main()
