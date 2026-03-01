"""Regras de mapeamento STRIDE para componentes detectados no diagrama."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class ThreatTemplate:
    category: str
    title: str
    description: str


# Regras base do MVP: componente -> ameaças STRIDE prováveis.
COMPONENT_STRIDE_RULES: Dict[str, List[ThreatTemplate]] = {
    "user": [
        ThreatTemplate("Spoofing", "Impersonação de usuário", "Credenciais fracas ou sessão exposta podem permitir se passar por usuário legítimo."),
        ThreatTemplate("Repudiation", "Negação de ações", "Sem trilha de auditoria confiável, o usuário pode negar operações realizadas."),
    ],
    "edge_security": [
        ThreatTemplate("Tampering", "Manipulação de regras de borda", "Mudanças indevidas em WAF/Firewall podem abrir caminho para ataques."),
        ThreatTemplate("Denial of Service", "Saturação de borda", "Ataques volumétricos podem degradar ou indisponibilizar proteção de entrada."),
    ],
    "gateway": [
        ThreatTemplate("Spoofing", "Falsificação de cliente no gateway", "Tokens/chaves expostas podem permitir chamadas não autorizadas à API."),
        ThreatTemplate("Tampering", "Manipulação de payload em trânsito", "Falta de validação de input no gateway permite alteração maliciosa de dados."),
        ThreatTemplate("Denial of Service", "Exaustão do gateway", "Sem rate limiting adequado, requisições massivas derrubam o serviço."),
    ],
    "compute": [
        ThreatTemplate("Elevation of Privilege", "Escalada de privilégio em workload", "Configurações permissivas permitem que código acesse recursos além do necessário."),
        ThreatTemplate("Information Disclosure", "Vazamento de segredos em execução", "Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis."),
        ThreatTemplate("Tampering", "Alteração não autorizada de artefatos", "Deploy sem integridade pode permitir execução de binário adulterado."),
    ],
    "data_store": [
        ThreatTemplate("Information Disclosure", "Exposição de dados sensíveis", "Controles de acesso ou criptografia inadequados expõem dados em repouso."),
        ThreatTemplate("Tampering", "Corrupção de dados", "Falta de validação e trilha de alterações permite alteração indevida de registros."),
        ThreatTemplate("Denial of Service", "Indisponibilidade de banco", "Consultas pesadas/abusivas podem degradar severamente o datastore."),
    ],
    "ops": [
        ThreatTemplate("Repudiation", "Lacunas de auditoria operacional", "Sem logging centralizado e íntegro, ações administrativas ficam sem rastreio."),
        ThreatTemplate("Elevation of Privilege", "Abuso de privilégios administrativos", "Papéis excessivos em operações podem levar a controle indevido do ambiente."),
    ],
}


def threats_for_component(component_type: str) -> List[ThreatTemplate]:
    """Retorna ameaças STRIDE aplicáveis ao tipo de componente.

    Caso não exista mapeamento específico, retorna lista vazia.
    """
    return COMPONENT_STRIDE_RULES.get(component_type, [])
