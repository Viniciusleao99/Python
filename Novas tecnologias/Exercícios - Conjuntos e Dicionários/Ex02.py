"""Escreva um programa que compare duas listas. Utilizando operações com
conjuntos, imprima:
a. os valores comuns às duas listas
b. os valores que só existem na primeira
c. os valores que existem apenas na segunda
d. uma lista com os elementos não repetidos das duas listas.
e. a primeira lista sem os elementos repetidos na segunda"""

lista1 = [5,55,8,2,56,74,167,97]
lista2 = [88,5,36,74,124,2]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

# a. Valores comuns às duas listas
valores_comuns = conjunto1.intersection(conjunto2)
print("Valores comuns às duas listas:", valores_comuns)

# b. Valores que só existem na primeira
valores_lista1 = conjunto1.difference(conjunto2)
print("Valores que só existem na primeira lista:", valores_lista1)

# c. Valores que existem apenas na segunda
valores_lista2 = conjunto2.difference(conjunto1)
print("Valores que só existem na segunda lista:", valores_lista2)

# d. Uma lista com os elementos não repetidos das duas listas
elementos_unicos = conjunto1.union(conjunto2)
print("Elementos não repetidos das duas listas:", elementos_unicos)

# e. A primeira lista sem os elementos repetidos na segunda
lista1_sem_lista2 = conjunto1.difference(conjunto2)
print("A primeira lista sem os elementos repetidos na segunda:", lista1_sem_lista2)
