# -*- coding: utf-8 -*-
# Visualização de dados em python

import matplotlib.pyplot as plt

# Gráfico de pontos/dispersão/scatterplot:

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

eixox = "Eixo x"
eixoy = "Eixo y"

# Legendas:

plt.title(u"Scatterplot: Gráfico de dispersão") # u: unicode string (aceita acentos)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="b", linestyle=":")
# atributos: (cor, tipo da linha)
plt.scatter(x, y, label="Pontos", color="m", marker="*", s=200)
# atributos: (cor, marcador (bolinha), tamanho)
plt.legend()
#plt.show()
plt.savefig("Graficopontos.png", dpi=300) # dpi: resolução da imagem
# pdf: formato vetorial (alta qualidade)