# -*- coding: UTF-8 -*-
# Crescimento da População Brasileira 1980-2016
# Informações tiradas do banco de dados do DataSus
import matplotlib.pyplot as plt


dados = open("populacao_brasileira.csv").readlines()

x = [] # vetor para armazenar anos
y = [] # vetor para armazenar populacao

for i in range(len(dados)):
	if i != 0: # ignora a primeira linha
		linha = dados[i].split(";") # separa ano de populacao armazenando no vetor
		x.append(int(linha[0])) # 1º indice: ano
		y.append(int(linha[1])) # 2º indice: populacao

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color="k", linestyle="--")
plt.title(u"Crescimento da População Brasileira 1980-2016")
plt.xlabel(u"Ano")
plt.ylabel(u"População x100.000.000")
#plt.show()
plt.savefig("populacao_brasileira.png", dpi=300)