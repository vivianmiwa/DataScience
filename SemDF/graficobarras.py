# -*- coding: utf-8 -*-
# Visualização de dados em python

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] # barras
y = [2, 3, 7, 1, 0] # tamanho das barras

eixox = "Eixo x"
eixoy = "Eixo y"

# Legendas:
plt.title(u"Gráfico de barras") # u: unicode string (aceita acentos) 
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y) # plota um gráfico de barras
plt.show()