# -*- coding: utf-8 -*-
# Visualização de dados em python

import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Legendas:
plt.title(u"Gráfico de linhas") # u: unicode string (aceita acentos) 
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.plot(x, y) # plota um gráfico de linhas
plt.show()