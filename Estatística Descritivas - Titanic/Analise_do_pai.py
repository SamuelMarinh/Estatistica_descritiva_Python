# Dicionario dos dados

# PassengerId: Um número único de identificação para cada passageiro.
# Survived: Indica se o passageiro sobreviveu (1) ou não (0) ao naufrágio.
# Pclass: Classe do bilhete do passageiro (1ª, 2ª ou 3ª classe).
# Name: Nome do passageiro.
# Sex: Sexo do passageiro.
# Age: Idade do passageiro em anos. (Algumas entradas podem estar em forma de fração se a idade for estimada).
# SibSp: Número de irmãos/cônjuges a bordo do Titanic.
# Parch: Número de pais/filhos a bordo do Titanic.
# Ticket: Número do bilhete.
# Fare: Tarifa paga pelo passageiro.
# Cabin: Número da cabine do passageiro.
# Embarked: Porto de embarque do passageiro (C = Cherbourg, Q = Queenstown, S = Southampton).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
caminho_arquivo = 'C:/Users/samuel.marinho/Desktop/Python/Estatistica_descritiva_Python/Estatística Descritivas - Titanic/train.csv'

# Leitura do arquivo em Excel
dados = pd.read_csv(caminho_arquivo, sep=',')
print(dados.head())

# Porcentagem de mulheres que sobreviveram | Nota-se que as mulheres tiveram uma alta taxa de sobrevivencia
women = dados.loc[dados.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)*100
print(f'\n\nPorcentagens dos homens e mulheres sobreviventes:\nDas {len(women)} mulheres {round(rate_women, 2)}% sobreviveram')

# Porcentagem de homens que sobreviveram | Nota-se que os tiveram uma alta taxa de mortalidade
man = dados.loc[dados.Sex == 'male']["Survived"]
rate_women = sum(man)/len(man)*100
print(f'Dos {len(man)} homens {round(rate_women, 2)}% sobreviveram')

# Nota-se que a  média e a mediana da idade estão próximas o que indica que os pontos estão mais distribuídos em torno de um ponto central
media = dados['Age'].median()
mediana = dados['Age'].mean()
print(f'\n\nAnalise das idades:\nMedia: {media}\nMediana: {mediana}')

# Criando a figura e os subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Filtrando apenas os passageiros masculinos
male_passengers = dados[dados['Sex'] == 'male']

# Filtrando os passageiros masculinos que sobreviveram e não sobreviveram
male_survived = male_passengers[male_passengers['Survived'] == 1]
male_not_survived = male_passengers[male_passengers['Survived'] == 0]

# Plotando o gráfico de dispersão para passageiros masculinos
axs[0].scatter(male_survived['Age'], male_survived.index, label='Male - Survived', c='g', alpha=0.5)
axs[0].scatter(male_not_survived['Age'], male_not_survived.index, label='Male - Not Survived', c='r', alpha=0.5)
axs[0].set_xlabel('Age')
axs[0].set_ylabel('Passenger Index')
axs[0].set_title('Passengers - Male')
axs[0].legend()

# Filtrando apenas as passageiras femininas
female_passengers = dados[dados['Sex'] == 'female']

# Filtrando as passageiras femininas que sobreviveram e não sobreviveram
female_survived = female_passengers[female_passengers['Survived'] == 1]
female_not_survived = female_passengers[female_passengers['Survived'] == 0]

# Plotando o gráfico de dispersão para passageiras femininas
axs[1].scatter(female_survived['Age'], female_survived.index, label='Female - Survived', c='b', alpha=0.5)
axs[1].scatter(female_not_survived['Age'], female_not_survived.index, label='Female - Not Survived', c='m', alpha=0.5)
axs[1].set_xlabel('Age')
axs[1].set_ylabel('Passenger Index')
axs[1].set_title('Passengers - Female')
axs[1].legend()

# Ajustando o espaçamento entre os subplots
plt.tight_layout()

# Exibindo os gráficos
plt.show()
