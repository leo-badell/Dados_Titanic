"""
Script principal para execução da Análise Exploratória de Dados do Titanic.

Este script coordena todas as etapas da análise:
1. Carregamento dos dados
2. Exibição de informações básicas
3. Tratamento de dados
4. Geração de estatísticas descritivas
5. Análise de sobrevivência
6. Geração de insights
7. Criação de visualizações

Autor: Projeto EDA Titanic
Data: 2026
"""

import os
import sys

# Importar módulos do projeto
from carregador import carregar_dados, exibir_info_basica
from analise import (
    tratar_dados, 
    gerar_estatisticas_descritivas, 
    analisar_sobrevivencia,
    gerar_insights,
    salvar_insights
)
from graficos import gerar_todas_visualizacoes


def main():
    """
    Função principal que executa todo o pipeline de análise.
    """
    print("="*60)
    print("ANÁLISE EXPLORATÓRIA DE DADOS - DATASET TITANIC")
    print("="*60)
    print()
    
    # ==============================
    # 1. DEFINIR CAMINHOS
    # ==============================
    # Caminho base do projeto (diretório raiz)
    caminho_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Caminho do dataset
    caminho_dataset = os.path.join(caminho_base, 'data', 'titanic.csv')
    
    # Diretórios de saída
    diretorio_figuras = os.path.join(caminho_base, 'outputs', 'figures')
    diretorio_tabelas = os.path.join(caminho_base, 'outputs', 'tables')
    
    # ==============================
    # 2. CARREGAR DADOS
    # ==============================
    try:
        df_original = carregar_dados(caminho_dataset)
    except FileNotFoundError as e:
        print(f"\n[ERRO] {e}")
        print("Certifique-se de que o arquivo 'titanic.csv' está no diretório 'data/'")
        sys.exit(1)
    except ValueError as e:
        print(f"\n[ERRO] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERRO] Erro inesperado ao carregar dados: {e}")
        sys.exit(1)
    
    # ==============================
    # 3. INFORMAÇÕES BÁSICAS
    # ==============================
    try:
        exibir_info_basica(df_original)
    except Exception as e:
        print(f"\n[AVISO] Erro ao exibir informações básicas: {e}")
        print("Continuando com a análise...")
    
    # ==============================
    # 4. TRATAMENTO DE DADOS
    # ==============================
    try:
        df_tratado = tratar_dados(df_original)
    except Exception as e:
        print(f"\n[ERRO] Erro ao tratar dados: {e}")
        print("Usando dados originais sem tratamento...")
        df_tratado = df_original.copy()
    
    # ==============================
    # 5. ESTATÍSTICAS DESCRITIVAS
    # ==============================
    try:
        estatisticas = gerar_estatisticas_descritivas(df_tratado)
    except Exception as e:
        print(f"\n[AVISO] Erro ao gerar estatísticas: {e}")
        estatisticas = {}
    
    # ==============================
    # 6. ANÁLISE DE SOBREVIVÊNCIA
    # ==============================
    try:
        analises = analisar_sobrevivencia(df_tratado)
    except Exception as e:
        print(f"\n[AVISO] Erro ao analisar sobrevivência: {e}")
        analises = {}
    
    # ==============================
    # 7. GERAR INSIGHTS
    # ==============================
    try:
        insights = gerar_insights(df_tratado, analises)
        
        # Exibir insights no console
        print("\n")
        for linha in insights:
            print(linha)
        
        # Salvar insights em arquivo
        caminho_insights = os.path.join(diretorio_tabelas, 'insights.txt')
        salvar_insights(insights, caminho_insights)
    except Exception as e:
        print(f"\n[AVISO] Erro ao gerar/salvar insights: {e}")
    
    # ==============================
    # 8. GERAR VISUALIZAÇÕES
    # ==============================
    try:
        gerar_todas_visualizacoes(df_tratado, diretorio_figuras)
    except Exception as e:
        print(f"\n[AVISO] Erro ao gerar visualizações: {e}")
    
    # ==============================
    # 9. FINALIZAÇÃO
    # ==============================
    print("\n" + "="*60)
    print("ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("="*60)
    print(f"\nResultados salvos em:")
    print(f"   - Insights: {caminho_insights}")
    print(f"   - Gráficos: {diretorio_figuras}")
    print("\n[OK] Pipeline de análise executado com sucesso!")
    print()


if __name__ == "__main__":
    main()
