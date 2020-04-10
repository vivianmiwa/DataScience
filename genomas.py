# -*- coding: UTF-8 -*-

entrada = open("human.fasta").read()
saida = open("human.html", "w")

cont = {} # dicionario

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0 # preenche combinacoes com 0

entrada = entrada.replace("\n","") # apaga a quebra de linha

for k in range(len(entrada)-1): # ajunta pares, excluindo o ultimo caractere que é impar 
	cont[entrada[k]+entrada[k+1]] += 1 # soma mais um a cada combinacao feita

# html:
i = 1

for k in cont:
	transparencia = cont[k]/max(cont.values()) # pega todos os valores e divide pelo maior
	saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>") # nivel de transparencia

	if i%4 == 0: # se for divisivel por 4
		saida.write("<div style='clear:both'</div>")
	i+=1

saida.close()