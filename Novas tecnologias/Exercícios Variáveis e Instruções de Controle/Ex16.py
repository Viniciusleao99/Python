"""A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros termos são iguais a 1, e a partir do 
terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da série de Fibonacci."""

numero = int(input("Digite um número natural (n ≥ 3): "))

if numero < 3:
  print("Erro: O número deve ser maior ou igual a 3.")
  exit()

a = 1
b = 1
c = 0

for i in range(3, numero + 1):
  c = a + b
  a = b
  b = c

print(f"O {numero}-ésimo termo da série de Fibonacci é {c}")