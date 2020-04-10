# -*- coding: utf-8 -*-
# Visualização de dados em python

import matplotlib.pyplot as plt

# Fazendo comparação com dois gráficos de barras:

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

eixox = "Eixo x"
eixoy = "Eixo y"

# Legendas:

plt.title(u"Gráfico de barras 2") # u: unicode string (aceita acentos)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo 1") # plota gráfico de barras
plt.bar(x2, y2, label = "Grupo 2") # e atribui legenda pras cores
plt.legend()

plt.show()