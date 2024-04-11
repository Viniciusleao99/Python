# Escreva um programa que copie os valores pares para uma lista e os valores ímpares para outra lista. A lista inicialmente de valores é V=[9,8,7,12,0,13,21].

V=[9,8,7,12,0,13,21]
lista_pares = []
lista_impares = []

for num in V:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f"A lista de valores pares é: {lista_pares}.\nE a lista de valores impares é {lista_impares}.")