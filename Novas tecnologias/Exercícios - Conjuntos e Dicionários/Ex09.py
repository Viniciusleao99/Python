"""Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações. 
Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
 ◦ os elementos que não mudaram
 ◦ os novos elementos
 ◦ os elementos que foram removidos"""

lista1 = [5,55,8,2,56,74,167,97]
lista2 = [88,5,36,74,124,2]

versao1 = set(lista1)
versao2 = set(lista2)

# Elementos que não mudaram
elementos_n_modificados = lista1.intersection(versao2)
print("Elementos que não mudaram:", elementos_n_modificados)

# Novos elementos
novos_elementos = versao2.difference(versao1)
print("Novos elementos:", novos_elementos)

# Elementos que foram removidos
elementos_removidos = versao1.difference(versao2)
print("Elementos que foram removidos:", elementos_removidos)