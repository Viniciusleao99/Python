"""Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os 
parênteses foram abertos e fechados na ordem correta. O exemplo está na imagem."""

expressao = input("Digite uma expressão com parênteses: ").strip()

pilha = []

for caractere in expressao:

    if caractere == "(":
        pilha.append(caractere)
  
    elif caractere == ")":
    
        if not pilha:
            print("Erro! Parênteses não foram abertos e fechados corretamente.")
            break
        pilha.pop()
else:
    if pilha:
        print("Erro! Parênteses não foram abertos e fechados corretamente.")
    else:
        print("Os parênteses foram abertos e fechados na ordem correta.")
