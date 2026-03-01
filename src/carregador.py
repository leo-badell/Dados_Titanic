"""
Módulo para carregamento e validação de dados.
Responsável por importar o dataset CSV e validar sua existência.
"""

import pandas as pd
import os


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset do Titanic a partir de um arquivo CSV.
    
    Parâmetros:
    -----------
    caminho_arquivo : str
        Caminho para o arquivo CSV do dataset Titanic
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame contendo os dados do Titanic
    
    Levanta:
    --------
    FileNotFoundError
        Se o arquivo não for encontrado
    ValueError
        Se o arquivo estiver vazio ou malformado
    """
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    
    # Verifica se o arquivo tem tamanho válido
    if os.path.getsize(caminho_arquivo) == 0:
        raise ValueError(f"Arquivo vazio: {caminho_arquivo}")
    
    # Carrega o arquivo CSV com tratamento de encoding
    print(f"Carregando dados de: {caminho_arquivo}")
    try:
        # Tenta carregar com encoding UTF-8 (padrão)
        df = pd.read_csv(caminho_arquivo, encoding='utf-8')
    except UnicodeDecodeError:
        # Se falhar, tenta com encoding latin-1 (comum em datasets antigos)
        print("  [INFO] Tentando encoding alternativo...")
        df = pd.read_csv(caminho_arquivo, encoding='latin-1')
    
    # Valida se o DataFrame não está vazio
    if df.empty:
        raise ValueError("O arquivo CSV foi carregado mas não contém dados.")
    
    print(f"[OK] Dados carregados com sucesso!")
    print(f"  - Registros: {len(df)}")
    print(f"  - Colunas: {len(df.columns)}")
    
    return df


def exibir_info_basica(df):
    """
    Exibe informações básicas sobre o dataset.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados do Titanic
    """
    print("\n" + "="*60)
    print("INFORMAÇÕES BÁSICAS DO DATASET")
    print("="*60)
    
    # Dimensões
    print(f"\nDimensões: {df.shape[0]} linhas × {df.shape[1]} colunas")
    
    # Nome das colunas
    print(f"\nColunas: {list(df.columns)}")
    
    # Tipos de dados
    print("\nTipos de dados:")
    print(df.dtypes)
    
    # Valores ausentes
    print("\nValores ausentes por coluna:")
    valores_faltantes = df.isnull().sum()
    for coluna, qtd in valores_faltantes.items():
        percentual = (qtd / len(df)) * 100
        print(f"  {coluna}: {qtd} ({percentual:.1f}%)")
    
    # Primeiras linhas
    print("\nPrimeiras 5 linhas do dataset:")
    print(df.head())
