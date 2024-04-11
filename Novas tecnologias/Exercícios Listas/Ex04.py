"""A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T= [-10, -8, 0, 1, 2, 5, -2,-4]. 
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média."""

T= [-10, -8, 0, 1, 2, 5, -2,-4]
soma = 0

T.sort(reverse = True)
maior_temperatura = T[0] 

T.sort()
menor_temperatura = T[0]

for num in T:
    soma += num
media = soma / len(T)

print(f"A maior temperatura é {maior_temperatura}, a menor temperatura é {menor_temperatura} e a média das temperaturas é {media:.0f}")