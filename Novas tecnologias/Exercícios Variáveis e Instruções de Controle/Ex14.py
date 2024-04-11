#Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu fatorial.

numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
  print("Erro: O número deve ser não negativo.")
  exit()

fatorial = 1
for i in range(1, numero + 1):
  fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")