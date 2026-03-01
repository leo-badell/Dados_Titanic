# 🚢 Análise Exploratória de Dados - Dataset Titanic

## 📋 Objetivo do Projeto

Este projeto realiza uma **Análise Exploratória de Dados (EDA)** completa sobre o famoso dataset do Titanic. O objetivo é investigar os fatores que influenciaram a sobrevivência dos passageiros durante o naufrágio, utilizando técnicas estatísticas e visualizações gráficas para extrair insights valiosos dos dados.

O projeto foi desenvolvido com foco didático, sendo ideal para iniciantes em análise de dados que desejam aprender Python, pandas, matplotlib e seaborn através de um exemplo prático e bem estruturado.

## 📊 Descrição do Dataset

O dataset do Titanic contém informações sobre os passageiros do navio RMS Titanic, que naufragou em 15 de abril de 1912. O conjunto de dados inclui variáveis demográficas, socioeconômicas e de sobrevivência:

- **PassengerId**: Identificador único do passageiro
- **Survived**: Status de sobrevivência (0 = Não, 1 = Sim)
- **Pclass**: Classe do bilhete (1ª, 2ª ou 3ª classe)
- **Name**: Nome completo do passageiro
- **Sex**: Sexo (male/female)
- **Age**: Idade em anos
- **SibSp**: Número de irmãos/cônjuges a bordo
- **Parch**: Número de pais/filhos a bordo
- **Ticket**: Número do bilhete
- **Fare**: Tarifa paga pelo bilhete
- **Cabin**: Número da cabine
- **Embarked**: Porto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton)

## 🔍 Etapas da Análise

A análise é dividida nas seguintes etapas, executadas de forma automática pelo script principal:

### 1. Carregamento e Validação dos Dados
- Importação do arquivo CSV
- Verificação da integridade do arquivo
- Exibição das dimensões e estrutura do dataset

### 2. Exploração Inicial
- Identificação dos tipos de variáveis (numéricas e categóricas)
- Detecção de valores ausentes
- Visualização das primeiras linhas do dataset

### 3. Tratamento de Dados
- **Valores ausentes tratados conforme estratégias específicas:**
  - **Age (Idade)**: Valores ausentes preenchidos com a **mediana** da idade, pois a distribuição pode conter outliers
  - **Embarked (Porto de embarque)**: Valores ausentes preenchidos com a **moda** (valor mais frequente)
  - **Cabin (Cabine)**: Mantidos como ausentes devido à alta proporção de dados faltantes (>75%)

### 4. Criação de Variáveis Derivadas
- **AgeGroup**: Categorização da idade em 5 faixas etárias
  - Criança (0-12 anos)
  - Adolescente (13-18 anos)
  - Adulto (19-35 anos)
  - Meia-idade (36-60 anos)
  - Idoso (60+ anos)
- **FamilySize**: Tamanho da família a bordo (SibSp + Parch + 1)

### 5. Estatísticas Descritivas
- Cálculo de medidas de tendência central (média, mediana)
- Cálculo de medidas de dispersão (desvio padrão, quartis)
- Frequência de variáveis categóricas

### 6. Análise de Sobrevivência
Investigação de padrões através de agrupamentos e comparações:
- Taxa geral de sobrevivência
- Sobrevivência por sexo
- Sobrevivência por classe social
- Sobrevivência por faixa etária
- Relação entre tarifa paga e sobrevivência

### 7. Geração de Insights
Extração de conclusões em linguagem natural sobre:
- Impacto do sexo na sobrevivência
- Influência da classe social
- Efeito da idade
- Relação entre poder aquisitivo (tarifa) e chances de sobrevivência

### 8. Visualizações Gráficas
Criação de 5 gráficos salvos em alta resolução (300 DPI):
- **Distribuição de sobreviventes**: Contagem total de sobreviventes vs não sobreviventes
- **Sobrevivência por sexo**: Comparação entre homens e mulheres
- **Sobrevivência por classe**: Taxa de sobrevivência nas três classes
- **Distribuição de idade**: Histograma de idade por status de sobrevivência
- **Tarifa por sobrevivência**: Boxplot mostrando distribuição de tarifas

## 🧠 Decisões de Tratamento

### Por que usar a mediana para idade?
A mediana é mais robusta a outliers do que a média. Como a distribuição de idade pode conter valores extremos, a mediana representa melhor a "idade típica" dos passageiros.

### Por que usar a moda para porto de embarque?
Para variáveis categóricas com poucos valores ausentes, a moda (valor mais frequente) é a escolha mais lógica, pois mantém a distribuição proporcional original dos dados.

### Por que criar faixas etárias?
Categorizar a idade permite identificar padrões mais claros de sobrevivência por grupo etário, facilitando a análise da política "mulheres e crianças primeiro".

### Por que calcular tamanho da família?
Passageiros viajando sozinhos podem ter comportamento diferente de famílias. Esta variável permite investigar se grupos familiares tiveram maiores chances de sobrevivência.

## 🎨 Explicação das Visualizações

### Gráfico 1: Distribuição de Sobreviventes
Gráfico de barras simples mostrando quantos passageiros sobreviveram ou não. Permite visualizar rapidamente a proporção geral de mortalidade.

### Gráfico 2: Sobrevivência por Sexo
Gráfico de barras agrupadas que evidencia a diferença dramática entre taxas de sobrevivência de homens e mulheres, confirmando a política de evacuação.

### Gráfico 3: Sobrevivência por Classe
Gráfico de barras empilhadas mostrando percentuais. Revela desigualdade social: passageiros de primeira classe tiveram acesso privilegiado aos botes salva-vidas.

### Gráfico 4: Distribuição de Idade
Histogramas sobrepostos que permitem comparar a distribuição etária entre sobreviventes e não sobreviventes. Útil para identificar faixas etárias mais vulneráveis.

### Gráfico 5: Tarifa por Sobrevivência
Boxplot que mostra a distribuição de valores pagos. Tarifas mais altas indicam melhores acomodações (classes superiores), correlacionadas com maior sobrevivência.

## 💡 Principais Insights

1. **Taxa geral de sobrevivência foi baixa (~38%)**, evidenciando a magnitude do desastre
2. **Mulheres tiveram taxa de sobrevivência ~74%** vs ~19% dos homens (política "mulheres e crianças primeiro")
3. **Classe social foi determinante**: 1ª classe (~63%), 2ª classe (~47%), 3ª classe (~24%)
4. **Crianças e adolescentes tiveram prioridade** nos botes salva-vidas
5. **Passageiros que pagaram tarifas mais altas sobreviveram mais**, refletindo vantagens das classes superiores

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem de programação principal
- **pandas**: Manipulação e análise de dados tabulares
- **numpy**: Operações numéricas e arrays
- **matplotlib**: Biblioteca base para visualizações
- **seaborn**: Visualizações estatísticas de alto nível

## 📁 Estrutura de Pastas

```
Dados_Titanic/
│
├── data/                          # Dados brutos
│   └── titanic.csv               # Dataset original do Titanic
│
├── outputs/                       # Resultados gerados
│   ├── figures/                  # Gráficos em PNG (alta resolução)
│   │   ├── 01_distribuicao_sobreviventes.png
│   │   ├── 02_sobrevivencia_por_sexo.png
│   │   ├── 03_sobrevivencia_por_classe.png
│   │   ├── 04_distribuicao_idade.png
│   │   └── 05_tarifa_por_sobrevivencia.png
│   │
│   └── tables/                   # Tabelas e insights em texto
│       └── insights.txt          # Interpretações e conclusões
│
├── src/                           # Código-fonte modularizado
│   ├── executar.py               # Script principal de execução
│   ├── carregador.py             # Carregamento e validação de dados
│   ├── analise.py                # Funções de análise exploratória
│   └── graficos.py               # Criação de gráficos
│
├── README.md                      # Documentação completa do projeto
├── requirements.txt               # Dependências Python
└── .gitignore                     # Arquivos ignorados pelo Git
```

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone ou baixe este repositório**
   ```bash
   cd Dados_Titanic
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o script principal**
   ```bash
   python src/executar.py
   ```

4. **Visualize os resultados**
   - Gráficos gerados em: `outputs/figures/`
   - Insights salvos em: `outputs/tables/insights.txt`

### Saída Esperada

Ao executar o projeto, você verá no console:
- Informações sobre o carregamento dos dados
- Estrutura do dataset (dimensões, tipos, valores ausentes)
- Decisões de tratamento aplicadas
- Estatísticas descritivas
- Análises de sobrevivência por diferentes categorias
- Insights gerados automaticamente
- Confirmação do salvamento de gráficos e arquivos

## 📝 Observações

- O código foi desenvolvido de forma **didática e comentada**, ideal para aprendizado
- As funções são **pequenas e específicas**, seguindo boas práticas de programação
- **Caminhos são relativos**, garantindo portabilidade entre sistemas
- **Diretórios são criados automaticamente** se não existirem
- Tratamento de erros para garantir **execução robusta**

## 👥 Contribuições

Este é um projeto educacional. Sinta-se à vontade para:
- Adicionar novas análises
- Criar visualizações adicionais
- Melhorar o tratamento de dados
- Sugerir novos insights

## 📄 Licença

Projeto de código aberto para fins educacionais.

---

**Desenvolvido como material didático para aprendizado de Python e Análise de Dados**
