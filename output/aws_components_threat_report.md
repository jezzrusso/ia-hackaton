# Relatório de Modelagem de Ameaças (STRIDE)

- Gerado em: `2026-03-01T20:19:32.964990+00:00`
- Imagem de origem: `C:\Users\office\Documents\estudo\IA\FIAP\projetos\git\Hackaton\data\images\train\aws.png`
- Componentes analisados: **94**

## Componente c1 (compute)
- Confiança: `0.0068`

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
- Confiança: `0.0065`

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
- Confiança: `0.006`

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
- Confiança: `0.0053`

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
- Confiança: `0.0043`

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

## Componente c6 (user)
- Confiança: `0.0039`

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

## Componente c7 (compute)
- Confiança: `0.0037`

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

## Componente c9 (user)
- Confiança: `0.0033`

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

## Componente c10 (user)
- Confiança: `0.0032`

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

## Componente c11 (user)
- Confiança: `0.0031`

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

## Componente c12 (compute)
- Confiança: `0.003`

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
- Confiança: `0.0029`

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

## Componente c14 (compute)
- Confiança: `0.0029`

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

## Componente c15 (user)
- Confiança: `0.0028`

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

## Componente c16 (user)
- Confiança: `0.0028`

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

## Componente c17 (user)
- Confiança: `0.0028`

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

## Componente c18 (gateway)
- Confiança: `0.0028`

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

## Componente c19 (compute)
- Confiança: `0.0027`

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

## Componente c20 (compute)
- Confiança: `0.0027`

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

## Componente c21 (edge_security)
- Confiança: `0.0026`

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

## Componente c22 (user)
- Confiança: `0.0026`

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

## Componente c23 (compute)
- Confiança: `0.0026`

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

## Componente c24 (user)
- Confiança: `0.0026`

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

## Componente c25 (edge_security)
- Confiança: `0.0025`

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

## Componente c26 (edge_security)
- Confiança: `0.0025`

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

## Componente c27 (edge_security)
- Confiança: `0.0025`

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

## Componente c28 (edge_security)
- Confiança: `0.0025`

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

## Componente c29 (user)
- Confiança: `0.0025`

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

## Componente c30 (edge_security)
- Confiança: `0.0025`

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

## Componente c31 (gateway)
- Confiança: `0.0025`

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

## Componente c32 (edge_security)
- Confiança: `0.0025`

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

## Componente c33 (data_store)
- Confiança: `0.0025`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c34 (user)
- Confiança: `0.0025`

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

## Componente c35 (data_store)
- Confiança: `0.0025`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c36 (edge_security)
- Confiança: `0.0025`

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

## Componente c37 (edge_security)
- Confiança: `0.0025`

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

## Componente c38 (data_store)
- Confiança: `0.0025`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c39 (data_store)
- Confiança: `0.0025`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c40 (edge_security)
- Confiança: `0.0024`

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

## Componente c41 (edge_security)
- Confiança: `0.0024`

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

## Componente c42 (user)
- Confiança: `0.0024`

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

## Componente c43 (edge_security)
- Confiança: `0.0024`

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

## Componente c44 (data_store)
- Confiança: `0.0024`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c45 (edge_security)
- Confiança: `0.0024`

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

## Componente c46 (user)
- Confiança: `0.0024`

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

## Componente c47 (edge_security)
- Confiança: `0.0024`

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

## Componente c48 (data_store)
- Confiança: `0.0024`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c49 (compute)
- Confiança: `0.0024`

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

## Componente c50 (ops)
- Confiança: `0.0024`

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

## Componente c51 (ops)
- Confiança: `0.0024`

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

## Componente c52 (gateway)
- Confiança: `0.0024`

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

## Componente c53 (gateway)
- Confiança: `0.0024`

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

## Componente c54 (edge_security)
- Confiança: `0.0024`

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

## Componente c55 (ops)
- Confiança: `0.0024`

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

## Componente c56 (edge_security)
- Confiança: `0.0023`

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

## Componente c57 (user)
- Confiança: `0.0023`

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

## Componente c58 (edge_security)
- Confiança: `0.0023`

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

## Componente c59 (data_store)
- Confiança: `0.0023`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c60 (edge_security)
- Confiança: `0.0023`

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

## Componente c61 (edge_security)
- Confiança: `0.0023`

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

## Componente c62 (ops)
- Confiança: `0.0023`

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

## Componente c63 (edge_security)
- Confiança: `0.0023`

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

## Componente c64 (user)
- Confiança: `0.0023`

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

## Componente c65 (user)
- Confiança: `0.0023`

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

## Componente c66 (edge_security)
- Confiança: `0.0023`

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

## Componente c67 (user)
- Confiança: `0.0023`

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

## Componente c68 (gateway)
- Confiança: `0.0023`

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

## Componente c69 (gateway)
- Confiança: `0.0023`

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

## Componente c70 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c71 (edge_security)
- Confiança: `0.0022`

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

## Componente c72 (user)
- Confiança: `0.0022`

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

## Componente c73 (edge_security)
- Confiança: `0.0022`

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

## Componente c74 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c75 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c76 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c77 (edge_security)
- Confiança: `0.0022`

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

## Componente c78 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c79 (edge_security)
- Confiança: `0.0022`

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

## Componente c80 (user)
- Confiança: `0.0022`

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

## Componente c81 (edge_security)
- Confiança: `0.0022`

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

## Componente c82 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c83 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c84 (data_store)
- Confiança: `0.0022`

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
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

### 3. [Denial of Service] Indisponibilidade de banco
- Descrição: Consultas pesadas/abusivas podem degradar severamente o datastore.
- Vulnerabilidade associada: Configuração insegura ou ausência de controles específicos para a ameaça.
- Contramedidas:
  - Definir baseline de segurança para o componente.
  - Ativar monitoramento e alertas com resposta a incidentes.
  - Executar testes contínuos de segurança (SAST/DAST/config).
- Referências: OWASP, NIST CSF

## Componente c85 (user)
- Confiança: `0.0022`

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

## Componente c86 (user)
- Confiança: `0.0022`

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

## Componente c87 (compute)
- Confiança: `0.0022`

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

## Componente c88 (compute)
- Confiança: `0.0022`

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

## Componente c89 (edge_security)
- Confiança: `0.0021`

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

## Componente c90 (ops)
- Confiança: `0.0021`

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

## Componente c91 (user)
- Confiança: `0.0021`

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

## Componente c92 (compute)
- Confiança: `0.0021`

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

## Componente c93 (gateway)
- Confiança: `0.0012`

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

## Componente c94 (gateway)
- Confiança: `0.001`

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
