# Modelagem de Ameaças com IA (MVP)

Este repositório implementa um MVP para o desafio de **modelagem automática de ameaças** a partir de diagramas de arquitetura, combinando:

1. **Detecção supervisionada de componentes** (YOLO);
2. **Mapeamento STRIDE por tipo de componente**;
3. **Associação de vulnerabilidades e contramedidas**;
4. **Geração de relatório automático** em JSON e Markdown.

## Estrutura real do projeto

```text
.
├── data/
│   ├── images/
│   ├── labels/
│   └── data.yaml
├── docs/
│   ├── desafio.md
│   ├── planning.md
│   ├── threat-baseline.md
│   └── architectures/
├── output/
│   ├── *_components.json
│   └── *_threat_report.(json|md)
└── src/
    ├── detector/
    │   ├── classes.py
    │   ├── train_yolo.py
    │   ├── predict_yolo.py
    │   └── write_data_yaml.py
    ├── stride/
    │   └── rules.py
    ├── knowledge_base/
    │   └── catalog.py
    └── report/
        └── generate_report.py
```

## Como executar

### 1) Gerar `data/data.yaml`

```bash
python src/detector/write_data_yaml.py
```

> Observação (Windows): o script escreve `path` absoluto no YAML para evitar o erro
> `images not found` quando o Ultralytics tenta resolver caminhos relativos no
> diretório interno de datasets.

### 2) Treinar detector (opcional)

```bash
python src/detector/train_yolo.py
```

### 3) Detectar componentes nos diagramas

```bash
python src/detector/predict_yolo.py --device cpu
```

Arquivos esperados:
- `output/aws_components.json`
- `output/azure_components.json`

### 4) Gerar relatório STRIDE + contramedidas

```bash
python src/report/generate_report.py --input-dir output --out-dir output
```

Arquivos gerados:
- `output/aws_components_threat_report.json`
- `output/aws_components_threat_report.md`
- `output/azure_components_threat_report.json`
- `output/azure_components_threat_report.md`

## Limitações do MVP

- O mapeamento STRIDE é baseado em regras heurísticas por tipo de componente.
- A base de conhecimento de vulnerabilidades/contramedidas é inicial e pode ser expandida.
- A qualidade do relatório depende da qualidade da detecção dos componentes.
