import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
caminho_arquivo = 'C:/Users/samuel.marinho/Desktop/Python/Estatistica_descritiva_Python/Estatística Descritivas - Preços de Ativos Financeiros/PETR4.SA.csv'

# Leitura do arquivo em Excel
dados = pd.read_csv(caminho_arquivo, sep=',')

# informações gerais sobre os dados
print("Analise Geral sobre os ativos da petrobras:\n")
dados.info()

# Observar as x primeira linhas do conjunto de dados
dh = dados.head(3)
print(f'\nAnalise das 3 primeiras linhas:\n\n{dh}')

# Observar as x ultimas linhas do conjunto de dados
dt = dados.tail(3)
print(f'\n\nAnalise das 3 ultimas linhas:\n\n{dt}')

# Estatistica geral com os principais calculos usados: Contagem; media; desvio padrao; minimo; primeiro; segundo e terceiro quartil; valor max.
ddes = dados.describe()
print(f'\n\nEstatistica geral:\n\n{ddes}')

# Saber a dimensão dos dados
dim = dados.shape
print(f'\n\nDimensão dos dados:\n\n{dim}')

# Coeficiente de Variação
CV = (dados.std(numeric_only=True) / dados.mean(numeric_only=True)) * 100
print(f'\n\nCoeficiente de variação:\n\n{CV}')

# Criação de Histogramas
Name = 'Volume'
dados[Name].hist()

plt.title(f'Histograma de {Name}')
plt.xlabel(Name, size=14)
plt.ylabel('Frequency', size=14)

# Média e mediana
plt.plot(dados[Name].median(), 1, '*r', label='Mediana')
plt.plot(dados[Name].mean(), 1, 'oy', label='Média')

plt.legend()  # Adiciona a legenda ao gráfico
plt.show()

# Criação de um Boxplot
sns.boxplot(data = dados.iloc[:,0:6])
plt.show

# Criação de um grafico de linhas
dados.iloc[:,0:6].plot()
plt.show()