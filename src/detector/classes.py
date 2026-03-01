# Fonte de verdade das classes do detector (MVP)
# Mantém a numeração estável para treino YOLO e geração de relatório.

CLASSES = [
    "user",          # 0
    "edge_security", # 1
    "gateway",       # 2
    "compute",       # 3
    "data_store",    # 4
    "ops",           # 5
]

CLASS_TO_ID = {name: i for i, name in enumerate(CLASSES)}
ID_TO_CLASS = {i: name for i, name in enumerate(CLASSES)}