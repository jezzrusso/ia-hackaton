# Relatório de Modelagem de Ameaças (STRIDE)

- Gerado em: `2026-03-03T02:18:28.893750+00:00`
- Imagem de origem: `C:\Users\office\Documents\estudo\IA\FIAP\projetos\git\Hackaton\data\images\train\azure.png`
- Componentes analisados: **15**
- Componentes excluídos por priorização: **79**
- Estratégia de seleção: `confidence_x_risk`
- Associações analisadas: **13**

## Indicadores de qualidade
- Confianca média das detecções: **0.0039**
- Faixa de confiança (min..max): `0.0024 .. 0.0068`
- Proporção de baixa confiança (<0.1): `1.0`
- Tipos distintos detectados: **6**
- Distribuição por tipo: `{'compute': 10, 'data_store': 1, 'gateway': 1, 'user': 1, 'edge_security': 1, 'ops': 1}`

## Alertas de confiabilidade
- ⚠️ Confianca media baixa nas deteccoes; revisar dataset, anotacoes e hiperparametros do detector.

## Componente c1 (compute)
- Confiança: `0.0068`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0544`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c2 (compute)
- Confiança: `0.0065`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.052`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c3 (compute)
- Confiança: `0.006`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.048`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c4 (compute)
- Confiança: `0.0053`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0424`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c5 (compute)
- Confiança: `0.0043`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0344`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c7 (compute)
- Confiança: `0.0037`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0296`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c8 (compute)
- Confiança: `0.0036`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0288`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c12 (compute)
- Confiança: `0.003`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.024`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c13 (compute)
- Confiança: `0.0029`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0232`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c14 (compute)
- Confiança: `0.0029`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0232`

### 1. [Elevation of Privilege] Escalada de privilégio em workload
- Descrição: Configurações permissivas permitem que código acesse recursos além do necessário.
- Vulnerabilidade associada: Papéis IAM superpermissivos e execução com privilégios elevados.
- Contramedidas:
  - Aplicar princípio do menor privilégio em identidades de workload.
  - Segregar funções e contas por ambiente.
  - Monitorar e revisar grants de privilégio periodicamente.
- Referências: CIS Benchmarks, NIST 800-53 AC-6

### 2. [Information Disclosure] Vazamento de segredos em execução
- Descrição: Variáveis, logs ou artefatos podem expor credenciais e dados sensíveis.
- Vulnerabilidade associada: Exposição de segredos em variáveis de ambiente, logs e imagens de container.
- Contramedidas:
  - Usar secret manager com rotação automática e acesso por identidade de workload.
  - Sanitizar logs para remover dados sensíveis e bloquear debug em produção.
  - Assinar e escanear imagens para evitar artefatos com credenciais embutidas.
- Referências: OWASP Secrets Management, NIST SP 800-57

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Pipeline de build/deploy sem verificação de integridade e proveniência.
- Contramedidas:
  - Implementar assinatura de artefatos (ex.: Sigstore/cosign) e política de verificação em runtime.
  - Restringir permissão de escrita em repositórios e registries com aprovação obrigatória.
  - Executar verificação de integridade e rollback automático em caso de drift.
- Referências: SLSA, NIST SSDF

## Componente c33 (data_store)
- Confiança: `0.0025`
- Risco estimado: `7.0`
- Prioridade (confiança x risco): `0.0175`

### 1. [Information Disclosure] Exposição de dados sensíveis
- Descrição: Controles de acesso ou criptografia inadequados expõem dados em repouso.
- Vulnerabilidade associada: Dados sem criptografia forte e políticas frágeis de acesso.
- Contramedidas:
  - Criptografar dados em repouso e em trânsito.
  - Restringir acesso por rede/identidade e auditar consultas sensíveis.
  - Aplicar mascaramento/tokenização para dados críticos.
- Referências: OWASP Top 10 A02, ISO 27001 Annex A

### 2. [Tampering] Corrupção de dados
- Descrição: Falta de validação e trilha de alterações permite alteração indevida de registros.
- Vulnerabilidade associada: Ausência de trilha de auditoria imutável e controles fracos de alteração de dados.
- Contramedidas:
  - Habilitar trilha de auditoria com retenção e proteção contra alteração.
  - Aplicar controles de integridade transacional e validação de entradas no app.
  - Separar contas de leitura/escrita e exigir aprovação para mudanças estruturais.
- Referências: CIS Database Benchmarks, NIST 800-53 AU

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c18 (gateway)
- Confiança: `0.0028`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `0.0168`

### 1. [Spoofing] Falsificação de cliente no gateway
- Descrição: Tokens/chaves expostas podem permitir chamadas não autorizadas à API.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 2. [Tampering] Manipulação de payload em trânsito
- Descrição: Falta de validação de input no gateway permite alteração maliciosa de dados.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Exaustão do gateway
- Descrição: Sem rate limiting adequado, requisições massivas derrubam o serviço.
- Vulnerabilidade associada: Ausência de limitação de taxa e controles de burst na entrada.
- Contramedidas:
  - Configurar rate limit e quotas por cliente/chave.
  - Aplicar circuit breaker e timeout defensivo.
  - Habilitar proteção anti-DDoS do provedor cloud.
- Referências: OWASP API Security, NIST CSF PR.PT

## Componente c6 (user)
- Confiança: `0.0039`
- Risco estimado: `3.0`
- Prioridade (confiança x risco): `0.0117`

### 1. [Spoofing] Impersonação de usuário
- Descrição: Credenciais fracas ou sessão exposta podem permitir se passar por usuário legítimo.
- Vulnerabilidade associada: Autenticação fraca, ausência de MFA e reutilização de credenciais.
- Contramedidas:
  - Habilitar MFA para acessos críticos.
  - Aplicar política de senha forte e proteção contra brute force.
  - Adotar gerenciamento de sessão com expiração e rotação de token.
- Referências: OWASP ASVS V2, NIST SP 800-63

### 2. [Repudiation] Negação de ações
- Descrição: Sem trilha de auditoria confiável, o usuário pode negar operações realizadas.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c21 (edge_security)
- Confiança: `0.0026`
- Risco estimado: `4.0`
- Prioridade (confiança x risco): `0.0104`

### 1. [Tampering] Manipulação de regras de borda
- Descrição: Mudanças indevidas em WAF/Firewall podem abrir caminho para ataques.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 2. [Denial of Service] Saturação de borda
- Descrição: Ataques volumétricos podem degradar ou indisponibilizar proteção de entrada.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c50 (ops)
- Confiança: `0.0024`
- Risco estimado: `4.0`
- Prioridade (confiança x risco): `0.0096`

### 1. [Repudiation] Lacunas de auditoria operacional
- Descrição: Sem logging centralizado e íntegro, ações administrativas ficam sem rastreio.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 2. [Elevation of Privilege] Abuso de privilégios administrativos
- Descrição: Papéis excessivos em operações podem levar a controle indevido do ambiente.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Ameaças por associação entre componentes

### c1 (compute) ↔ c13 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c1 (compute) ↔ c3 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c12 (compute) ↔ c3 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c12 (compute) ↔ c4 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c13 (compute) ↔ c3 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c14 (compute) ↔ c18 (gateway)
- 1. [Elevation of Privilege] Escalada de privilégios via integração API-serviço: Políticas permissivas entre gateway e serviço podem ampliar escopo de execução além do necessário.
- 2. [Denial of Service] Saturação da camada de serviço por rajadas aceitas no gateway: Sem proteção de cota ponta a ponta, picos de tráfego podem exaurir o backend.

### c14 (compute) ↔ c7 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c18 (gateway) ↔ c7 (compute)
- 1. [Elevation of Privilege] Escalada de privilégios via integração API-serviço: Políticas permissivas entre gateway e serviço podem ampliar escopo de execução além do necessário.
- 2. [Denial of Service] Saturação da camada de serviço por rajadas aceitas no gateway: Sem proteção de cota ponta a ponta, picos de tráfego podem exaurir o backend.

### c18 (gateway) ↔ c8 (compute)
- 1. [Elevation of Privilege] Escalada de privilégios via integração API-serviço: Políticas permissivas entre gateway e serviço podem ampliar escopo de execução além do necessário.
- 2. [Denial of Service] Saturação da camada de serviço por rajadas aceitas no gateway: Sem proteção de cota ponta a ponta, picos de tráfego podem exaurir o backend.

### c2 (compute) ↔ c33 (data_store)
- 1. [Information Disclosure] Exposição de dados na comunicação aplicação-banco: Conexões sem criptografia adequada ou com segredos fracos podem vazar dados sensíveis.
- 2. [Tampering] Manipulação de comandos de persistência: Sem sanitização e autorização contextual, operações de escrita podem adulterar dados.

### c3 (compute) ↔ c4 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c33 (data_store) ↔ c7 (compute)
- 1. [Information Disclosure] Exposição de dados na comunicação aplicação-banco: Conexões sem criptografia adequada ou com segredos fracos podem vazar dados sensíveis.
- 2. [Tampering] Manipulação de comandos de persistência: Sem sanitização e autorização contextual, operações de escrita podem adulterar dados.

### c50 (ops) ↔ c8 (compute)
- 1. [Repudiation] Ações administrativas sem rastreabilidade: Mudanças operacionais sem trilha imutável dificultam atribuição e auditoria.
