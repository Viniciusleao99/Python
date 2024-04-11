"""Numa certa agência bancária, as contas são identificadas por números de até seis dígitos seguidos de um dígito 
verificador, calculado conforme exemplificado a seguir. Dado um número de conta n, exiba o número de conta completo 
correspondente. Seja n = 7314 o número da conta. Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15;
Calculamos o resto da divisão de s por 10 e obtemos o dígito d = 5. Número de conta completo: 007314−5"""

numero_conta = int(input("Digite o número da conta (sem dígito verificador): "))

soma_digitos = 0
while numero_conta > 0:
  digito = numero_conta % 10
  soma_digitos += digito
  numero_conta //= 10

digito_verificador = 10 - (soma_digitos % 10)

numero_conta_completo = f"{numero_conta:06d}{digito_verificador}"

print(f"Número da conta completo: {numero_conta_completo}")