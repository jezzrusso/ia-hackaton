"""Base de conhecimento MVP: ameaça STRIDE -> vulnerabilidades e contramedidas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class KnowledgeItem:
    vulnerability: str
    countermeasures: Tuple[str, ...]
    references: Tuple[str, ...]


KB: Dict[Tuple[str, str], KnowledgeItem] = {
    # user
    ("user", "Spoofing"): KnowledgeItem(
        vulnerability="Autenticação fraca, ausência de MFA e reutilização de credenciais.",
        countermeasures=(
            "Habilitar MFA para acessos críticos.",
            "Aplicar política de senha forte e proteção contra brute force.",
            "Adotar gerenciamento de sessão com expiração e rotação de token.",
        ),
        references=("OWASP ASVS V2", "NIST SP 800-63"),
    ),
    ("user", "Repudiation"): KnowledgeItem(
        vulnerability="Ações de usuário sem trilha auditável e sem não-repúdio em operações críticas.",
        countermeasures=(
            "Registrar trilhas de auditoria com identificador de usuário, horário e contexto da ação.",
            "Proteger logs com retenção, imutabilidade e controle de acesso.",
            "Aplicar assinaturas/recibos eletrônicos em operações de alto impacto.",
        ),
        references=("NIST 800-53 AU", "ISO 27001 A.12.4"),
    ),
    # edge_security
    ("edge_security", "Tampering"): KnowledgeItem(
        vulnerability="Mudanças não autorizadas em políticas de WAF/firewall e regras de borda.",
        countermeasures=(
            "Aplicar controle de mudanças com revisão por pares e trilha de aprovação.",
            "Versionar políticas de borda e executar validação automática antes de publicar.",
            "Ativar alertas em tempo real para alterações de regras críticas.",
        ),
        references=("CIS Controls 4/8", "NIST 800-53 CM"),
    ),
    ("edge_security", "Denial of Service"): KnowledgeItem(
        vulnerability="Capacidade insuficiente de absorver picos e ataques volumétricos na camada de borda.",
        countermeasures=(
            "Habilitar mitigação DDoS gerenciada e autoscaling na borda.",
            "Aplicar rate limiting, bot management e desafios progressivos.",
            "Configurar failover multi-região para serviços expostos.",
        ),
        references=("NIST CSF PR.PT", "OWASP ASVS V1"),
    ),
    # gateway
    ("gateway", "Spoofing"): KnowledgeItem(
        vulnerability="Chaves/tokens de cliente expostos ou sem validação robusta no gateway.",
        countermeasures=(
            "Exigir autenticação forte (OAuth2/OIDC, mTLS ou assinatura de requisição).",
            "Rotacionar credenciais e bloquear tokens comprometidos rapidamente.",
            "Validar issuer, audience e expiração de tokens em todas as rotas.",
        ),
        references=("OWASP API Security", "NIST 800-63"),
    ),
    ("gateway", "Tampering"): KnowledgeItem(
        vulnerability="Payload e parâmetros manipuláveis em trânsito por validação insuficiente no gateway.",
        countermeasures=(
            "Implementar validação de schema e sanitização de entrada no edge/gateway.",
            "Aplicar assinatura de payload para integrações sensíveis.",
            "Restringir métodos, cabeçalhos e tamanhos de requisição por rota.",
        ),
        references=("OWASP API Security", "NIST 800-53 SI"),
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
    # compute
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
    # data_store
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
    ("data_store", "Denial of Service"): KnowledgeItem(
        vulnerability="Consultas abusivas e contenção de recursos degradam disponibilidade de banco e filas.",
        countermeasures=(
            "Aplicar governança de queries (timeouts, limites de concorrência e índices adequados).",
            "Separar workloads OLTP/analytics e usar réplicas para leitura intensa.",
            "Configurar autoscaling, alertas de capacidade e planos de contingência.",
        ),
        references=("CIS Database Benchmarks", "NIST 800-53 SC"),
    ),
    # ops
    ("ops", "Repudiation"): KnowledgeItem(
        vulnerability="Ações administrativas sem trilha centralizada e íntegra em plataformas operacionais.",
        countermeasures=(
            "Centralizar logs administrativos e eventos de auditoria com retenção adequada.",
            "Habilitar trilhas imutáveis para ações privilegiadas e mudanças de configuração.",
            "Exigir identidade individual e proibir contas compartilhadas em operações.",
        ),
        references=("NIST 800-53 AU", "ISO 27001 A.12.4"),
    ),
    ("ops", "Elevation of Privilege"): KnowledgeItem(
        vulnerability="Privilégios excessivos em ferramentas de operação e CI/CD permitem abuso administrativo.",
        countermeasures=(
            "Aplicar RBAC com segregação de funções e aprovação em ações críticas.",
            "Impor acesso just-in-time para tarefas privilegiadas.",
            "Revisar periodicamente permissões e remover acessos órfãos.",
        ),
        references=("NIST 800-53 AC-6", "CIS Controls 6"),
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
