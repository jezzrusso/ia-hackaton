# Planejamento de Execução do Projeto

Este documento descreve as etapas previstas para o desenvolvimento do projeto de **Modelagem de Ameaças utilizando Inteligência Artificial**, desde a definição do escopo até a entrega do MVP e da documentação final.

O planejamento foi organizado de forma incremental, priorizando validações progressivas e redução de risco técnico, conforme boas práticas de engenharia de software e segurança da informação.

---

## Visão Geral das Etapas

O projeto será executado nas seguintes fases:

1. Alinhamento e definição do escopo
2. Análise manual das arquiteturas e baseline de ameaças
3. Detecção automática de componentes de arquitetura
4. Mapeamento automatizado de ameaças com STRIDE
5. Associação de vulnerabilidades e contramedidas
6. Integração do MVP e avaliação
7. Documentação e apresentação final

Cada fase possui objetivos claros e entregáveis bem definidos.

---

## Fase 0 – Alinhamento e Definição do Escopo

### Objetivo
Definir claramente o recorte do problema a ser tratado no MVP, garantindo viabilidade técnica e foco nos requisitos essenciais do projeto.

### Atividades
- Definição dos tipos de componentes de arquitetura que serão considerados no MVP (ex.: usuários, API Gateway, balanceadores de carga, serviços backend e bancos de dados).
- Definição das categorias STRIDE que serão abordadas inicialmente.
- Estabelecimento dos limites do MVP, deixando explícito o que ficará fora do escopo nesta fase.

### Entregáveis
- Documento de escopo do MVP
- Lista de premissas e limitações assumidas

---

## Fase 1 – Análise Manual das Arquiteturas

### Objetivo
Criar um entendimento sólido das arquiteturas de referência e estabelecer uma base confiável de ameaças para validação futura do modelo.

### Atividades
- Análise manual das arquiteturas em nuvem (Azure e AWS).
- Identificação dos principais componentes, fluxos de dados e fronteiras de confiança.
- Aplicação manual da metodologia STRIDE sobre cada componente identificado.

### Entregáveis
- Tabela de ameaças por componente e por arquitetura
- Base de referência (ground truth) para validação do modelo automatizado

---

## Fase 2 – Detecção de Componentes de Arquitetura

### Objetivo
Desenvolver um modelo capaz de identificar automaticamente componentes de arquitetura a partir de diagramas em imagem.

### Atividades
- Construção ou seleção de um dataset contendo diagramas de arquitetura.
- Anotação manual dos componentes presentes nas imagens.
- Treinamento de um modelo supervisionado de visão computacional para detecção de objetos arquiteturais.

### Entregáveis
- Modelo treinado para identificação de componentes
- Saída estruturada contendo tipo e posição dos componentes detectados

---

## Fase 3 – Mapeamento Automatizado de Ameaças (STRIDE)

### Objetivo
Associar automaticamente categorias de ameaças STRIDE aos componentes identificados pelo modelo.

### Atividades
- Definição de regras de associação entre tipos de componentes e categorias STRIDE aplicáveis.
- Implementação de um módulo responsável por gerar ameaças potenciais com base nos componentes detectados.
- Validação dos resultados utilizando a análise manual realizada na Fase 1.

### Entregáveis
- Lista automatizada de ameaças por componente
- Relatório intermediário de validação

---

## Fase 4 – Associação de Vulnerabilidades e Contramedidas

### Objetivo
Enriquecer o resultado da modelagem de ameaças com vulnerabilidades conhecidas e contramedidas recomendadas.

### Atividades
- Construção de uma base de conhecimento relacionando:
  - Componente
  - Ameaça
  - Vulnerabilidade
  - Contramedidas
- Consideração de diferenças entre provedores de nuvem quando aplicável (Azure e AWS).

### Entregáveis
- Base estruturada de vulnerabilidades e contramedidas
- Motor de recomendação de mitigação de riscos

---

## Fase 5 – Integração do MVP e Avaliação

### Objetivo
Integrar todos os módulos desenvolvidos em um MVP funcional, capaz de gerar relatórios de modelagem de ameaças a partir de imagens de arquitetura.

### Atividades
- Integração do modelo de detecção, mapeamento STRIDE e motor de contramedidas.
- Geração automática de relatórios em formato estruturado.
- Testes utilizando as arquiteturas de referência fornecidas.

### Entregáveis
- MVP funcional
- Relatórios de modelagem de ameaças gerados automaticamente

---

## Fase 6 – Documentação e Apresentação Final

### Objetivo
Consolidar o projeto para entrega acadêmica, garantindo clareza técnica e comunicacional.

### Atividades
- Elaboração da documentação técnica detalhando o fluxo da solução.
- Preparação do vídeo de apresentação da proposta.
- Organização do repositório GitHub com código, instruções e artefatos do projeto.

### Entregáveis
- Documentação técnica completa
- Vídeo explicativo (até 15 minutos)
- Repositório GitHub do projeto

---

## Considerações Finais

O planejamento adotado prioriza uma abordagem incremental e validável, permitindo demonstrar a viabilidade técnica da solução proposta sem comprometer a clareza, a qualidade e o rigor conceitual exigidos para um MVP de segurança de software.
