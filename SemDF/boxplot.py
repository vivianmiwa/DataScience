# -*- coding: UTF-8 -*-
# Boxplot (Diagrama de Caixa): tecnica de visualizacao de dados que 
# representa a variação de dados por meio de quartis
import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
	num_aleatorio = random.randint(0, 10000)
	vetor.append(num_aleatorio)

plt.boxplot(vetor)
plt.title(u"Boxplot")
plt.show()