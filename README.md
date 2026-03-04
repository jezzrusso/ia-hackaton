# Modelagem de Ameaças com IA (MVP)

Este repositório implementa um MVP para o desafio de **modelagem automática de ameaças** a partir de diagramas de arquitetura, combinando:

1. **Detecção supervisionada de componentes** (YOLO);
2. **Mapeamento STRIDE por tipo de componente**;
3. **Mapeamento STRIDE por componente e por associação entre componentes**;
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
    │   ├── rules.py
    │   └── interaction_rules.py
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


### Converter XML para YOLO (opcional)

Se você tiver anotações em XML (ex.: Pascal VOC/LabelImg), use:

```bash
python src/detector/xml_to_yolo.py --xml-dir data/xml --labels-dir data/labels/train
```

Para descobrir primeiro todos os nomes de componentes existentes no lote de XML e ver
o que ainda não está mapeado para as classes genéricas:

```bash
python src/detector/xml_to_yolo.py --xml-dir data/xml --scan-only
```

Você pode sobrescrever o mapeamento de nomes de serviços para classes genéricas com `--mapping-json`.
O JSON deve ser um dicionário `nome_servico -> classe_generica` (classe em: `user`, `edge_security`, `gateway`, `compute`, `data_store`, `ops`).

### 2) Treinar detector (opcional)

```bash
python src/detector/train_yolo.py --device 0
```

O script de treino agora regenera o `data/data.yaml` e valida automaticamente se
`train` e `val` existem antes de iniciar o treinamento.

### 3) Detectar componentes nos diagramas

```bash
python src/detector/predict_yolo.py --device cpu --max-components 15 --min-priority-confidence 0.0
```

Arquivos esperados:
- `output/aws_components.json`
- `output/azure_components.json`
- `output/aws_annotated.png`
- `output/azure_annotated.png`

Os PNGs anotados preservam a resolução original e incluem:
- apenas componentes priorizados por `confiança x risco`;
- bounding box do componente;
- rótulo visual com ID (`c1`, `c2`, ...);
- linha de ligação quando o rótulo é deslocado para evitar sobreposição.

A saída JSON também registra:
- `selection`: estratégia de priorização aplicada;
- `excluded_components`: componentes descartados para reduzir ruído.

Você pode ajustar a priorização no CLI com `--max-components` e `--min-priority-confidence`.

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
- As associações entre componentes são inferidas por proximidade espacial quando o detector não informa fluxos explícitos.
- A base de conhecimento de vulnerabilidades/contramedidas é inicial e pode ser expandida.
- A qualidade do relatório depende da qualidade da detecção dos componentes.
