"""
Módulo para Análise Exploratória de Dados (EDA).
Contém funções para análise estatística, tratamento de dados e geração de insights.
"""

import pandas as pd
import numpy as np
import os


def tratar_dados(df):
    """
    Aplica tratamentos nos dados ausentes e cria variáveis derivadas.
    
    Decisões de tratamento:
    - Age: preencher valores ausentes com a mediana
    - Embarked: preencher com a moda (valor mais frequente)
    - Cabin: manter ausentes (muitos valores faltando)
    - Criar variável 'AgeGroup' para faixas etárias
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame original
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame tratado com novas variáveis
    """
    # Cria uma cópia para não modificar o original
    df_tratado = df.copy()
    
    print("\n" + "="*60)
    print("TRATAMENTO DE DADOS")
    print("="*60)
    
    # 1. Tratamento de valores ausentes em Age
    if 'Age' in df_tratado.columns:
        idade_ausentes = df_tratado['Age'].isnull().sum()
        if idade_ausentes > 0:
            mediana_idade = df_tratado['Age'].median()
            df_tratado['Age'] = df_tratado['Age'].fillna(mediana_idade)
            print(f"\n[OK] Age: {idade_ausentes} valores ausentes preenchidos com mediana ({mediana_idade:.1f})")
    
    # 2. Tratamento de valores ausentes em Embarked
    if 'Embarked' in df_tratado.columns:
        embarked_ausentes = df_tratado['Embarked'].isnull().sum()
        if embarked_ausentes > 0:
            moda_embarked = df_tratado['Embarked'].mode()[0]
            df_tratado['Embarked'] = df_tratado['Embarked'].fillna(moda_embarked)
            print(f"[OK] Embarked: {embarked_ausentes} valores ausentes preenchidos com moda ('{moda_embarked}')")
    
    # 3. Criação de variável derivada: Faixa Etária
    if 'Age' in df_tratado.columns:
        df_tratado['AgeGroup'] = pd.cut(
            df_tratado['Age'], 
            bins=[0, 12, 18, 35, 60, 100],
            labels=['Criança (0-12)', 'Adolescente (13-18)', 'Adulto (19-35)', 'Meia-idade (36-60)', 'Idoso (60+)']
        )
        print(f"[OK] Criada variável 'AgeGroup' com 5 faixas etárias")
    
    # 4. Criação de variável: Tamanho da Família
    if 'SibSp' in df_tratado.columns and 'Parch' in df_tratado.columns:
        df_tratado['FamilySize'] = df_tratado['SibSp'] + df_tratado['Parch'] + 1
        print(f"[OK] Criada variável 'FamilySize' (irmãos + pais/filhos + passageiro)")
    
    print(f"\nDataset tratado: {df_tratado.shape[0]} linhas × {df_tratado.shape[1]} colunas")
    
    return df_tratado


def gerar_estatisticas_descritivas(df):
    """
    Gera estatísticas descritivas do dataset.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    
    Retorna:
    --------
    dict
        Dicionário contendo estatísticas descritivas
    """
    print("\n" + "="*60)
    print("ESTATÍSTICAS DESCRITIVAS")
    print("="*60)
    
    estatisticas = {}
    
    # Estatísticas numéricas
    print("\nVariáveis Numéricas:")
    stats_numericas = df.describe()
    print(stats_numericas)
    estatisticas['numericas'] = stats_numericas
    
    # Estatísticas categóricas
    print("\nVariáveis Categóricas:")
    colunas_categoricas = df.select_dtypes(include=['object']).columns
    for col in colunas_categoricas:
        print(f"\n{col}:")
        print(df[col].value_counts())
    
    return estatisticas


def analisar_sobrevivencia(df):
    """
    Analisa padrões associados à sobrevivência.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    
    Retorna:
    --------
    dict
        Dicionário com análises de sobrevivência
    """
    print("\n" + "="*60)
    print("ANÁLISE DE SOBREVIVÊNCIA")
    print("="*60)
    
    analises = {}
    
    # Validação: verifica se a coluna Survived existe
    if 'Survived' not in df.columns:
        print("\n[AVISO] Coluna 'Survived' não encontrada. Pulando análise de sobrevivência.")
        return analises
    
    # Taxa geral de sobrevivência
    try:
        taxa_sobrevivencia = df['Survived'].mean() * 100
        print(f"\nTaxa geral de sobrevivência: {taxa_sobrevivencia:.2f}%")
        analises['taxa_geral'] = taxa_sobrevivencia
    except Exception as e:
        print(f"[AVISO] Erro ao calcular taxa geral: {e}")
    
    # Sobrevivência por Sexo
    if 'Sex' in df.columns:
        try:
            sobrev_sexo = df.groupby('Sex')['Survived'].agg(['sum', 'count', 'mean'])
            sobrev_sexo['percentual'] = sobrev_sexo['mean'] * 100
            print("\nSobrevivência por Sexo:")
            print(sobrev_sexo)
            analises['por_sexo'] = sobrev_sexo
        except Exception as e:
            print(f"[AVISO] Erro ao analisar sobrevivência por sexo: {e}")
    
    # Sobrevivência por Classe
    if 'Pclass' in df.columns:
        try:
            sobrev_classe = df.groupby('Pclass')['Survived'].agg(['sum', 'count', 'mean'])
            sobrev_classe['percentual'] = sobrev_classe['mean'] * 100
            print("\nSobrevivência por Classe:")
            print(sobrev_classe)
            analises['por_classe'] = sobrev_classe
        except Exception as e:
            print(f"[AVISO] Erro ao analisar sobrevivência por classe: {e}")
    
    # Sobrevivência por Faixa Etária
    if 'AgeGroup' in df.columns:
        try:
            sobrev_idade = df.groupby('AgeGroup')['Survived'].agg(['sum', 'count', 'mean'])
            sobrev_idade['percentual'] = sobrev_idade['mean'] * 100
            print("\nSobrevivência por Faixa Etária:")
            print(sobrev_idade)
            analises['por_idade'] = sobrev_idade
        except Exception as e:
            print(f"[AVISO] Erro ao analisar sobrevivência por idade: {e}")
    
    # Tarifa média por sobrevivência
    if 'Fare' in df.columns:
        try:
            tarifa_sobrev = df.groupby('Survived')['Fare'].mean()
            print("\nTarifa média por sobrevivência:")
            print(tarifa_sobrev)
            analises['tarifa_media'] = tarifa_sobrev
        except Exception as e:
            print(f"[AVISO] Erro ao analisar tarifa por sobrevivência: {e}")
    
    return analises


def gerar_insights(df, analises):
    """
    Gera insights em linguagem natural a partir das análises.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados
    analises : dict
        Dicionário com resultados das análises
    
    Retorna:
    --------
    list
        Lista de insights em formato de texto
    """
    insights = []
    
    insights.append("="*60)
    insights.append("PRINCIPAIS INSIGHTS DA ANÁLISE DO TITANIC")
    insights.append("="*60)
    insights.append("")
    
    # Insight 1: Taxa geral
    if 'taxa_geral' in analises:
        taxa = analises['taxa_geral']
        insights.append(f"1. TAXA DE SOBREVIVÊNCIA GERAL")
        insights.append(f"   Apenas {taxa:.1f}% dos passageiros sobreviveram ao naufrágio,")
        insights.append(f"   evidenciando a gravidade do desastre.")
        insights.append("")
    
    # Insight 2: Sexo
    if 'por_sexo' in analises:
        sobrev_sexo = analises['por_sexo']
        if 'female' in sobrev_sexo.index and 'male' in sobrev_sexo.index:
            taxa_f = sobrev_sexo.loc['female', 'percentual']
            taxa_m = sobrev_sexo.loc['male', 'percentual']
            insights.append(f"2. INFLUÊNCIA DO SEXO")
            insights.append(f"   Mulheres tiveram taxa de sobrevivência de {taxa_f:.1f}%,")
            insights.append(f"   enquanto homens tiveram apenas {taxa_m:.1f}%.")
            insights.append(f"   Isso confirma a política 'mulheres e crianças primeiro'.")
            insights.append("")
    
    # Insight 3: Classe social
    if 'por_classe' in analises:
        sobrev_classe = analises['por_classe']
        insights.append(f"3. IMPACTO DA CLASSE SOCIAL")
        for classe in [1, 2, 3]:
            if classe in sobrev_classe.index:
                taxa = sobrev_classe.loc[classe, 'percentual']
                nome_classe = {1: 'primeira', 2: 'segunda', 3: 'terceira'}[classe]
                insights.append(f"   Classe {classe} ({nome_classe}): {taxa:.1f}% de sobrevivência")
        insights.append(f"   A classe social foi um fator determinante na sobrevivência.")
        insights.append("")
    
    # Insight 4: Idade
    if 'por_idade' in analises:
        insights.append(f"4. FAIXA ETÁRIA E SOBREVIVÊNCIA")
        insights.append(f"   Crianças e adolescentes tiveram prioridade nos botes salva-vidas,")
        insights.append(f"   conforme evidenciado pelas taxas de sobrevivência por faixa etária.")
        insights.append("")
    
    # Insight 5: Tarifa
    if 'tarifa_media' in analises:
        tarifa = analises['tarifa_media']
        if 0 in tarifa.index and 1 in tarifa.index:
            tarifa_mortos = tarifa[0]
            tarifa_sobrev = tarifa[1]
            insights.append(f"5. RELAÇÃO ENTRE TARIFA E SOBREVIVÊNCIA")
            insights.append(f"   Passageiros que sobreviveram pagaram em média £{tarifa_sobrev:.2f},")
            insights.append(f"   enquanto os que morreram pagaram £{tarifa_mortos:.2f}.")
            insights.append(f"   Tarifas mais altas indicam melhores acomodações e acesso aos botes.")
            insights.append("")
    
    # Insight 6: Valores ausentes
    insights.append(f"6. QUALIDADE DOS DADOS")
    insights.append(f"   O dataset possui {df.shape[0]} registros e {df.shape[1]} variáveis.")
    insights.append(f"   Valores ausentes foram tratados usando mediana (idade) e moda (embarque).")
    insights.append("")
    
    insights.append("="*60)
    insights.append("CONCLUSÃO")
    insights.append("="*60)
    insights.append("A análise revela que sobrevivência no Titanic foi fortemente influenciada")
    insights.append("por fatores socioeconômicos (classe), demográficos (sexo e idade) e")
    insights.append("protocolos de emergência da época. Mulheres, crianças e passageiros")
    insights.append("de classes mais altas tiveram significativamente mais chances de sobreviver.")
    
    return insights


def salvar_insights(insights, caminho_saida):
    """
    Salva os insights em um arquivo de texto.
    
    Parâmetros:
    -----------
    insights : list
        Lista de strings com os insights
    caminho_saida : str
        Caminho do arquivo de saída
    """
    # Verifica se há insights para salvar
    if not insights:
        print("[AVISO] Nenhum insight para salvar.")
        return
    
    # Cria o diretório se não existir
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    
    # Salva o arquivo com encoding UTF-8 para suportar caracteres especiais
    try:
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            for linha in insights:
                f.write(linha + '\n')
        print(f"\n[OK] Insights salvos em: {caminho_saida}")
    except Exception as e:
        print(f"\n[ERRO] Falha ao salvar insights: {e}")
