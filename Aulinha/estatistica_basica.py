import pandas as pd
import numpy as np
import random

# Entrada
number = int(input("Digite quantos números você quer: "))

# Amostra de dados
dados = sorted([random.randint(1, 10) for _ in range(number)])

# Imprime os números gerados aleatoriamente
print(f'\nNúmeros gerados aleatoriamente: {dados}')

# Cálculo da Média
media = np.mean(dados)
media = round(media, 2)
print(f'\nCálculo de estatísticas básicas:\nMédia: {media}')

# Cálculo da Mediana
mediana = np.median(dados)
mediana = round(mediana, 2)
print(f'Mediana: {mediana}')

# Cálculo da Moda
moda = pd.Series(dados).mode()
print(f'Moda: {moda}')

# Cálculo da Amplitude
amplitude = np.max(dados) - np.min(dados)
amplitude = round(amplitude, 2)
print(f'\nEstatistica Descritiva:\nAmplitude: {amplitude}')

# Cálculo do Desvio Padrão
desvio_padrao = np.std(dados)
desvio_padrao = round(desvio_padrao, 2)
print(f'Desvio Padrão: {desvio_padrao}')

# Cálculo da Variância
variancia = np.var(dados)
variancia = round(variancia, 2)
print(f'Variância: {variancia}')

# Cálculo do Coeficiente de Variação
coef_variacao = (desvio_padrao / media) * 100
coef_variacao = round(coef_variacao, 2)
print(f'Coeficiente de Variação: {coef_variacao}')

# Cálculo da Curtose
curtose = pd.Series(dados).kurtosis()
curtose = round(curtose, 2)
print(f'Curtose: {curtose}')

#Calculo de separatrizes
q1 = np.quantile(dados, 0.25)
q1 = round(q1,2)
q2 = np.quantile(dados, 0.50)
q2 = round(q2,2)
q3 = np.quantile(dados, 0.75)
q3 = round(q3,2)

print('\nCalculo de separatrizes:')
print(f'Primeiro Quartil: {q1}\nSegundo  Quartil: {q2}\nTerceiro Quartil: {q3}')


