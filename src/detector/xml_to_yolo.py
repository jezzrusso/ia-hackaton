from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from typing import Dict, Iterable, List, Optional, Tuple

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.detector.classes import CLASS_TO_ID, CLASSES


DEFAULT_SERVICE_TO_GENERIC: Dict[str, str] = {
    # user
    "user": "user",
    "client": "user",
    "browser": "user",
    "admin": "user",
    "customer": "user",
    "developer_portal": "user",
    "sei_sip": "user",
    # edge_security
    "waf": "edge_security",
    "firewall": "edge_security",
    "security_group": "edge_security",
    "nsg": "edge_security",
    "cloudflare": "edge_security",
    "identity_access_management": "edge_security",
    "identity_and_access_management": "edge_security",
    "identity_access_management_role": "edge_security",
    "iam": "edge_security",
    "key_vault": "edge_security",
    "key_vaults": "edge_security",
    "entra": "edge_security",
    "microsoft_entra": "edge_security",
    # gateway
    "gateway": "gateway",
    "api_gateway": "gateway",
    "apigateway": "gateway",
    "apim": "gateway",
    "ingress": "gateway",
    "load_balancer": "gateway",
    "lb": "gateway",
    "cloudfront": "gateway",
    "route_53": "gateway",
    "vpc": "gateway",
    "virtual_private_cloud": "gateway",
    "virtual_network": "gateway",
    "virtual_networks": "gateway",
    "subnet": "gateway",
    "public_subnet": "gateway",
    "private_subnet": "gateway",
    "region": "gateway",
    # compute
    "compute": "compute",
    "server": "compute",
    "vm": "compute",
    "virtual_machine": "compute",
    "ec2": "compute",
    "lambda": "compute",
    "ecs": "compute",
    "eks": "compute",
    "aks": "compute",
    "gke": "compute",
    "app_service": "compute",
    "container": "compute",
    "cloud_run": "compute",
    "openai": "compute",
    "machine_learning": "compute",
    "machine_learning_studio_workspaces": "compute",
    # data_store
    "data_store": "data_store",
    "database": "data_store",
    "db": "data_store",
    "rds": "data_store",
    "aurora": "data_store",
    "dynamodb": "data_store",
    "dynamodb_table": "data_store",
    "cosmosdb": "data_store",
    "cosmos_db": "data_store",
    "sql": "data_store",
    "sql_database": "data_store",
    "redis": "data_store",
    "s3": "data_store",
    "storage": "data_store",
    "redshift": "data_store",
    "bigquery": "data_store",
    "event_hubs": "data_store",
    "pubsub": "data_store",
    "solr": "data_store",
    "elastic_file_system": "data_store",
    # ops
    "ops": "ops",
    "monitoring": "ops",
    "monitor": "ops",
    "cloudwatch": "ops",
    "prometheus": "ops",
    "grafana": "ops",
    "devops": "ops",
    "cicd": "ops",
    "ci_cd": "ops",
    "cloudformation": "ops",
    "cloudformation_template": "ops",
    "resource_groups": "ops",
    "resource_group": "ops",
    "backup": "ops",
    "cloud_trail": "ops",
    "auto_scaling": "ops",
    "autoscaling": "ops",
    "aws_cloud": "ops",
}


PROVIDER_TOKENS = {"aws", "amazon", "azure", "gcp", "google", "cloud", "microsoft"}


KEYWORD_TO_GENERIC: Dict[str, str] = {
    # gateway/network
    "api_gateway": "gateway",
    "gateway": "gateway",
    "ingress": "gateway",
    "load_balancer": "gateway",
    "application_gateway": "gateway",
    "traffic_manager": "gateway",
    "vpc": "gateway",
    "virtual_private_cloud": "gateway",
    "virtual_network": "gateway",
    "subnet": "gateway",
    "route_53": "gateway",
    "route53": "gateway",
    "cloudfront": "gateway",
    "dns": "gateway",
    "cdn": "gateway",
    # edge security
    "waf": "edge_security",
    "firewall": "edge_security",
    "security_group": "edge_security",
    "nsg": "edge_security",
    "shield": "edge_security",
    "ddos": "edge_security",
    "identity": "edge_security",
    "iam": "edge_security",
    "access_management": "edge_security",
    "vault": "edge_security",
    "secret": "edge_security",
    "entra": "edge_security",
    # data_store
    "sql": "data_store",
    "database": "data_store",
    "datastore": "data_store",
    "storage": "data_store",
    "bucket": "data_store",
    "queue": "data_store",
    "topic": "data_store",
    "kafka": "data_store",
    "redis": "data_store",
    "cache": "data_store",
    "dynamodb": "data_store",
    "cosmos": "data_store",
    "bigquery": "data_store",
    "redshift": "data_store",
    "event_hub": "data_store",
    "pubsub": "data_store",
    "elasticsearch": "data_store",
    "solr": "data_store",
    "file_system": "data_store",
    # compute
    "compute": "compute",
    "server": "compute",
    "instance": "compute",
    "function": "compute",
    "lambda": "compute",
    "kubernetes": "compute",
    "container": "compute",
    "service": "compute",
    "app_service": "compute",
    "databricks": "compute",
    "synapse": "compute",
    "data_factory": "compute",
    "data_factories": "compute",
    "machine_learning": "compute",
    "cloud_run": "compute",
    "openai": "compute",
    "vm": "compute",
    # ops
    "monitor": "ops",
    "monitoring": "ops",
    "devops": "ops",
    "cicd": "ops",
    "ci_cd": "ops",
    "prometheus": "ops",
    "grafana": "ops",
    "cloudwatch": "ops",
    "cloudformation": "ops",
    "resource_group": "ops",
    "backup": "ops",
    "auto_scaling": "ops",
    "autoscaling": "ops",
    "log": "ops",
    "alert": "ops",
    "trail": "ops",
    # user
    "user": "user",
    "client": "user",
    "consumer": "user",
    "admin": "user",
    "developer": "user",
    "portal": "user",
}

# Prioridade determinística quando há múltiplas palavras candidatas no label
GENERIC_PRIORITY = ["gateway", "edge_security", "data_store", "compute", "ops", "user"]


class ConversionError(RuntimeError):
    """Erro de conversão de um XML individual."""


def _normalize_label(raw: str) -> str:
    normalized = raw.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized)
    return normalized.strip("_")


def _tokenize(label: str) -> List[str]:
    tokens = [tok for tok in _normalize_label(label).split("_") if tok]
    return [tok for tok in tokens if tok not in PROVIDER_TOKENS]


def _map_label(raw_label: str, mapping: Dict[str, str]) -> Optional[str]:
    normalized = _normalize_label(raw_label)

    # 1) Mapeamento explícito (dicionário default + JSON opcional)
    direct = mapping.get(normalized)
    if direct is not None:
        return direct

    # 2) Tentativas com remoção de tokens de provider
    tokens = _tokenize(normalized)
    if not tokens:
        return None

    collapsed = "_".join(tokens)
    direct = mapping.get(collapsed)
    if direct is not None:
        return direct

    # 2.1) Singularização leve para reduzir variações no plural
    singular_tokens = [tok[:-1] if tok.endswith("s") and len(tok) > 3 else tok for tok in tokens]
    singular_collapsed = "_".join(singular_tokens)
    direct = mapping.get(singular_collapsed)
    if direct is not None:
        return direct

    # 3) Heurística por palavra-chave/substring com prioridade determinística
    hits: List[str] = []
    search_space = [collapsed, singular_collapsed] + tokens + singular_tokens
    for candidate, generic in KEYWORD_TO_GENERIC.items():
        for item in search_space:
            if candidate in item or item in candidate:
                hits.append(generic)
                break

    if not hits:
        return None

    for generic in GENERIC_PRIORITY:
        if generic in hits:
            return generic
    return hits[0]


def _load_mapping(mapping_path: Optional[Path]) -> Dict[str, str]:
    mapping = dict(DEFAULT_SERVICE_TO_GENERIC)
    if mapping_path is None:
        return mapping

    payload = json.loads(mapping_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("Arquivo de mapeamento deve conter um objeto JSON (dict)")

    for key, value in payload.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("Mapeamento inválido: chaves e valores devem ser strings")
        normalized_key = _normalize_label(key)
        normalized_value = _normalize_label(value)
        if normalized_value not in CLASS_TO_ID:
            allowed = ", ".join(CLASSES)
            raise ValueError(f"Classe alvo inválida '{value}'. Classes permitidas: {allowed}")
        mapping[normalized_key] = normalized_value

    return mapping


def _find_xmls(xml_root: Path) -> List[Path]:
    return sorted([path for path in xml_root.rglob("*") if path.is_file() and path.suffix.lower() == ".xml"])


def _local_name(tag: str) -> str:
    if "}" in tag:
        tag = tag.split("}", 1)[1]
    return tag.lower()


def _iter_elements_by_tag(root: ET.Element, tag: str) -> Iterable[ET.Element]:
    wanted = tag.lower()
    for node in root.iter():
        if _local_name(node.tag) == wanted:
            yield node


def _first_text_anywhere(node: ET.Element, tag: str) -> Optional[str]:
    for child in node.iter():
        if _local_name(child.tag) == tag.lower() and child.text:
            text = child.text.strip()
            if text:
                return text
    return None


def _parse_size(root: ET.Element) -> Tuple[int, int]:
    size_node = next(_iter_elements_by_tag(root, "size"), None)
    if size_node is None:
        raise ConversionError("XML sem nó <size>")

    width_text = _first_text_anywhere(size_node, "width")
    height_text = _first_text_anywhere(size_node, "height")
    if not width_text or not height_text:
        raise ConversionError("XML sem width/height em <size>")

    width = int(float(width_text))
    height = int(float(height_text))
    if width <= 0 or height <= 0:
        raise ConversionError(f"Dimensão inválida: width={width}, height={height}")
    return width, height


def _to_yolo_line(class_id: int, width: int, height: int, xmin: float, ymin: float, xmax: float, ymax: float) -> str:
    x_center = ((xmin + xmax) / 2.0) / width
    y_center = ((ymin + ymax) / 2.0) / height
    box_w = (xmax - xmin) / width
    box_h = (ymax - ymin) / height
    return f"{class_id} {x_center:.6f} {y_center:.6f} {box_w:.6f} {box_h:.6f}"


def _safe_bbox(width: int, height: int, xmin: float, ymin: float, xmax: float, ymax: float) -> Optional[Tuple[float, float, float, float]]:
    xmin = max(0.0, min(float(width), xmin))
    xmax = max(0.0, min(float(width), xmax))
    ymin = max(0.0, min(float(height), ymin))
    ymax = max(0.0, min(float(height), ymax))
    if xmax <= xmin or ymax <= ymin:
        return None
    return xmin, ymin, xmax, ymax


def _extract_bbox(obj: ET.Element) -> Optional[Tuple[float, float, float, float]]:
    bndbox = next(_iter_elements_by_tag(obj, "bndbox"), None)
    if bndbox is None:
        return None

    try:
        xmin = float(_first_text_anywhere(bndbox, "xmin") or "")
        ymin = float(_first_text_anywhere(bndbox, "ymin") or "")
        xmax = float(_first_text_anywhere(bndbox, "xmax") or "")
        ymax = float(_first_text_anywhere(bndbox, "ymax") or "")
    except ValueError:
        return None

    return xmin, ymin, xmax, ymax


def _convert_xml(
    xml_path: Path,
    xml_root: Path,
    mapping: Dict[str, str],
    labels_root: Path,
    default_class: Optional[str],
) -> Tuple[int, int, List[str], List[str]]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    width, height = _parse_size(root)

    yolo_lines: List[str] = []
    unknown_labels: List[str] = []
    skip_reasons: List[str] = []

    objects = list(_iter_elements_by_tag(root, "object"))
    total_objects = len(objects)

    for idx, obj in enumerate(objects, start=1):
        raw_name = _first_text_anywhere(obj, "name")
        if not raw_name:
            skip_reasons.append(f"obj#{idx}: sem <name>")
            continue

        mapped_label = _map_label(raw_name, mapping)
        if mapped_label is None and default_class is not None:
            mapped_label = default_class
        if mapped_label is None:
            unknown_labels.append(raw_name)
            skip_reasons.append(f"obj#{idx} '{raw_name}': sem mapeamento")
            continue

        bbox_raw = _extract_bbox(obj)
        if bbox_raw is None:
            skip_reasons.append(f"obj#{idx} '{raw_name}': bndbox ausente/inválido")
            continue

        bbox = _safe_bbox(width, height, *bbox_raw)
        if bbox is None:
            skip_reasons.append(f"obj#{idx} '{raw_name}': bndbox degenerado")
            continue

        class_id = CLASS_TO_ID[mapped_label]
        yolo_lines.append(_to_yolo_line(class_id, width, height, *bbox))

    relative_xml = xml_path.relative_to(xml_root)
    out_name = relative_xml.with_suffix(".txt").name
    out_dir = labels_root / relative_xml.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / out_name
    out_file.write_text("\n".join(yolo_lines) + ("\n" if yolo_lines else ""), encoding="utf-8")

    return len(yolo_lines), total_objects, unknown_labels, skip_reasons


def _scan_labels(xml_files: List[Path], mapping: Dict[str, str]) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int], int]:
    all_labels: Dict[str, int] = {}
    mapped_labels: Dict[str, int] = {}
    unmapped_labels: Dict[str, int] = {}
    total_objects = 0

    for xml_path in xml_files:
        root = ET.parse(xml_path).getroot()
        for obj in _iter_elements_by_tag(root, "object"):
            raw_name = _first_text_anywhere(obj, "name")
            if not raw_name:
                continue

            total_objects += 1
            all_labels[raw_name] = all_labels.get(raw_name, 0) + 1

            mapped = _map_label(raw_name, mapping)
            if mapped is None:
                unmapped_labels[raw_name] = unmapped_labels.get(raw_name, 0) + 1
            else:
                mapped_labels[mapped] = mapped_labels.get(mapped, 0) + 1

    return all_labels, mapped_labels, unmapped_labels, total_objects


def _print_scan_report(
    all_labels: Dict[str, int],
    mapped_labels: Dict[str, int],
    unmapped_labels: Dict[str, int],
    total_objects: int,
    xml_count: int,
) -> None:
    print(f"XMLs analisados: {xml_count}")
    print(f"Objetos anotados: {total_objects}")
    print(f"Rótulos distintos encontrados: {len(all_labels)}")

    if mapped_labels:
        print("\nCobertura por classe genérica (após mapeamento):")
        for label, count in sorted(mapped_labels.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {label}: {count}")

    print("\nRótulos brutos encontrados no XML:")
    for label, count in sorted(all_labels.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {label}: {count}")

    if unmapped_labels:
        print("\nRótulos SEM mapeamento (precisam entrar no mapping):")
        for label, count in sorted(unmapped_labels.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {label}: {count}")
    else:
        print("\nTodos os rótulos possuem mapeamento. ✅")


def main() -> None:
    parser = argparse.ArgumentParser(description="Converte anotações XML (Pascal VOC/LabelImg) para YOLO TXT")
    parser.add_argument("--xml-dir", type=Path, default=project_root / "data" / "xml", help="Pasta com arquivos XML")
    parser.add_argument("--labels-dir", type=Path, default=project_root / "data" / "labels" / "train", help="Pasta de saída dos TXT YOLO")
    parser.add_argument(
        "--mapping-json",
        type=Path,
        default=None,
        help="JSON opcional para sobrescrever/expandir mapeamento de nome_de_servico -> classe_generica",
    )
    parser.add_argument(
        "--scan-only",
        action="store_true",
        help="Somente analisa rótulos existentes nos XMLs e cobertura do mapeamento, sem gerar TXT",
    )
    parser.add_argument(
        "--default-class",
        type=str,
        default=None,
        help="Classe fallback para rótulos sem mapeamento (user, edge_security, gateway, compute, data_store, ops)",
    )
    parser.add_argument(
        "--fail-on-empty",
        action="store_true",
        help="Falha com exit code 2 se algum XML com objetos gerar 0 linhas YOLO.",
    )
    args = parser.parse_args()

    if args.default_class is not None:
        args.default_class = _normalize_label(args.default_class)
        if args.default_class not in CLASS_TO_ID:
            allowed = ", ".join(CLASSES)
            raise ValueError(f"Classe default inválida '{args.default_class}'. Classes permitidas: {allowed}")

    if not args.xml_dir.exists():
        raise FileNotFoundError(f"Pasta de XML não encontrada: {args.xml_dir}")

    mapping = _load_mapping(args.mapping_json)
    xml_files = _find_xmls(args.xml_dir)
    if not xml_files:
        print(f"Nenhum XML encontrado em {args.xml_dir}")
        return

    if args.scan_only:
        all_labels, mapped_labels, unmapped_labels, total_objects = _scan_labels(xml_files, mapping)
        _print_scan_report(all_labels, mapped_labels, unmapped_labels, total_objects, len(xml_files))
        return

    converted_objects = 0
    total_objects = 0
    unknown: Dict[str, int] = {}
    files_with_zero_output: List[Tuple[Path, List[str]]] = []

    for xml_path in xml_files:
        try:
            kept, total, unknown_labels, skip_reasons = _convert_xml(
                xml_path=xml_path,
                xml_root=args.xml_dir,
                mapping=mapping,
                labels_root=args.labels_dir,
                default_class=args.default_class,
            )
        except (ET.ParseError, ConversionError, ValueError) as exc:
            print(f"[ERRO] {xml_path}: {exc}")
            files_with_zero_output.append((xml_path, [str(exc)]))
            continue

        converted_objects += kept
        total_objects += total
        for label in unknown_labels:
            unknown[label] = unknown.get(label, 0) + 1

        if total > 0 and kept == 0:
            files_with_zero_output.append((xml_path, skip_reasons))

    print(f"XMLs processados: {len(xml_files)}")
    print(f"Objetos convertidos: {converted_objects}/{total_objects}")
    print(f"Arquivos com objetos mas saída vazia: {len(files_with_zero_output)}")
    print(f"Saída YOLO: {args.labels_dir}")

    if unknown:
        print("\nRótulos sem mapeamento:")
        for label, count in sorted(unknown.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {label}: {count}")

    if files_with_zero_output:
        print("\nDiagnóstico de XMLs com saída vazia:")
        for xml_path, reasons in files_with_zero_output:
            print(f"- {xml_path}:")
            if reasons:
                for reason in reasons[:20]:
                    print(f"  * {reason}")
                if len(reasons) > 20:
                    print(f"  * ... e mais {len(reasons) - 20} razão(ões)")
            else:
                print("  * sem motivo detalhado")

    if args.fail_on_empty and files_with_zero_output:
        sys.exit(2)


if __name__ == "__main__":
    main()
