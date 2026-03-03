# Relatório de Modelagem de Ameaças (STRIDE)

- Gerado em: `2026-03-03T02:13:03.850425+00:00`
- Imagem de origem: `C:\Users\office\Documents\estudo\IA\FIAP\projetos\git\Hackaton\data\images\val\aws.png`
- Componentes analisados: **15**
- Componentes excluídos por priorização: **91**
- Estratégia de seleção: `confidence_x_risk`
- Associações analisadas: **18**

## Indicadores de qualidade
- Confianca média das detecções: **0.0039**
- Faixa de confiança (min..max): `0.0024 .. 0.0099`
- Proporção de baixa confiança (<0.1): `1.0`
- Tipos distintos detectados: **1**
- Distribuição por tipo: `{'compute': 15}`

## Alertas de confiabilidade
- ⚠️ Confianca media baixa nas deteccoes; revisar dataset, anotacoes e hiperparametros do detector.
- ⚠️ Baixa diversidade de tipos detectados; resultado pode estar enviesado para uma classe dominante.

## Componente c1 (compute)
- Confiança: `0.0099`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0792`

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
- Confiança: `0.0063`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0504`

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

## Componente c4 (compute)
- Confiança: `0.0044`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0352`

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
- Confiança: `0.0038`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0304`

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

## Componente c9 (compute)
- Confiança: `0.0034`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0272`

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

## Componente c11 (compute)
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
- Confiança: `0.0028`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0224`

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

## Componente c24 (compute)
- Confiança: `0.0026`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0208`

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

## Componente c28 (compute)
- Confiança: `0.0025`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.02`

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

## Componente c38 (compute)
- Confiança: `0.0024`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0192`

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

## Componente c40 (compute)
- Confiança: `0.0024`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0192`

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

## Componente c51 (compute)
- Confiança: `0.0024`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `0.0192`

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

## Ameaças por associação entre componentes

### c1 (compute) ↔ c24 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c1 (compute) ↔ c5 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c1 (compute) ↔ c8 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c11 (compute) ↔ c3 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c11 (compute) ↔ c4 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c13 (compute) ↔ c2 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c13 (compute) ↔ c40 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c13 (compute) ↔ c9 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c2 (compute) ↔ c28 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c2 (compute) ↔ c4 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c24 (compute) ↔ c3 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c24 (compute) ↔ c8 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c28 (compute) ↔ c7 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c3 (compute) ↔ c7 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c38 (compute) ↔ c40 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c38 (compute) ↔ c9 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c5 (compute) ↔ c51 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.

### c51 (compute) ↔ c7 (compute)
- 1. [Tampering] Movimentação lateral entre workloads: Comunicação interna sem controles de segmentação permite alteração indevida entre serviços.
- 2. [Denial of Service] Contenção de recursos entre serviços: Ausência de isolamento de recursos pode causar indisponibilidade em cascata entre workloads.
