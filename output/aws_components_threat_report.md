# Relatório de Modelagem de Ameaças (STRIDE)

- Gerado em: `2026-03-04T04:10:21.622729+00:00`
- Imagem de origem: `C:\Users\office\Documents\estudo\IA\FIAP\projetos\git\Hackaton\data\images\val\aws.png`
- Componentes analisados: **15**
- Componentes excluídos por priorização: **19**
- Estratégia de seleção: `confidence_x_risk`
- Associações analisadas: **9**

## Indicadores de qualidade
- Confianca média das detecções: **0.9498**
- Faixa de confiança (min..max): `0.9418 .. 0.9648`
- Proporção de baixa confiança (<0.1): `0.0`
- Tipos distintos detectados: **6**
- Distribuição por tipo: `{'compute': 1, 'data_store': 5, 'gateway': 6, 'edge_security': 1, 'ops': 1, 'user': 1}`

## Componente c13 (compute)
- Confiança: `0.9479`
- Risco estimado: `8.0`
- Prioridade (confiança x risco): `7.5832`

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

## Componente c7 (data_store)
- Confiança: `0.9526`
- Risco estimado: `7.0`
- Prioridade (confiança x risco): `6.6682`

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

## Componente c11 (data_store)
- Confiança: `0.9495`
- Risco estimado: `7.0`
- Prioridade (confiança x risco): `6.6465`

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

## Componente c15 (data_store)
- Confiança: `0.9461`
- Risco estimado: `7.0`
- Prioridade (confiança x risco): `6.6227`

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

## Componente c16 (data_store)
- Confiança: `0.9455`
- Risco estimado: `7.0`
- Prioridade (confiança x risco): `6.6185`

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

## Componente c18 (data_store)
- Confiança: `0.9449`
- Risco estimado: `7.0`
- Prioridade (confiança x risco): `6.6143`

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

## Componente c4 (gateway)
- Confiança: `0.9572`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `5.7432`

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

## Componente c9 (gateway)
- Confiança: `0.9501`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `5.7006`

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

## Componente c10 (gateway)
- Confiança: `0.9498`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `5.6988`

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

## Componente c17 (gateway)
- Confiança: `0.9454`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `5.6724`

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

## Componente c20 (gateway)
- Confiança: `0.9418`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `5.6508`

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

## Componente c21 (gateway)
- Confiança: `0.9418`
- Risco estimado: `6.0`
- Prioridade (confiança x risco): `5.6508`

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

## Componente c3 (edge_security)
- Confiança: `0.9598`
- Risco estimado: `4.0`
- Prioridade (confiança x risco): `3.8392`

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

## Componente c8 (ops)
- Confiança: `0.9504`
- Risco estimado: `4.0`
- Prioridade (confiança x risco): `3.8016`

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

## Componente c1 (user)
- Confiança: `0.9648`
- Risco estimado: `3.0`
- Prioridade (confiança x risco): `2.8944`

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

## Ameaças por associação entre componentes

### c1 (user) ↔ c21 (gateway)
- 1. [Spoofing] Sessão de usuário falsificada no acesso ao gateway: Ausência de autenticação forte e proteção de sessão pode permitir uso indevido de identidade.
- 2. [Tampering] Manipulação de parâmetros na entrada: Sem validação de payload e assinatura de requisições, parâmetros podem ser alterados em trânsito.

### c10 (gateway) ↔ c20 (gateway)
- 1. [Denial of Service] Amplificação de tráfego entre camadas de entrada: Sem controle de cota e backpressure, gateways encadeados podem saturar mutuamente.

### c10 (gateway) ↔ c21 (gateway)
- 1. [Denial of Service] Amplificação de tráfego entre camadas de entrada: Sem controle de cota e backpressure, gateways encadeados podem saturar mutuamente.

### c10 (gateway) ↔ c4 (gateway)
- 1. [Denial of Service] Amplificação de tráfego entre camadas de entrada: Sem controle de cota e backpressure, gateways encadeados podem saturar mutuamente.

### c10 (gateway) ↔ c9 (gateway)
- 1. [Denial of Service] Amplificação de tráfego entre camadas de entrada: Sem controle de cota e backpressure, gateways encadeados podem saturar mutuamente.

### c11 (data_store) ↔ c13 (compute)
- 1. [Information Disclosure] Exposição de dados na comunicação aplicação-banco: Conexões sem criptografia adequada ou com segredos fracos podem vazar dados sensíveis.
- 2. [Tampering] Manipulação de comandos de persistência: Sem sanitização e autorização contextual, operações de escrita podem adulterar dados.

### c13 (compute) ↔ c18 (data_store)
- 1. [Information Disclosure] Exposição de dados na comunicação aplicação-banco: Conexões sem criptografia adequada ou com segredos fracos podem vazar dados sensíveis.
- 2. [Tampering] Manipulação de comandos de persistência: Sem sanitização e autorização contextual, operações de escrita podem adulterar dados.

### c17 (gateway) ↔ c4 (gateway)
- 1. [Denial of Service] Amplificação de tráfego entre camadas de entrada: Sem controle de cota e backpressure, gateways encadeados podem saturar mutuamente.

### c20 (gateway) ↔ c9 (gateway)
- 1. [Denial of Service] Amplificação de tráfego entre camadas de entrada: Sem controle de cota e backpressure, gateways encadeados podem saturar mutuamente.
