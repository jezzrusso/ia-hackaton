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

## Dataset utilizado

Este projeto utiliza como base o dataset público:

- https://www.kaggle.com/datasets/carlosrian/software-architecture-dataset

Crédito ao autor do dataset, aluno da FIAP. O conjunto original está no formato **Pascal VOC (XML)**, e neste projeto os rótulos foram convertidos para o formato **YOLO (TXT)** para treino e inferência com Ultralytics.

O dataset também já inclui variações de imagens geradas por **data augmentation** (por exemplo: rotação, ajustes de saturação e brilho), técnica usada para aumentar diversidade do treino e melhorar a robustez do modelo.

## Requisitos

- Python 3.10+
- `pip` atualizado
- (Opcional) GPU compatível com CUDA para treino/inferência acelerados

Instalação base (CPU):

```bash
pip install -r requirements.txt
```

Instalação para treino com GPU (CUDA 12.1):

```bash
pip install -r requirements-gpu.txt
pip install ultralytics opencv-python jinja2 pydantic pyyaml pillow
```

## Como baixar e preparar o dataset

Este projeto espera o dataset disponível dentro de `data/`, seguindo esta organização:

```text
data/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
├── xml/                 # obrigatório para treino (anotações Pascal VOC)
├── classes.txt
└── data.yaml
```

### Opção A (manual, via navegador)

1. Acesse o dataset no Kaggle: `https://www.kaggle.com/datasets/carlosrian/software-architecture-dataset`.
2. Faça download do `.zip`.
3. Extraia os arquivos do dataset para dentro da pasta `data/` do projeto.
4. Garanta que os XMLs de treino estejam em `data/xml` (formato Pascal VOC).
5. Garanta que as imagens estejam em `images/train` e `images/val`.
6. Gere os labels YOLO TXT a partir dos XMLs com o script de conversão (passo obrigatório para treino).

### Opção B (Kaggle CLI)

Pré-requisitos:

- conta no Kaggle;
- API token (`kaggle.json`) configurado em `~/.kaggle/kaggle.json`.

Comandos:

```bash
pip install kaggle
kaggle datasets download -d carlosrian/software-architecture-dataset -p data
unzip -o data/software-architecture-dataset.zip -d data
```

> Observação: dependendo da estrutura interna do zip, pode ser necessário mover as pastas extraídas para o layout esperado em `data/`.

### Gerar/normalizar `data/data.yaml`

Após posicionar os arquivos do dataset, execute:

```bash
python src/detector/write_data_yaml.py
```

Esse passo garante que o `data/data.yaml` seja recriado com a estrutura de classes correta.

### Converter XML (Pascal VOC) para YOLO TXT (obrigatório para treino)

Os dados de anotação de treinamento deste projeto são mantidos em XML e devem estar dentro de `data/xml`.
Antes de treinar, execute a conversão para gerar os labels `.txt` no formato YOLO:

```bash
python src/detector/xml_to_yolo.py --xml-dir data/xml --labels-dir data/labels/train --fail-on-empty
```

> Sem esse passo, o treino não terá labels YOLO válidos em `data/labels/train`.

## Como reproduzir o pipeline

### 1) Converter XML para YOLO (obrigatório para treino)

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

### 2) Treinar detector (opcional)

```bash
python src/detector/train_yolo.py --device 0
```

### 3) Detectar componentes

```bash
python src/detector/predict_yolo.py --device cpu --max-components 15 --min-priority-confidence 0.0
```

Saídas esperadas em `output/`:

- `*_components.json`
- `*_annotated.png`

### 4) Gerar relatório STRIDE

```bash
python src/report/generate_report.py --input-dir output --out-dir output
```

Saídas esperadas em `output/`:

- `*_threat_report.json`
- `*_threat_report.md`

## Reprodução mínima (sem treino)

Se você já possui pesos treinados em `runs/*/weights/best.pt`, a validação ponta a ponta pode ser feita com:

```bash
python src/detector/write_data_yaml.py
python src/detector/predict_yolo.py --device cpu
python src/report/generate_report.py --input-dir output --out-dir output
```

Esse fluxo gera componentes detectados e relatórios STRIDE sem necessidade de novo treinamento.

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
