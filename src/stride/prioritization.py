"""Priorização de componentes para reduzir ruído visual e analítico."""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Tuple

from src.stride.rules import threats_for_component

CATEGORY_WEIGHTS: Dict[str, float] = {
    "Elevation of Privilege": 3.0,
    "Information Disclosure": 3.0,
    "Tampering": 2.0,
    "Spoofing": 2.0,
    "Denial of Service": 2.0,
    "Repudiation": 1.0,
}


def component_risk_score(component_type: str) -> float:
    threats = threats_for_component(component_type)
    if not threats:
        return 0.5
    return sum(CATEGORY_WEIGHTS.get(t.category, 1.0) for t in threats)


def prioritize_components(
    components: List[Dict],
    *,
    max_components: int = 15,
    min_confidence: float = 0.0,
    min_per_type: int = 1,
) -> Tuple[List[Dict], List[Dict]]:
    """Seleciona componentes por confiança + risco, preservando diversidade de tipos.

    Retorna (selecionados, descartados), ambos ordenados por score decrescente.
    """
    scored: List[Dict] = []
    for comp in components:
        confidence = float(comp.get("confidence") or 0.0)
        if confidence < min_confidence:
            continue

        risk_score = component_risk_score(comp.get("type", "unknown"))
        priority_score = confidence * risk_score
        scored.append(
            {
                **comp,
                "risk_score": round(risk_score, 3),
                "priority_score": round(priority_score, 4),
            }
        )

    scored.sort(key=lambda c: (c["priority_score"], c.get("confidence", 0)), reverse=True)
    if not scored and components:
        for comp in components:
            confidence = float(comp.get("confidence") or 0.0)
            risk_score = component_risk_score(comp.get("type", "unknown"))
            scored.append(
                {
                    **comp,
                    "risk_score": round(risk_score, 3),
                    "priority_score": round(confidence * risk_score, 4),
                }
            )
        scored.sort(key=lambda c: c.get("confidence", 0), reverse=True)

    selected: List[Dict] = []
    used_ids = set()
    by_type: Dict[str, List[Dict]] = defaultdict(list)
    for comp in scored:
        by_type[comp.get("type", "unknown")].append(comp)

    for comp_type in sorted(by_type):
        for candidate in by_type[comp_type][:min_per_type]:
            if len(selected) >= max_components:
                break
            selected.append(candidate)
            used_ids.add(candidate.get("id"))

    if len(selected) < max_components:
        for comp in scored:
            if comp.get("id") in used_ids:
                continue
            selected.append(comp)
            used_ids.add(comp.get("id"))
            if len(selected) >= max_components:
                break

    dropped = [comp for comp in scored if comp.get("id") not in used_ids]
    selected.sort(key=lambda c: (c["priority_score"], c.get("confidence", 0)), reverse=True)
    dropped.sort(key=lambda c: (c["priority_score"], c.get("confidence", 0)), reverse=True)
    return selected, dropped
