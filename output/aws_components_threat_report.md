# Relatório de Modelagem de Ameaças (STRIDE)

- Gerado em: `2026-03-01T21:47:56.632368+00:00`
- Imagem de origem: `C:\Users\office\Documents\estudo\IA\FIAP\projetos\git\Hackaton\data\images\val\aws.png`
- Componentes analisados: **15**
- Componentes excluídos por priorização: **91**
- Estratégia de seleção: `confidence_x_risk`
- Associações analisadas: **0**

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Tampering] Alteração não autorizada de artefatos
- Descrição: Deploy sem integridade pode permitir execução de binário adulterado.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF
