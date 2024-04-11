#Melhore o programa anterior (Ex.04), permitindo a entrada de números com quaisquer dígitos.

numero = input("Digite um número com quaisquer dígitos: ")

comprimento = len(numero)

if comprimento != 5:
  print("O número deve ter 5 dígitos.")
  exit()

digito1 = numero[0]
digito2 = numero[1]
digito3 = numero[2]
digito4 = numero[3]
digito5 = numero[4]

print(f"{digito1}   {digito2}   {digito3}   {digito4}   {digito5}")