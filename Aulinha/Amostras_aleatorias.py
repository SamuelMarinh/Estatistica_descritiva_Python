#Obtenção de amostras com python

import random
import numpy as np

ran = []

for i in range(100):
    ran.append(random.random())

#Reorganizar os itens de forma aleatória
random.shuffle(ran)

#Buscar uma amostra aleatória
print(random.choice(ran))

#Extrair varias amostra aleatória
print(random.sample(ran,10))

