"""Regras STRIDE focadas em interações entre componentes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class InteractionThreatTemplate:
    category: str
    title: str
    description: str


INTERACTION_STRIDE_RULES: Dict[Tuple[str, str], List[InteractionThreatTemplate]] = {
    ("gateway", "user"): [
        InteractionThreatTemplate(
            "Spoofing",
            "Sessão de usuário falsificada no acesso ao gateway",
            "Ausência de autenticação forte e proteção de sessão pode permitir uso indevido de identidade.",
        ),
        InteractionThreatTemplate(
            "Tampering",
            "Manipulação de parâmetros na entrada",
            "Sem validação de payload e assinatura de requisições, parâmetros podem ser alterados em trânsito.",
        ),
    ],
    ("compute", "gateway"): [
        InteractionThreatTemplate(
            "Elevation of Privilege",
            "Escalada de privilégios via integração API-serviço",
            "Políticas permissivas entre gateway e serviço podem ampliar escopo de execução além do necessário.",
        ),
        InteractionThreatTemplate(
            "Denial of Service",
            "Saturação da camada de serviço por rajadas aceitas no gateway",
            "Sem proteção de cota ponta a ponta, picos de tráfego podem exaurir o backend.",
        ),
    ],
    ("compute", "data_store"): [
        InteractionThreatTemplate(
            "Information Disclosure",
            "Exposição de dados na comunicação aplicação-banco",
            "Conexões sem criptografia adequada ou com segredos fracos podem vazar dados sensíveis.",
        ),
        InteractionThreatTemplate(
            "Tampering",
            "Manipulação de comandos de persistência",
            "Sem sanitização e autorização contextual, operações de escrita podem adulterar dados.",
        ),
    ],
    ("compute", "ops"): [
        InteractionThreatTemplate(
            "Repudiation",
            "Ações administrativas sem rastreabilidade",
            "Mudanças operacionais sem trilha imutável dificultam atribuição e auditoria.",
        ),
    ],
}


def threats_for_interaction(source_type: str, target_type: str) -> List[InteractionThreatTemplate]:
    """Retorna ameaças STRIDE para uma interação entre dois tipos.

    A consulta é normalizada para ser simétrica entre origem/destino.
    """
    pair = tuple(sorted((source_type, target_type)))
    return INTERACTION_STRIDE_RULES.get(pair, [])
