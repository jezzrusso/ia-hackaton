# Roteiro de Apresentação — MVP de Modelagem de Ameaças com IA

Este roteiro foi pensado para uma apresentação objetiva (10–15 minutos), mostrando **o que foi feito, em qual ordem, e onde isso está implementado no código**.

---

## 1) Abertura (Problema e objetivo)

**Mensagem para apresentar**
- O problema: modelagem de ameaças costuma ser manual, demorada e dependente de especialistas.
- O objetivo do MVP: automatizar parte desse processo a partir de diagramas de arquitetura.

**Onde isso está no projeto**
- Visão geral e escopo do MVP: `README.md`
- Contexto do desafio: `docs/desafio.md`

---

## 2) Fonte de dados e preparação do dataset

**Mensagem para apresentar**
- Foi usado o dataset público do Kaggle:
  - https://www.kaggle.com/datasets/carlosrian/software-architecture-dataset
- O dataset original está em **Pascal VOC XML**.
- Para treinar YOLO, foi necessário converter para **YOLO TXT**.
- O dataset já contém variações por **data augmentation** (rotação, brilho, saturação etc.), o que ajuda na robustez.

**Onde isso está no projeto**
- Documentação da origem do dataset e contexto: `README.md`
- Conversão XML → YOLO: `src/detector/xml_to_yolo.py`
- Escrita do `data.yaml`: `src/detector/write_data_yaml.py`
- Split balanceado train/val: `src/detector/split_dataset.py`

---

## 3) Treinamento do detector de componentes

**Mensagem para apresentar**
- O modelo utilizado foi YOLO (Ultralytics) para detecção de componentes em diagramas.
- O processo de treino foi estruturado para validar entradas e gerar os artefatos necessários.

**Onde isso está no projeto**
- Script de treino: `src/detector/train_yolo.py`
- Classes detectáveis: `src/detector/classes.py`
- Dependências: `requirements.txt` e `requirements-gpu.txt`

---

## 4) Inferência e priorização de componentes

**Mensagem para apresentar**
- Após o treino, a inferência detecta componentes nos diagramas.
- Em seguida, há priorização para reduzir ruído e focar no que é mais relevante para análise de ameaça.

**Onde isso está no projeto**
- Inferência e geração de JSON/PNG anotado: `src/detector/predict_yolo.py`
- Lógica de priorização: `src/stride/prioritization.py`
- Saídas produzidas: pasta `output/`

---

## 5) Regras STRIDE e base de conhecimento

**Mensagem para apresentar**
- O coração do MVP é transformar componentes detectados em riscos de segurança.
- Isso é feito com regras STRIDE por tipo de componente e por interação entre componentes.
- Cada ameaça é enriquecida com vulnerabilidades, contramedidas e referências.

**Onde isso está no projeto**
- Regras STRIDE por componente: `src/stride/rules.py`
- Regras STRIDE por interação: `src/stride/interaction_rules.py`
- Catálogo de conhecimento: `src/knowledge_base/catalog.py`

---

## 6) Geração do relatório final

**Mensagem para apresentar**
- O pipeline consolida tudo em relatório automático (JSON + Markdown).
- O relatório apresenta ameaças por componente, por associação e indicadores de qualidade.

**Onde isso está no projeto**
- Geração do relatório: `src/report/generate_report.py`
- Exemplos de saída: pasta `output/`

---

## 7) Organização profissional do projeto (governança)

**Mensagem para apresentar**
- Além da parte técnica, o projeto recebeu melhorias de organização para facilitar manutenção e colaboração.

**Onde isso está no projeto**
- Guia de contribuição: `CONTRIBUTING.md`
- Comandos de desenvolvimento: `Makefile`
- Configuração de qualidade/lint/test: `pyproject.toml`
- Higiene de repositório: `.gitignore`

---

## 8) Demo sugerida (passo a passo ao vivo)

1. Mostrar estrutura do projeto (`README.md`).
2. Mostrar conversão XML → YOLO (`src/detector/xml_to_yolo.py`).
3. Rodar inferência em um diagrama (`src/detector/predict_yolo.py`).
4. Abrir JSON de componentes gerado em `output/`.
5. Gerar relatório (`src/report/generate_report.py`).
6. Exibir relatório Markdown final em `output/*_threat_report.md`.

---

## 9) Fechamento (valor entregue e próximos passos)

**Mensagem para apresentar**
- Valor atual: acelera análise inicial de ameaças e padroniza uma primeira avaliação de risco.
- Próximos passos:
  - aumentar e qualificar dataset;
  - calibrar regras e priorização;
  - adicionar testes automatizados mais profundos;
  - evoluir para suporte a fluxos explícitos entre componentes.

**Onde isso está no projeto**
- Limitações e próximos passos já documentados: `README.md`

---

## 10) Script curto de fala (resumo de 60–90s)

> “Este MVP automatiza modelagem de ameaças a partir de diagramas. Primeiro detectamos componentes com YOLO, depois aplicamos regras STRIDE por componente e por interação, e por fim geramos relatórios com vulnerabilidades e contramedidas. A base veio de um dataset público no Kaggle, originalmente em Pascal VOC XML, que convertemos para YOLO TXT. O projeto também foi estruturado com boas práticas de engenharia — documentação, comandos padronizados e configuração de qualidade — para facilitar evolução e colaboração.”
