""" Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos 
individuais e imprime os dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o 
número 42339, o programa deve imprimir: 4 2 3 3 9."""

numero = int(input("Digite um número de cinco dígitos: "))

n1 = numero // 10000
n2 = (numero % 10000) // 1000
n3 = (numero % 1000) // 100
n4 = (numero % 100) // 10
n5 = numero % 10

print(n1, " ", n2, " ", n3, " ", n4, " ", n5)