#Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

import math

numero = int(input("Digite um número: "))

primo = True

for i in range(2, int(math.sqrt(numero)) + 1, 2):
  if numero % i == 0:
    primo = False
    break

if primo:
  print(f"{numero} é um número primo.")
else:
  print(f"{numero} não é um número primo.")

    #Pesquisei teoremas