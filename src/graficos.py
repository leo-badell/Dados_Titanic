"""
Módulo para visualização de dados.
Responsável por criar e salvar gráficos da análise exploratória.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os


# Configurações globais de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10


def criar_diretorio_saida(caminho):
    """
    Cria o diretório de saída se não existir.
    
    Parâmetros:
    -----------
    caminho : str
        Caminho do diretório
    """
    os.makedirs(caminho, exist_ok=True)


def plot_distribuicao_sobreviventes(df, caminho_saida):
    """
    Cria gráfico de distribuição de sobreviventes vs não sobreviventes.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    caminho_saida : str
        Caminho para salvar o gráfico
    """
    # Validação: verifica se a coluna Survived existe
    if 'Survived' not in df.columns:
        print(f"[AVISO] Coluna 'Survived' não encontrada. Pulando gráfico: {caminho_saida}")
        return
    
    try:
        plt.figure(figsize=(8, 6))
        
        # Contagem de sobreviventes
        sobrevivencia_count = df['Survived'].value_counts().sort_index()
        labels = ['Não Sobreviveu', 'Sobreviveu']
        colors = ['#ff6b6b', '#51cf66']
        
        # Criar gráfico de barras
        ax = sobrevivencia_count.plot(kind='bar', color=colors)
        plt.title('Distribuição de Sobreviventes no Titanic', fontsize=14, fontweight='bold')
        plt.xlabel('Status de Sobrevivência', fontsize=12)
        plt.ylabel('Número de Passageiros', fontsize=12)
        plt.xticks([0, 1], labels, rotation=0)
        
        # Adicionar valores nas barras
        for i, v in enumerate(sobrevivencia_count):
            ax.text(i, v + 10, str(v), ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        
        # Salvar gráfico
        criar_diretorio_saida(os.path.dirname(caminho_saida))
        plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
        print(f"[OK] Gráfico salvo: {caminho_saida}")
        plt.close()
    except Exception as e:
        print(f"[ERRO] Falha ao criar gráfico de distribuição de sobreviventes: {e}")
        plt.close()  # Garante que a figura seja fechada mesmo em caso de erro


def plot_sobrevivencia_por_sexo(df, caminho_saida):
    """
    Cria gráfico de sobrevivência por sexo.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    caminho_saida : str
        Caminho para salvar o gráfico
    """
    # Validação: verifica se as colunas necessárias existem
    if 'Sex' not in df.columns or 'Survived' not in df.columns:
        print(f"[AVISO] Colunas 'Sex' ou 'Survived' não encontradas. Pulando gráfico: {caminho_saida}")
        return
    
    try:
        plt.figure(figsize=(10, 6))
        
        # Criar gráfico de barras agrupadas (com proteção contra valores ausentes)
        sobrev_sexo = df.groupby(['Sex', 'Survived']).size().unstack(fill_value=0)
        ax = sobrev_sexo.plot(kind='bar', color=['#ff6b6b', '#51cf66'], width=0.7)
        
        plt.title('Sobrevivência por Sexo no Titanic', fontsize=14, fontweight='bold')
        plt.xlabel('Sexo', fontsize=12)
        plt.ylabel('Número de Passageiros', fontsize=12)
        plt.xticks(rotation=0)
        plt.legend(['Não Sobreviveu', 'Sobreviveu'], title='Status')
        
        # Adicionar valores nas barras
        for container in ax.containers:
            ax.bar_label(container, fontweight='bold')
        
        plt.tight_layout()
        
        # Salvar gráfico
        criar_diretorio_saida(os.path.dirname(caminho_saida))
        plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
        print(f"[OK] Gráfico salvo: {caminho_saida}")
        plt.close()
    except Exception as e:
        print(f"[ERRO] Falha ao criar gráfico de sobrevivência por sexo: {e}")
        plt.close()


def plot_sobrevivencia_por_classe(df, caminho_saida):
    """
    Cria gráfico de sobrevivência por classe.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    caminho_saida : str
        Caminho para salvar o gráfico
    """
    # Validação: verifica se as colunas necessárias existem
    if 'Pclass' not in df.columns or 'Survived' not in df.columns:
        print(f"[AVISO] Colunas 'Pclass' ou 'Survived' não encontradas. Pulando gráfico: {caminho_saida}")
        return
    
    try:
        plt.figure(figsize=(10, 6))
        
        # Calcular percentuais (com proteção contra valores ausentes)
        sobrev_classe = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
        sobrev_classe_pct = sobrev_classe.div(sobrev_classe.sum(axis=1), axis=0) * 100
        
        # Criar gráfico de barras empilhadas
        ax = sobrev_classe_pct.plot(kind='bar', stacked=True, color=['#ff6b6b', '#51cf66'], width=0.6)
        
        plt.title('Taxa de Sobrevivência por Classe (%)', fontsize=14, fontweight='bold')
        plt.xlabel('Classe', fontsize=12)
        plt.ylabel('Percentual (%)', fontsize=12)
        plt.xticks([0, 1, 2], ['1ª Classe', '2ª Classe', '3ª Classe'], rotation=0)
        plt.legend(['Não Sobreviveu', 'Sobreviveu'], title='Status', loc='upper right')
        plt.ylim(0, 100)
        
        # Adicionar linha de referência em 50%
        plt.axhline(y=50, color='gray', linestyle='--', linewidth=1, alpha=0.5)
        
        plt.tight_layout()
        
        # Salvar gráfico
        criar_diretorio_saida(os.path.dirname(caminho_saida))
        plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
        print(f"[OK] Gráfico salvo: {caminho_saida}")
        plt.close()
    except Exception as e:
        print(f"[ERRO] Falha ao criar gráfico de sobrevivência por classe: {e}")
        plt.close()


def plot_distribuicao_idade(df, caminho_saida):
    """
    Cria gráfico de distribuição de idade por sobrevivência.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    caminho_saida : str
        Caminho para salvar o gráfico
    """
    # Validação: verifica se as colunas necessárias existem
    if 'Age' not in df.columns or 'Survived' not in df.columns:
        print(f"[AVISO] Colunas 'Age' ou 'Survived' não encontradas. Pulando gráfico: {caminho_saida}")
        return
    
    try:
        plt.figure(figsize=(10, 6))
        
        # Criar histogramas sobrepostos (removendo valores NaN)
        sobreviveu = df[df['Survived'] == 1]['Age'].dropna()
        nao_sobreviveu = df[df['Survived'] == 0]['Age'].dropna()
        
        # Verifica se há dados suficientes para plotar
        if len(sobreviveu) == 0 and len(nao_sobreviveu) == 0:
            print(f"[AVISO] Não há dados de idade válidos. Pulando gráfico: {caminho_saida}")
            plt.close()
            return
        
        plt.hist(nao_sobreviveu, bins=30, alpha=0.6, color='#ff6b6b', label='Não Sobreviveu', edgecolor='black')
        plt.hist(sobreviveu, bins=30, alpha=0.6, color='#51cf66', label='Sobreviveu', edgecolor='black')
        
        plt.title('Distribuição de Idade por Status de Sobrevivência', fontsize=14, fontweight='bold')
        plt.xlabel('Idade', fontsize=12)
        plt.ylabel('Frequência', fontsize=12)
        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        
        # Salvar gráfico
        criar_diretorio_saida(os.path.dirname(caminho_saida))
        plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
        print(f"[OK] Gráfico salvo: {caminho_saida}")
        plt.close()
    except Exception as e:
        print(f"[ERRO] Falha ao criar gráfico de distribuição de idade: {e}")
        plt.close()


def gerar_todas_visualizacoes(df, diretorio_saida):
    """
    Gera todas as visualizações do projeto.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    diretorio_saida : str
        Diretório onde salvar os gráficos
    """
    print("\n" + "="*60)
    print("GERANDO VISUALIZAÇÕES")
    print("="*60)
    print()
    
    # Criar diretório se não existir
    criar_diretorio_saida(diretorio_saida)
    
    # Gerar cada gráfico
    plot_distribuicao_sobreviventes(df, os.path.join(diretorio_saida, '01_distribuicao_sobreviventes.png'))
    plot_sobrevivencia_por_sexo(df, os.path.join(diretorio_saida, '02_sobrevivencia_por_sexo.png'))
    plot_sobrevivencia_por_classe(df, os.path.join(diretorio_saida, '03_sobrevivencia_por_classe.png'))
    plot_distribuicao_idade(df, os.path.join(diretorio_saida, '04_distribuicao_idade.png'))
    
    print(f"\n[OK] Todas as visualizações foram geradas em: {diretorio_saida}")
