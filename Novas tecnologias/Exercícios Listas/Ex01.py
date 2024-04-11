#Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52] faça um programa que:

#a.imprima o maior elemento;

# lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

# lista.sort(reverse = True)
# print(lista[0])

# #b.imprima o menor elemento;

# lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

# lista.sort()
# print(lista[0])

#c.imprima os números pares;

# lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

# print("Números pares da lista:")

# for num in lista:
    
#     if num % 2 == 0:
        
#       print(num, end="")

#d.imprima o número de ocorrências do primeiro elemento da lista;

# lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
# ocorrencias = 0

# for num in lista:
#     if num == lista[0]:
#         ocorrencias += 1
# print(ocorrencias)

#e. imprima a média dos elementos;

# lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
# soma = 0

# for num in lista:
#     soma += num

# media = soma / len(lista)

# print (f"{media:.2f}")

#f. imprima a soma dos elementos de valor negativo

# lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
# soma = 0

# for num in lista:
#     if num < 0:
#         soma += num
# print(soma)