"""Base de conhecimento MVP: ameaça STRIDE -> vulnerabilidades e contramedidas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class KnowledgeItem:
    vulnerability: str
    countermeasures: Tuple[str, ...]
    references: Tuple[str, ...]


KB: Dict[Tuple[str, str], KnowledgeItem] = {
    ("user", "Spoofing"): KnowledgeItem(
        vulnerability="Autenticação fraca, ausência de MFA e reutilização de credenciais.",
        countermeasures=(
            "Habilitar MFA para acessos críticos.",
            "Aplicar política de senha forte e proteção contra brute force.",
            "Adotar gerenciamento de sessão com expiração e rotação de token.",
        ),
        references=("OWASP ASVS V2", "NIST SP 800-63"),
    ),
    ("gateway", "Denial of Service"): KnowledgeItem(
        vulnerability="Ausência de limitação de taxa e controles de burst na entrada.",
        countermeasures=(
            "Configurar rate limit e quotas por cliente/chave.",
            "Aplicar circuit breaker e timeout defensivo.",
            "Habilitar proteção anti-DDoS do provedor cloud.",
        ),
        references=("OWASP API Security", "NIST CSF PR.PT"),
    ),
    ("compute", "Elevation of Privilege"): KnowledgeItem(
        vulnerability="Papéis IAM superpermissivos e execução com privilégios elevados.",
        countermeasures=(
            "Aplicar princípio do menor privilégio em identidades de workload.",
            "Segregar funções e contas por ambiente.",
            "Monitorar e revisar grants de privilégio periodicamente.",
        ),
        references=("CIS Benchmarks", "NIST 800-53 AC-6"),
    ),
    ("compute", "Information Disclosure"): KnowledgeItem(
        vulnerability="Exposição de segredos em variáveis de ambiente, logs e imagens de container.",
        countermeasures=(
            "Usar secret manager com rotação automática e acesso por identidade de workload.",
            "Sanitizar logs para remover dados sensíveis e bloquear debug em produção.",
            "Assinar e escanear imagens para evitar artefatos com credenciais embutidas.",
        ),
        references=("OWASP Secrets Management", "NIST SP 800-57"),
    ),
    ("compute", "Tampering"): KnowledgeItem(
        vulnerability="Pipeline de build/deploy sem verificação de integridade e proveniência.",
        countermeasures=(
            "Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.",
            "Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.",
            "Executar verificação de integridade e rollback automático em caso de drift.",
        ),
        references=("SLSA", "NIST SSDF"),
    ),
    ("data_store", "Information Disclosure"): KnowledgeItem(
        vulnerability="Dados sem criptografia forte e políticas frágeis de acesso.",
        countermeasures=(
            "Criptografar dados em repouso e em trânsito.",
            "Restringir acesso por rede/identidade e auditar consultas sensíveis.",
            "Aplicar mascaramento/tokenização para dados críticos.",
        ),
        references=("OWASP Top 10 A02", "ISO 27001 Annex A"),
    ),
    ("data_store", "Tampering"): KnowledgeItem(
        vulnerability="Ausência de trilha de auditoria imutável e controles fracos de alteração de dados.",
        countermeasures=(
            "Habilitar trilha de auditoria com retenção e proteção contra alteração.",
            "Aplicar controles de integridade transacional e validação de entradas no app.",
            "Separar contas de leitura/escrita e exigir aprovação para mudanças estruturais.",
        ),
        references=("CIS Database Benchmarks", "NIST 800-53 AU"),
    ),
}


def lookup(component_type: str, stride_category: str) -> KnowledgeItem:
    """Retorna item específico da KB ou fallback genérico para o par informado."""
    default = KnowledgeItem(
        vulnerability="Configuração insegura ou ausência de controles específicos para a ameaça.",
        countermeasures=(
            "Definir baseline de segurança para o componente.",
            "Ativar monitoramento e alertas com resposta a incidentes.",
            "Executar testes contínuos de segurança (SAST/DAST/config).",
        ),
        references=("OWASP", "NIST CSF"),
    )
    return KB.get((component_type, stride_category), default)
