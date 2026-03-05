#!/usr/bin/env python3
"""
Script para separar dataset balanceado entre train/val
Garante distribuição equilibrada entre AWS, Azure e GCP
"""

import shutil
import random
from pathlib import Path
from collections import defaultdict

def get_provider_from_filename(filename):
    """Identifica provider (AWS, Azure, GCP) pelo nome do arquivo"""
    filename_lower = filename.lower()
    if filename_lower.startswith('aws_'):
        return 'aws'
    elif filename_lower.startswith('azure_'):
        return 'azure'
    elif filename_lower.startswith('gcp_'):
        return 'gcp'
    else:
        return 'unknown'

def group_files_by_service(image_files):
    """Agrupa arquivos por serviço (ignorando augmentations)"""
    service_groups = defaultdict(list)
    
    for img_path in image_files:
        filename = img_path.name
        # Remove sufixo de augmentation (_aug_X) para agrupar por serviço
        base_name = '_'.join(filename.split('_')[:-2]) if '_aug_' in filename else filename
        
        service_groups[base_name].append(img_path)
    
    return service_groups

def split_dataset_balanced(data_dir, val_ratio=0.1, seed=42):
    """
    Separa dataset mantendo balanceamento entre:
    - Providers (AWS, Azure, GCP)
    - Serviços dentro de cada provider
    """
    
    random.seed(seed)
    
    # Diretórios
    images_train_dir = data_dir / 'images' / 'train'
    images_val_dir = data_dir / 'images' / 'val'
    labels_train_dir = data_dir / 'labels' / 'train'
    labels_val_dir = data_dir / 'labels' / 'val'
    
    # Criar diretórios val se não existirem
    images_val_dir.mkdir(parents=True, exist_ok=True)
    labels_val_dir.mkdir(parents=True, exist_ok=True)
    
    # Obter todos os arquivos de imagens em train
    image_files = list(images_train_dir.glob('*.png'))
    print(f"Total de imagens encontradas: {len(image_files)}")
    
    # Agrupar por provider e serviço
    provider_services = defaultdict(lambda: defaultdict(list))
    
    for img_path in image_files:
        provider = get_provider_from_filename(img_path.name)
        service_name = '_'.join(img_path.name.split('_')[:-2]) if '_aug_' in img_path.name else img_path.name
        provider_services[provider][service_name].append(img_path)
    
    print("\nDistribuição por provider:")
    for provider, services in provider_services.items():
        total_files = sum(len(files) for files in services.values())
        print(f"  {provider.upper()}: {total_files} arquivos em {len(services)} serviços")
    
    # Separar arquivos para validação
    val_files = []
    train_files = []
    
    for provider, services in provider_services.items():
        provider_val_files = []
        provider_train_files = []
        
        print(f"\nSeparando {provider.upper()}:")
        
        for service_name, files in services.items():
            # Calcular quantos arquivos vão para val (arredondado para cima)
            n_val = max(1, int(len(files) * val_ratio))
            
            # Embaralhar e separar
            files_sorted = sorted(files)  # Sort para consistência
            random.shuffle(files_sorted)
            
            service_val = files_sorted[:n_val]
            service_train = files_sorted[n_val:]
            
            provider_val_files.extend(service_val)
            provider_train_files.extend(service_train)
            
            print(f"  {service_name}: {len(service_train)} train, {len(service_val)} val")
        
        val_files.extend(provider_val_files)
        train_files.extend(provider_train_files)
        
        print(f"  {provider.upper()} total: {len(provider_train_files)} train, {len(provider_val_files)} val")
    
    print("\nResumo final:")
    print(f"  Train: {len(train_files)} arquivos")
    print(f"  Val: {len(val_files)} arquivos")
    print(f"  Ratio val/total: {len(val_files)/(len(train_files)+len(val_files)):.2%}")
    
    # Verificar balanceamento de providers em val
    val_provider_count = defaultdict(int)
    for img_path in val_files:
        provider = get_provider_from_filename(img_path.name)
        val_provider_count[provider] += 1
    
    print("\nDistribuição VAL por provider:")
    for provider, count in val_provider_count.items():
        print(f"  {provider.upper()}: {count} arquivos ({count/len(val_files):.1%})")
    
    # Mover arquivos para val
    moved_count = 0
    for img_path in val_files:
        # Mover imagem
        img_dest = images_val_dir / img_path.name
        if not img_dest.exists():
            shutil.move(str(img_path), str(img_dest))
            
            # Mover label correspondente
            label_name = img_path.stem + '.txt'
            label_src = labels_train_dir / label_name
            label_dest = labels_val_dir / label_name
            
            if label_src.exists():
                shutil.move(str(label_src), str(label_dest))
            
            moved_count += 1
    
    print(f"\nMovidos {moved_count} arquivos para val/")
    
    # Limpar arquivos .cache se existirem
    for cache_file in [labels_train_dir / 'train.cache', labels_val_dir / 'val.cache']:
        if cache_file.exists():
            cache_file.unlink()
            print(f"Removido cache file: {cache_file}")
    
    return len(train_files), len(val_files)

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / 'data'
    
    print("=== Separando Dataset Train/Val ===")
    print(f"Diretório de dados: {data_dir}")
    
    if not data_dir.exists():
        print("ERRO: Diretório data/ não encontrado!")
        return
    
    # Verificar se há arquivos em train
    images_train_dir = data_dir / 'images' / 'train'
    if not images_train_dir.exists():
        print("ERRO: Diretório data/images/train não encontrado!")
        return
    
    # Fazer split balanceado
    train_count, val_count = split_dataset_balanced(data_dir, val_ratio=0.1)
    
    print("\n=== Concluído ===")
    print(f"Train: {train_count} arquivos")
    print(f"Val: {val_count} arquivos")
    print(f"Total: {train_count + val_count} arquivos")

if __name__ == "__main__":
    main()
