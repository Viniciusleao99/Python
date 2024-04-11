#Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar ou par.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
  print("O número", numero, "é par.")
else:
  print("O número", numero, "é ímpar.")