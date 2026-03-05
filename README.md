# IA para Modelagem de Ameaças (MVP)

Pipeline de **modelagem automática de ameaças** a partir de diagramas de arquitetura, combinando:

1. detecção supervisionada de componentes (YOLO);
2. mapeamento STRIDE por tipo de componente;
3. mapeamento STRIDE por interação entre componentes;
4. geração de relatório automático em JSON e Markdown.

## Visão geral da arquitetura

```text
Diagramas -> Detector YOLO -> Componentes priorizados -> Regras STRIDE -> Relatório (JSON/MD)
```

## Estrutura do repositório

```text
.
├── data/                        # Dataset local (imagens, labels, yaml)
├── docs/                        # Materiais de apoio do desafio
├── output/                      # Saídas de inferência e relatórios
├── src/
│   ├── detector/                # Treino/inferência e utilitários de dataset
│   ├── knowledge_base/          # Vulnerabilidades, contramedidas e referências
│   ├── report/                  # Geração de relatório final
│   └── stride/                  # Regras STRIDE por componente/interação
├── Makefile                     # Comandos de desenvolvimento
├── pyproject.toml               # Configuração de lint/format/test
├── requirements.txt             # Dependências base (CPU)
└── requirements-gpu.txt         # Dependências para GPU
```

## Requisitos

- Python 3.10+
- Dependências instaladas com `pip install -r requirements.txt`
- (Opcional) GPU compatível com CUDA para treino/inferência acelerados

## Execução rápida

### 1) Preparar `data/data.yaml`

```bash
python src/detector/write_data_yaml.py
```

### 2) Converter XML para YOLO (opcional)

```bash
python src/detector/xml_to_yolo.py --xml-dir data/xml --labels-dir data/labels/train
```

Comandos úteis:

```bash
# Somente varredura de rótulos
python src/detector/xml_to_yolo.py --xml-dir data/xml --scan-only

# Fallback de classe para rótulos não mapeados
python src/detector/xml_to_yolo.py --xml-dir data/xml --labels-dir data/labels/train --default-class compute

# Falhar execução quando houver XML com objetos e saída vazia
python src/detector/xml_to_yolo.py --xml-dir data/xml --labels-dir data/labels/train --fail-on-empty
```

### 3) Treinar detector (opcional)

```bash
python src/detector/train_yolo.py --device 0
```

### 4) Detectar componentes

```bash
python src/detector/predict_yolo.py --device cpu --max-components 15 --min-priority-confidence 0.0
```

Saídas esperadas em `output/`:

- `*_components.json`
- `*_annotated.png`

### 5) Gerar relatório STRIDE

```bash
python src/report/generate_report.py --input-dir output --out-dir output
```

Saídas esperadas em `output/`:

- `*_threat_report.json`
- `*_threat_report.md`

## Comandos de desenvolvimento

```bash
make install      # instala dependências base
make check        # validações rápidas (lint + compilação)
make run-report   # gera relatório a partir de output/
```

## Limitações atuais

- O mapeamento STRIDE usa regras heurísticas.
- Interações entre componentes podem ser inferidas por proximidade quando não há fluxos explícitos.
- A base de conhecimento é inicial e deve evoluir conforme novos cenários.
- A qualidade da saída depende da qualidade da detecção.

## Próximos passos recomendados

- ampliar dataset rotulado e matriz de classes;
- incluir avaliação sistemática (métricas de detecção e qualidade do relatório);
- adicionar suíte de testes automatizados para regras STRIDE e geração de relatório.
