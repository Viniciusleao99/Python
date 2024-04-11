"""Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. 
Imprima a tabuada da operaçãoescolhida. Repita até que a opção saída seja escolhida."""

def calcular_tabuada(operacao, numero):

  print(f"Tabuada do {numero} ({operacao}):")
  for i in range(1, 11):
    resultado = eval(f"{numero} {operacao} {i}")
    print(f"{numero} {operacao} {i} = {resultado}")

def main():

  while True:
 
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = int(input("Digite sua opção: "))

    if opcao not in range(1, 6):
      print("Opção inválida.")
      continue

    if opcao == 5:
      break

    numero = int(input("Digite um número: "))

    operacao = "+"
    
    match opcao:
      case 1:
        operacao = "+"
      case 2:
        operacao = "-"
      case 3:
        operacao = "*"
      case 4:
        operacao = "/"

    calcular_tabuada(operacao, numero)

if __name__ == "__main__":
  main()