import io
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
caminho_arquivo = 'C:/Users/samuel.marinho/Desktop/Python/Analises/train.csv'

# Leitura do arquivo em Excel
dados = pd.read_csv(caminho_arquivo, sep=',')

# informações gerais sobre os dados
print("Analise Geral sobre o Titanic:\n")
dados.info()

# Observar as x primeira linhas do conjunto de dados
dh = dados.head(3)
print(f'\nAnalise das 3 primeiras linhas:\n\n{dh}')


# Observar as x ultimas linhas do conjunto de dados
dt = dados.tail(3)
print(f'\n\nAnalise das 3 ultimas linhas:\n\n{dt}')

# Estatistica geral com os principais calculos usados
ddes = dados.describe()
print(f'\n\nEstatistica geral:\n\n{ddes}')

# Avaliar quantos valores faltantes existem
dft = dados.isnull().sum()
print(f'\n\nValores ausentes:\n\n{dft}')

# Preencher valores faltantes com a média   
dcm = dados.fillna(dados['Age'].dropna().median(), inplace = True)
print(f'\n\nPreenchimento dos valores faltantes com a média:\n\n{dft}')

# Avaliar se os valores foram trocados
dvr = dados.isnull().sum()
print(f'\n\nValores restaurados:\n\n{dvr}')

# Saber a dimensão dos dados
dim = dados.shape
print(f'\n\nDimensão dos dados:\n\n{dim}')

# Plotar sobreviventes
dados.plot(kind = "scatter", x = "Fare", y = "Survived", color = "r", linewidth = 1)
plt.show()

# Sobreviventes em relação a classe do navio (titanic)
sns.barplot(x = "Classe", y = "Sobreviventes", data = dados)
plt.show()