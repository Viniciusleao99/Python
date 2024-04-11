#Escreva um programa que leia um número e verifique se é ou não um número primo.

numero = int(input("Digite um número: "))

primo = True

for i in range(2, numero):
  if numero % i == 0:
    primo = False
    break

if primo:
  print(f"{numero} é um número primo.")
else:
  print(f"{numero} não é um número primo.")

  #Pesquisei teoremas